"""Profiler for demographic data."""

from datetime import datetime

import pandas as pd

from profiler import BaseProfiler


class DemoDemographicProfiler(BaseProfiler):
    """Clean demographic CSV files."""

    def clean_data(self) -> None:
        df = self.data
        assert df is not None

        # Keep only the relevant columns
        columns_to_keep = ["ehealth_id", "sex", "age", "occupation_holder", "dob"]
        df = df[columns_to_keep]

        # Drop rows missing required values
        df = df.dropna(subset=columns_to_keep)

        # Normalise columns
        df["sex"] = df["sex"].astype(str).str.upper()
        current_year = datetime.now().year
        df["dob"] = (current_year - df["age"].astype(int)).astype(str) + "-01-01"

        self.data = df

