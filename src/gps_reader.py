import random


class GPSReader:

    def get_location(self):

        # Simulated GPS (Mumbai area)
        lat = random.uniform(18.90, 19.30)
        lon = random.uniform(72.70, 73.00)

        return lat, lon
