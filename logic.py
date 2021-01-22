import json
from distance import getDistanceFromLatLonInKm

file_path = 'resources/restaurants.json'

def process(req_lat, req_lon):

    in_range = []
    in_range_with_distance = []

    with open(file_path) as f:
        data = json.load(f)

        for restaurant in data['restaurants']:
            distance = getDistanceFromLatLonInKm(req_lat, req_lon, restaurant['location'][1], restaurant['location'][0])
            if distance < 1.5:
                in_range.append(restaurant)
                in_range_with_distance.append((restaurant, distance))

    popular_restaurants = sorted(in_range_with_distance, key=lambda x : [x[0]['online'], x[0]['popularity']], reverse=True)
    new_restaurants = sorted(in_range_with_distance, key=lambda x : [x[0]['online'], x[0]['launch_date']], reverse=True)
    nearby_restaurants = sorted(in_range_with_distance, key=lambda x : [x[0]['online'], -x[1]], reverse=True)

    popular_restaurants = [x[0] for x in popular_restaurants]
    new_restaurants = [x[0] for x in new_restaurants]
    nearby_restaurants = [x[0] for x in nearby_restaurants]

    result = {
        'sections': [
            {
                'title': 'Popular Restaurants',
                'restaurants': popular_restaurants[:10]
            },
            {
                'title': 'New Restaurants',
                'restaurants': new_restaurants[:10]
            },
            {
                'title': 'Nearby Restaurants',
                'restaurants': nearby_restaurants[:10]
            }
        ]
    }

    return result
