# api/urls.py

from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('get_player_id/', views.get_player_id, name='get_player_id'), # Add a URL route for the view
    path('async_get_team_data/', views.async_get_team_data, name='async_get_team_data'),
]