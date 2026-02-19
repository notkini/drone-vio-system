# src/gps_reader.py

import random

class GPSReader:

    def get_location(self):

        # Example: Mumbai coordinates
        lat = 19.07 + random.uniform(-0.01, 0.01)
        lon = 72.87 + random.uniform(-0.01, 0.01)

        return lat, lon
