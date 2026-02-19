# main.py

import os
from src.detector import HelmetDetector
from src.gps_reader import GPSReader
from src.violation_logger import ViolationLogger
from src.heatmap_engine import HeatmapEngine
import config


# =====================================
# CREATE REQUIRED FOLDERS
# =====================================
os.makedirs(config.INPUT_DIR, exist_ok=True)
os.makedirs(config.OUTPUT_DIR, exist_ok=True)
os.makedirs(config.LOG_DIR, exist_ok=True)


def main():

    print("Initializing system...")

    detector = HelmetDetector()
    gps = GPSReader()

    log_file = os.path.join(config.LOG_DIR, "violations.csv")
    logger = ViolationLogger(log_file)

    print("Processing images...")

    for filename in os.listdir(config.INPUT_DIR):

        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img_path = os.path.join(config.INPUT_DIR, filename)

        print(f"\nAnalyzing: {filename}")

        # Read image
        import cv2
        image = cv2.imread(img_path)

        if image is None:
            print("Could not read image.")
            continue

        detections, violation = detector.detect(image)

        if violation:

            lat, lon = gps.get_location()
            logger.log(lat, lon, filename)

            print("🚨 VIOLATION: No helmet detected!")

            # Save violation image
            out_path = os.path.join(config.OUTPUT_DIR, filename)
            cv2.imwrite(out_path, image)

        else:
            print("No violation.")

        # Print detections
        for det in detections:
            print(
                f"Detected: {det['label']} "
                f"(score={det['score']:.2f})"
            )

    print("\nGenerating heatmap...")

    heatmap_output = os.path.join(config.OUTPUT_DIR, "heatmap.html")
    heatmap = HeatmapEngine(log_file, heatmap_output)
    heatmap.generate()

    print("Done.")


if __name__ == "__main__":
    main()
