# api/views.py
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .services import get_player_id_from_api, get_current_event, get_team_data

def home(request):
    return HttpResponse("Welcome to the FPL API!")

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

@csrf_exempt
async def async_get_team_data(request):
    player_name = request.GET.get('playerName')
    team_name = request.GET.get('teamName')

    if not player_name or not team_name:
        return JsonResponse({'error': 'Player name or team name missing.'}, status=400)

    player_id = await get_player_id_from_api(player_name, team_name)
    if not player_id:
        return JsonResponse({'error': 'Player ID not found.'}, status=404)

    current_event = await get_current_event()
    if not current_event:
        return JsonResponse({'error': 'Could not fetch current event.'}, status=500)

    team_data = await get_team_data(player_id, current_event['id'])
    if not team_data:
        return JsonResponse({'error': 'Team data not found.'}, status=404)

    return JsonResponse({'team_data': team_data})