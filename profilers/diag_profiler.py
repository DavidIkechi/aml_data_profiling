"""Profiler for diagnosis related fields."""

from profiler import BaseProfiler


class DiagnosisProfiler(BaseProfiler):
    """Clean diagnosis CSV files."""

    def clean_data(self) -> None:
        df = self.data
        assert df is not None

        # Remove the "M-" prefix from morphology codes
        df["morphology_code_dx"] = df["morphology_code_dx"].astype(str).str.replace("M-", "", regex=False)

        # Standardise sample_source values
        source_mapping = {
            "bone marrow biopsy": "287550000",
            "flow cytometry": "64444005",
            "lymph node biopsy": "396487001",
        }
        df["sample_source"] = df["method_dx"].map(
            lambda x: source_mapping.get(x.lower(), x) if isinstance(x, str) else x
        )

        self.data = df

