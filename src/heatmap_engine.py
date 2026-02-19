# src/heatmap_engine.py

import pandas as pd
import folium
from folium.plugins import HeatMap

class HeatmapEngine:

    def __init__(self, log_file, output_file):
        self.log_file = log_file
        self.output_file = output_file

    def generate(self):

        try:
            df = pd.read_csv(self.log_file)

            if df.empty:
                print("No data for heatmap.")
                return

            m = folium.Map(
                location=[df["latitude"].mean(), df["longitude"].mean()],
                zoom_start=13
            )

            HeatMap(df[["latitude", "longitude"]]).add_to(m)

            m.save(self.output_file)

            print("Heatmap saved:", self.output_file)

        except Exception as e:
            print("Heatmap error:", e)
