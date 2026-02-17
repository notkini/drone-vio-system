# src/gps_reader.py

import random
from config import DEFAULT_LAT, DEFAULT_LON


def get_current_location():
    """
    Replace this with real GPS module reading on Raspberry Pi.
    For now returns simulated nearby coordinates.
    """

    lat = DEFAULT_LAT + random.uniform(-0.01, 0.01)
    lon = DEFAULT_LON + random.uniform(-0.01, 0.01)

    return lat, lon
