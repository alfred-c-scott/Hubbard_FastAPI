import json
import math



# checks for two cities with same zip codes
def dup_check(city_list):
    dup = False
    dup_zips = []
    city_dict = {}
    dup_ct = 0
    city_list_copy = city_list
    for i, city in enumerate(city_list):
        z_0 = city["postal_code"]
        for j, c in enumerate(city_list_copy):
            if i != j:
                if z_0 == c["postal_code"]:
                    dup_ct += 1
                    city_dict = c
                    dup_zips.append(city_dict)

    # returns dictionary with boolean, num of cities with duplicated zips,
    # and list of cities
    return {"duplicates": dup, "duplicate_count": dup_ct, "zips": dup_zips}


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

# False Pass, Alaska 
lat1 = 54.8542  # Latitude of Location 1 
lon1 = -163.4113  # Longitude of Location 1
# Potosi, Missouri
lat2 = 37.9549  # Latitude of Location 2
lon2 = -90.8415  # Longitude of Location 2

distance = distance_lat_lon(lat1, lon1, lat2, lon2)

print(f"The distance between the two locations is approximately {distance:.2f} miles.")
