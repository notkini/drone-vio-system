# config.py

# ===============================
# MODEL
# ===============================
MODEL_PATH = "models/model_edgetpu.tflite"

# ===============================
# DATA PATHS
# ===============================
INPUT_FOLDER = "data/input"
OUTPUT_FOLDER = "data/output"

LOG_FILE = "data/logs/violations.csv"
HEATMAP_OUTPUT = "data/output/heatmap.html"

# ===============================
# DETECTION SETTINGS
# ===============================
CONF_THRESHOLD = 0.4

# Set your class IDs here (example)
NO_HELMET_CLASS_ID = 1   # change if needed
