class WaypointNotFoundError(Exception):
    def __init__(self, waypoint, message='was not found, be more specific using a State or use the Zip Code'):
        self.waypoint = waypoint
        self.message = f'Your entry {waypoint}: {message}'
        super().__init__(self.message)