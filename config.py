# ===== MODEL CONFIG =====

MODEL_PATH = "models/model_edgetpu.tflite"

# Coral requires this
USE_TPU = True

# Input size used during export
INPUT_SIZE = (640, 640)

# Detection threshold
CONF_THRESHOLD = 0.5

# ===== CLASS MAPPING =====

CLASS_NAMES = {
    0: "helmet",
    1: "no_helmet",
    2: "rider",
    3: "plate"
}

# ONLY THIS CLASS = violation
VIOLATION_CLASS_ID = 1

# ===== FILE PATHS =====

INPUT_DIR = "input"
OUTPUT_DIR = "output"
LOG_DIR = "logs"

# ===== HEATMAP DEFAULT (used if GPS unavailable) =====
DEFAULT_LAT = 19.0760
DEFAULT_LON = 72.8777
