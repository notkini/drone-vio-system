import os
from src.detector import Detector
from src.gps_reader import GPSReader
from src.violation_logger import ViolationLogger
from src.heatmap_engine import HeatmapEngine
import config


# Create required folders automatically
os.makedirs(config.INPUT_FOLDER, exist_ok=True)
os.makedirs(config.OUTPUT_FOLDER, exist_ok=True)
os.makedirs("data/logs", exist_ok=True)


def main():

    print("Initializing system...")

    detector = Detector(config.MODEL_PATH)
    gps = GPSReader()
    logger = ViolationLogger(config.LOG_FILE)

    print("Processing images...")

    for filename in os.listdir(config.INPUT_FOLDER):

        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img_path = os.path.join(config.INPUT_FOLDER, filename)

        print(f"Analyzing: {filename}")

        violations = detector.detect(img_path)

        if violations:
            lat, lon = gps.get_location()
            logger.log(lat, lon, filename)
            print("Violation detected!")
        else:
            print("No violation.")

    print("Generating heatmap...")

    heatmap = HeatmapEngine(config.LOG_FILE, config.HEATMAP_OUTPUT)
    heatmap.generate()

    print("Done.")


if __name__ == "__main__":
    main()
