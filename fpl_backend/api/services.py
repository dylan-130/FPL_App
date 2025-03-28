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
                data = await response.json()
            current_event = next((event for event in data['events'] if event['is_current']), None)
            return current_event
    except Exception as e:
        logger.error(f"Error fetching current event: {e}")
        return None

async def get_team_data(player_id, gameweek):
    url = f'https://fantasy.premierleague.com/api/entry/{player_id}/event/{gameweek}/picks/'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
            team_data = []
            for pick in data['picks']:
                player_info = pick['element']
                player_position = pick['position']
                team_data.append({
                    'player_id': player_info,
                    'position': player_position,
                    'points': pick['total_points'],
                    'captain': pick['captain'],
                    'vice_captain': pick['vice_captain']
                })
            return team_data
    except Exception as e:
        logger.error(f"Error fetching team data: {e}")
        return []
