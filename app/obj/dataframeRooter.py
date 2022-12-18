from dataclasses import dataclass

import pandas as pd

@dataclass
class DataframeRooter:
    csv_file : str

    def __init__(self, csv_file) -> None:
        self.csv_file = csv_file

    def get_dataframe(self):
        return pd.read_csv(self.csv_file)
