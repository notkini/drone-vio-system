# src/heatmap_engine.py

import csv
import folium
from folium.plugins import HeatMap
from config import LOG_FILE, HEATMAP_OUTPUT


def generate_heatmap():

    points = []

    try:
        with open(LOG_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                points.append([float(row["latitude"]), float(row["longitude"])])
    except FileNotFoundError:
        print("No violations logged yet.")
        return

    if not points:
        print("No data for heatmap.")
        return

    mumbai_map = folium.Map(location=[19.0760, 72.8777], zoom_start=12)

    HeatMap(points).add_to(mumbai_map)

    mumbai_map.save(HEATMAP_OUTPUT)

    print("Heatmap saved:", HEATMAP_OUTPUT)
