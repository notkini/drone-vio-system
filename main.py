# main.py

from src.detector import ViolationDetector
from src.gps_reader import get_current_location
from src.violation_logger import log_violation
from src.heatmap_engine import generate_heatmap
from config import MODEL_PATH


def main():

    detector = ViolationDetector(MODEL_PATH)

    image_path = "test.jpg"  # Replace with camera input later

    violation = detector.detect(image_path)

    if violation:
        print("Violation detected")

        lat, lon = get_current_location()

        print("Location:", lat, lon)

        log_violation(lat, lon)

        generate_heatmap()

    else:
        print("No violation")


if __name__ == "__main__":
    main()
