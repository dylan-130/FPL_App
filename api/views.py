# api/views.py
import logging
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .services import get_player_id_from_api, get_current_event, get_team_data

# Logger to monitor the process
logger = logging.getLogger(__name__)

# Home endpoint for basic checks
def home(request):
    return HttpResponse("Welcome to the FPL API!")

# View to get player ID
@csrf_exempt
async def get_player_id(request):
    player_name = request.GET.get('playerName')
    team_name = request.GET.get('teamName')

    if not player_name or not team_name:
        return JsonResponse({'error': 'Player name or team name missing.'}, status=400)

    player_id = await get_player_id_from_api(player_name, team_name)
    if not player_id:
        return JsonResponse({'error': 'Player ID not found.'}, status=404)

    return JsonResponse({'player_id': player_id})

# View to get team data (player_id is now passed in)
@csrf_exempt
async def async_get_team_data(request):
    player_id = request.GET.get('playerId')

    if not player_id:
        return JsonResponse({'error': 'Player ID missing.'}, status=400)

    # Fetch the current event (gameweek)
    current_event = await get_current_event()

    if not current_event:
        # Return error if current event cannot be fetched
        return JsonResponse({'error': 'Could not fetch current event.'}, status=500)
    
    gameweek = current_event['id']
    logger.info(f"Fetched current event: {current_event}, gameweek: {gameweek}")

    # Fetch the team data based on player ID and gameweek
    team_data = await get_team_data(player_id, gameweek)

    if not team_data:
        # Return error if no team data is found
        return JsonResponse({'error': 'Team data not found.'}, status=404)

    # Return the fetched team data as a JSON response
    return JsonResponse(team_data, safe=False)