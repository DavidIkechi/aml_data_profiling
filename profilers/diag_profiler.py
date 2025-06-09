from profiler import BaseProfiler

class DiagnosisProfiler(BaseProfiler):
    def clean_data(self):
        df = self.data
        # Remove 'M-' prefix from morphology_code
        df["morphology_code_dx"] = df["morphology_code_dx"].astype(str).str.replace("M-", "", regex=False)
        # Map sample_source values to standardized codes
        source_mapping = {
            "bone marrow biopsy": "287550000",
            "flow cytometry": "64444005",
            "lymph node biopsy": "396487001"
        }
        df["sample_source"] = df["method_dx"].map(lambda x: source_mapping.get(x.lower(), x) if isinstance(x, str) else x)

        self.data = df