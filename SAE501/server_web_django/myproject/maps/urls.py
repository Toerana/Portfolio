
from django.urls import path
from .views import get_latest_coordinate, get_location_history, history_view, map_view, get_address
from .mqtt_shutdown import shutdown_view
urlpatterns = [
    path('', map_view, name="map"),
    path('history/', history_view, name="history"),  
    path('api/latest/', get_latest_coordinate, name="latest_coordinate"),
    path('api/history/', get_location_history, name="location_history"),  
    path('api/address/', get_address, name="address"),
    path('api/shutdown/', shutdown_view, name="shutdown"),
]
