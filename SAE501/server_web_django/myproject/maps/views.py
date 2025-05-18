from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Coordinate
from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
from functools import partial



@api_view(['GET'])
def get_latest_coordinate(request):
    coord = Coordinate.objects.last()
    if coord:
        return Response({"lat": coord.latitude, "lng": coord.longitude})
    return Response({"error": "No coordinates available"})

def map_view(request):
    return render(request, "map.html")


@api_view(['GET'])
def get_location_history(request):
    """Return the last 20 recorded GPS coordinates."""
    coordinates = Coordinate.objects.all().order_by('-timestamp')
    data = [{"id": c.id, "lat": c.latitude, "lng": c.longitude, "timestamp": c.timestamp} for c in coordinates]
    return Response(data)

def history_view(request):
    """Render the history page."""
    return render(request, "history.html")



app = Flask(__name__)


geolocator = Nominatim(user_agent="pycomtracer")
reverse = partial(geolocator.reverse, language="fr")

@api_view(['GET'])
def get_address(request):
    try:
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        if lat and lng:
            location = reverse((lat, lng))
            address = location.raw.get("address", {})
            nbr = address.get("house_number", "N/A")
            rue = address.get("road", "N/A")
            ville = address.get("city", address.get("town", address.get("village", "N/A")))
            code_postal = address.get("postcode", "N/A")
            pays = address.get("country", "N/A")
            full_address = f"{nbr} {rue}, {code_postal} {ville}, {pays}"
            return JsonResponse({"address": full_address})
        return JsonResponse({"error": "Invalid coordinates"}, status=400)
    except Exception as e:
        return JsonResponse({"error": "Invalid yeet coordinates"}, status=400)

