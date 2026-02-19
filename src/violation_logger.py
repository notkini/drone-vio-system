# src/violation_logger.py

import csv
import os
from datetime import datetime

class ViolationLogger:

    def __init__(self, log_file):

        self.log_file = log_file

        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        if not os.path.exists(log_file):
            with open(log_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "latitude", "longitude", "image"])

    def log(self, lat, lon, image_name):

        with open(self.log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now(),
                lat,
                lon,
                image_name
            ])
