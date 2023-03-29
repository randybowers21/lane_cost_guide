#IMPORTS
#Python
import re
#3rd Party
import googlemaps
from tkinter import messagebox
#Local
from route import Route
from location import Location
from errors import WaypointNotFoundError
import config

#GOOGLE AUTH
API_KEY = config.API_KEY
gmaps = googlemaps.Client(key=API_KEY)

good_info = {
    'destination_addresses': ['Fontana, CA, USA', 'Moreno Valley, CA, USA', 'Tyler, TX, USA', 'Carthage, TX 75633, USA', 'Cedar City, UT, USA', 'St. George, UT, USA'],
    'origin_addresses': ['St. George, UT, USA', 'Fontana, CA, USA', 'Moreno Valley, CA, USA', 'Tyler, TX, USA', 'Carthage, TX 75633, USA', 'Cedar City, UT, USA'], 
    'rows': [
            {'elements': [
                {'distance': {'text': '342 mi', 'value': 550054}, 'duration': {'text': '5 hours 16 mins', 'value': 18939}, 'status': 'OK'},
                {'distance': {'text': '361 mi', 'value': 580750}, 'duration': {'text': '5 hours 28 mins', 'value': 19677}, 'status': 'OK'},
                {'distance': {'text': '1,269 mi', 'value': 2042564}, 'duration': {'text': '19 hours 39 mins', 'value': 70750}, 'status': 'OK'},
                {'distance': {'text': '1,330 mi', 'value': 2139647}, 'duration': {'text': '20 hours 33 mins', 'value': 73961}, 'status': 'OK'},
                {'distance': {'text': '52.2 mi', 'value': 83970}, 'duration': {'text': '52 mins', 'value': 3091}, 'status': 'OK'},
                {'distance': {'text': '1 ft', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}
                ]},
            {'elements': [
                {'distance': {'text': '1 ft', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'},
                {'distance': {'text': '24.8 mi', 'value': 39837}, 'duration': {'text': '33 mins', 'value': 1952}, 'status': 'OK'}, 
                {'distance': {'text': '1,487 mi', 'value': 2393260}, 'duration': {'text': '21 hours 43 mins', 'value': 78169}, 'status': 'OK'}, 
                {'distance': {'text': '1,547 mi', 'value': 2490343}, 'duration': {'text': '22 hours 36 mins', 'value': 81380}, 'status': 'OK'},
                {'distance': {'text': '393 mi', 'value': 631764}, 'duration': {'text': '5 hours 58 mins', 'value': 21499}, 'status': 'OK'}, 
                {'distance': {'text': '341 mi', 'value': 549363}, 'duration': {'text': '5 hours 15 mins', 'value': 18883}, 'status': 'OK'}
                ]}, 
            {'elements': [
                {'distance': {'text': '20.0 mi', 'value': 32193}, 'duration': {'text': '31 mins', 'value': 1881}, 'status': 'OK'}, 
                {'distance': {'text': '1 ft', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, 
                {'distance': {'text': '1,470 mi', 'value': 2366271}, 'duration': {'text': '21 hours 25 mins', 'value': 77119}, 'status': 'OK'}, 
                {'distance': {'text': '1,531 mi', 'value': 2463354}, 'duration': {'text': '22 hours 19 mins', 'value': 80331}, 'status': 'OK'}, 
                {'distance': {'text': '412 mi', 'value': 663005}, 'duration': {'text': '6 hours 10 mins', 'value': 22229}, 'status': 'OK'}, 
                {'distance': {'text': '361 mi', 'value': 580604}, 'duration': {'text': '5 hours 27 mins', 'value': 19613}, 'status': 'OK'}
                ]}, 
            {'elements': [
                {'distance': {'text': '1,487 mi', 'value': 2393824}, 'duration': {'text': '21 hours 42 mins', 'value': 78147}, 'status': 'OK'}, 
                {'distance': {'text': '1,471 mi', 'value': 2366805}, 'duration': {'text': '21 hours 25 mins', 'value': 77107}, 'status': 'OK'}, 
                {'distance': {'text': '1 ft', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, 
                {'distance': {'text': '61.0 mi', 'value': 98170}, 'duration': {'text': '1 hour 9 mins', 'value': 4156}, 'status': 'OK'}, 
                {'distance': {'text': '1,287 mi', 'value': 2071394}, 'duration': {'text': '19 hours 57 mins', 'value': 71801}, 'status': 'OK'}, 
                {'distance': {'text': '1,269 mi', 'value': 2041599}, 'duration': {'text': '19 hours 42 mins', 'value': 70923}, 'status': 'OK'}
                ]}, 
            {'elements': [
                {'distance': {'text': '1,549 mi', 'value': 2492521}, 'duration': {'text': '22 hours 35 mins', 'value': 81276}, 'status': 'OK'}, 
                {'distance': {'text': '1,532 mi', 'value': 2465502}, 'duration': {'text': '22 hours 17 mins', 'value': 80236}, 'status': 'OK'}, 
                {'distance': {'text': '60.9 mi', 'value': 98039}, 'duration': {'text': '1 hour 9 mins', 'value': 4123}, 'status': 'OK'}, 
                {'distance': {'text': '1 ft', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, 
                {'distance': {'text': '1,348 mi', 'value': 2170091}, 'duration': {'text': '20 hours 49 mins', 'value': 74930}, 'status': 'OK'}, 
                {'distance': {'text': '1,330 mi', 'value': 2140296}, 'duration': {'text': '20 hours 34 mins', 'value': 74051}, 'status': 'OK'}
                ]}, 
            {'elements': [
                {'distance': {'text': '393 mi', 'value': 632708}, 'duration': {'text': '5 hours 58 mins', 'value': 21491}, 'status': 'OK'},
                {'distance': {'text': '412 mi', 'value': 663405}, 'duration': {'text': '6 hours 10 mins', 'value': 22229}, 'status': 'OK'}, 
                {'distance': {'text': '1,288 mi', 'value': 2072678}, 'duration': {'text': '19 hours 55 mins', 'value': 71724}, 'status': 'OK'}, 
                {'distance': {'text': '1,348 mi', 'value': 2169761}, 'duration': {'text': '20 hours 49 mins', 'value': 74935}, 'status': 'OK'}, 
                {'distance': {'text': '1 ft', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}, 
                {'distance': {'text': '52.2 mi', 'value': 84049}, 'duration': {'text': '50 mins', 'value': 2992}, 'status': 'OK'}
                ]}
        ], 'status': 'OK'}

bad_info = {
    'destination_addresses': ['Carthage, Tunisia', 'St. George, UT, USA'], 
    'origin_addresses': ['St. George, UT, USA', 'Carthage, Tunisia'], 
    'rows': [{'elements':[
                    {'status': 'ZERO_RESULTS'},
                    {'distance': {'text': '1 ft', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'}   
                        ]},
            {'elements':[
                    {'distance': {'text': '1 ft', 'value': 0}, 'duration': {'text': '1 min', 'value': 0}, 'status': 'OK'},
                    {'status': 'ZERO_RESULTS'}
            ]}], 
    'status': 'OK'}

class Lane:
    def __init__(self):
        self.cost_per_mile = 2.552
        self.waypoints = []
        self.routes = []
        self.total_distance = 0
        self.empty_distance = 0
        self.loaded_distance = 0
        self.total_duration = 0
        self.total_cost = 0
        self.deadhead_percent = 0
        self.total_revenue = 0

    def create_routes(self):
        google_info = None
        try:
            google_info = self.get_google_info()
        except WaypointNotFoundError as wne:
            print(wne)
            messagebox.showerror("error", wne)

        if google_info:
            origins = google_info['origin_addresses']
            destinations = google_info['destination_addresses']
            for index in range(len(google_info['origin_addresses'])):
                route_list = google_info['rows'][index]['elements']

                duration = self.convert_duration_to_minutes(route_list[index]['duration']['text'])
                distance = self.convert_distance_to_int(distance_string=route_list[index]['distance']['text'])
                origin = origins[index]
                destination = destinations[index]

                self.routes.append(Route(origin=Location(origin), destination=Location(destination), distance=distance, duration=duration))

            self.get_totals()

    def get_google_info(self):
        self.routes.clear()
        google_info = gmaps.distance_matrix(origins=self.waypoints[:-1], destinations=self.waypoints[1:], units='imperial')
        print('Request Made to Google')
        self.waypoints.clear()
        for row in google_info['rows']:
            for index, element in enumerate(row['elements']):
                if element['status'] == 'ZERO_RESULTS':
                    raise WaypointNotFoundError(waypoint=google_info['destination_addresses'][index])
        return google_info

    def convert_distance_to_int(self, distance_string):
        distance = distance_string.replace(',', '')
        distance = [float(s) for s in re.findall(r'-?\d+\.?\d*', distance)][0]
        return distance

    def convert_duration_to_minutes(self, duration_string):
        duration = [int(s) for s in re.findall(r'-?\d+\.?\d*', duration_string)]
        if duration:
            if len(duration) > 1:
                    return (duration[0] * 60) + duration[1]
            else:
                return duration[0]
        else:
            pass

    def calculate_deadhead(self):
        deadhead = self.empty_distance / self.total_distance
        if deadhead > 0:
            return deadhead * 100
        else: 
            return deadhead

    def get_totals(self):
        self.total_distance = sum(route.distance for route in self.routes)
        self.loaded_distance = sum(route.distance for route in self.routes if route.is_loaded)
        self.empty_distance = self.total_distance - self.loaded_distance
        self.total_duration = sum(route.duration for route in self.routes)
        self.total_cost = self.cost_per_mile * self.total_distance
        self.deadhead_percent = self.calculate_deadhead()
        self.total_revenue = sum(route.route_revenue for route in self.routes)
        self.cost_difference = self.total_revenue - self.total_cost
        self.rate_per_mile = self.total_revenue / self.total_distance