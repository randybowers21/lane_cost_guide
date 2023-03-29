from string import digits

class Location:
    def __init__(self, location_str):
        self.location_str = location_str
        self.get_city_state()

    def get_city_state(self):
        location_list = self.location_str.split(',')
        city = location_list[0]
        state = location_list[1]
        country = location_list[2]

        self.city = city.strip()
        self.state = ''.join([i for i in state if not i.isdigit()]).strip()
        self.country = country.strip()