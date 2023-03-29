class Route:
    def __init__(self, origin, destination, distance, duration, is_loaded=True):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.duration = duration
        self.is_loaded = is_loaded
        self.rate_per_mile = 0.00
        self.route_revenue = 0

    def toggle_is_loaded(self):
        self.is_loaded = not self.is_loaded
        print(f'{self.origin.city}-{self.destination.city} loaded option is now marked {self.is_loaded}')

    def calculate_route_revenue(self):
        self.route_revenue = self.distance * self.rate_per_mile

    def __repr__(self):
        return f'{self.origin}-{self.destination}: {self.distance} Miles. Rate: ${self.rate} Loaded? {self.is_loaded}'

    def update_rate_per_mile(self, new_rate: float):
        if new_rate > 10:
            self.rate_per_mile = new_rate/self.distance
        else:
            self.rate_per_mile = new_rate