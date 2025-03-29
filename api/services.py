# api/services.py
import aiohttp
import logging

AWS_API_URL = "CLASSIFIED"
logger = logging.getLogger(__name__)

async def get_player_id_from_api(player_name, team_name):
    url = f"{AWS_API_URL}?teamName={team_name}&playerName={player_name}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if 'Player ID' in data:
                    return data['Player ID']
                return None
    except Exception as e:
        logger.error(f"Error fetching player ID: {e}")
        return None

async def get_current_event():
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                # Check if the response is successful
                if not response.ok:
                    logger.error(f"Failed to fetch bootstrap-static data. Status: {response.status}")
                    return None

                data = await response.json()

                # Find the current event
                current_event = next((event for event in data['events'] if event['is_current']), None)
                if not current_event:
                    logger.error("No current event found in bootstrap-static response.")
                    return None

                logger.info(f"Current event found: {current_event['id']}")
                return current_event

    except Exception as e:
        logger.error(f"Error fetching current event: {e}")
        return None
    
async def get_team_data(player_id, gameweek):
    url = f'https://fantasy.premierleague.com/api/entry/{player_id}/event/{gameweek}/picks/'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                # Check if response is successful
                if response.status != 200:
                    logger.error(f"FPL API Error: Status {response.status} for player {player_id}, GW {gameweek}")
                    return None
                data = await response.json()
                logger.info(f"Fetched team data: {data}")
                if 'picks' not in data:
                    logger.error(f"No 'picks' in response for player {player_id}, GW {gameweek}")
                    return None
                team_data = []
                for pick in data['picks']:
                    team_data.append({
                        'element': pick['element'],
                        'position': pick['position'],
                        'multiplier': pick['multiplier'],
                        'is_captain': pick['is_captain'],
                        'is_vice_captain': pick['is_vice_captain']
                    })
                return team_data
    except Exception as e:
        logger.error(f"Error in get_team_data: {e}")
        return None