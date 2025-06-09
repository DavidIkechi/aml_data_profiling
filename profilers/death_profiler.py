"""Profiler that filters patients confirmed dead."""

import pandas as pd

from profiler import BaseProfiler


class DeathProfiler(BaseProfiler):
    """Select only records for deceased patients."""

    def clean_data(self) -> None:
        df = self.data
        assert df is not None

        # Filter for rows marked as dead
        df = df[df["censor_status_death"].astype(str).str.lower() == "dead"]

        # Standardise patient identifier
        df = df.rename(columns={"patient_id": "ehealth_id"})
        df["ehealth_id"] = df["ehealth_id"].astype(str).str.replace("PT", "EHH", regex=False)

        self.data = df

