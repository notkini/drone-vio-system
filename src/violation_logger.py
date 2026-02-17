# src/violation_logger.py

import csv
import os
from config import LOG_FILE


def log_violation(lat, lon):

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["latitude", "longitude"])

        writer.writerow([lat, lon])
