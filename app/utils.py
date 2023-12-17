# python imports
import math

# third party imports
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def distance_lat_lon(lat_1, lon_1, lat_2, lon_2):
    # Radius of the Earth in miles
    earth_radius = 3958.8  # miles

    # Convert latitude and longitude from degrees to radians
    lat_1 = math.radians(lat_1)
    lon_1 = math.radians(lon_1)
    lat_2 = math.radians(lat_2)
    lon_2 = math.radians(lon_2)

    # Distance between two points on a sphere can be calculated using the
    # Haversine formula
    diff_lat = lat_2 - lat_1
    diff_lon = lon_2 - lon_1
    a = math.sin(diff_lat/2)**2 + math.cos(lat_1) * math.cos(lat_2) * math.sin(diff_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = earth_radius * c

    return distance