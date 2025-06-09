from profiler import BaseProfiler
import pandas as pd
from datetime import datetime


class DemoDemographicProfiler(BaseProfiler):
    def clean_data(self):
        df = self.data

        # Keep only specific columns
        columns_to_keep = ["ehealth_id", "sex", "age", "occupation_holder", "dob"]
        df = df[columns_to_keep]

        # Drop rows with missing values in required columns
        df = df.dropna(subset=columns_to_keep)

        # Convert 'sex' to uppercase
        df["sex"] = df["sex"].astype(str).str.upper()
        current_year = datetime.now().year
        df["dob"] = (current_year - df["age"].astype(int)).astype(str) + "-01-01"

        self.data = df