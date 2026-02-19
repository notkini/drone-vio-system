# config.py

MODEL_PATH = "models/model_edgetpu.tflite"

INPUT_FOLDER = "data/input"
OUTPUT_FOLDER = "data/output"

LOG_FILE = "data/logs/violations.csv"

HEATMAP_OUTPUT = "data/output/heatmap.html"


# ===== MODEL CLASSES =====

HELMET_CLASS_ID = 0
NO_HELMET_CLASS_ID = 1
RIDER_CLASS_ID = 2
PLATE_CLASS_ID = 3


# Optional dictionary (useful for debugging / future UI)

CLASS_NAMES = {
    0: "helmet",
    1: "no_helmet",
    2: "rider",
    3: "plate"
}


# Detection threshold
CONF_THRESHOLD = 0.4
