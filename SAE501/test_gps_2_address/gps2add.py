from geopy.geocoders import Nominatim
from functools import partial

# Initialize the geocoder
geolocator = Nominatim(user_agent="pycomtracer")
reverse = partial(geolocator.reverse, language="fr")
# Coordinates (latitude, longitude)
latitude = 48.076349
longitude = 7.363704

# Get address
location = reverse((latitude, longitude))
address = location.raw.get("address", {})

nbr = address.get("house_number", "N/A")  # House number
rue = address.get("road", "N/A")  # Street name
ville = address.get("city", address.get("town", address.get("village", "N/A")))  # City name
code_postal = address.get("postcode", "N/A")  # Zip code
pays = address.get("country", "N/A")  # Country

# Print the extracted information
print(f"{nbr} {rue}, {code_postal} {ville}, {pays}")