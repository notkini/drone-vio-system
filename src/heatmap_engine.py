import os
import pandas as pd
import folium
from folium.plugins import HeatMap


class HeatmapEngine:

    def __init__(self, log_file, output_file):

        self.log_file = log_file
        self.output_file = output_file

    def generate(self):

        if not os.path.exists(self.log_file):
            print("No data for heatmap.")
            return

        df = pd.read_csv(self.log_file)

        if df.empty:
            print("No data for heatmap.")
            return

        m = folium.Map(location=[df.latitude.mean(), df.longitude.mean()], zoom_start=12)

        HeatMap(df[["latitude", "longitude"]].values).add_to(m)

        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

        m.save(self.output_file)

        print(f"Heatmap saved: {self.output_file}")
