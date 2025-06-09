from profiler import BaseProfiler

class TreatmentProfiler(BaseProfiler):
    def clean_data(self):
        df = self.data

        # Map drug_name_tx to standard codes
        drug_mapping = {
            "acalabrutinib": "1986808",
            "bendamustine": "134547",
            "chlorambucil": "2346",
            "fcr": "2937",
            "ibrutinib": "1442981",
            "idelalisib": "1544460",
            "obinutuzumab": "974779",
            "predinisolone": "OMOP880540",
            "rituximab": "121191",
            "venetoclax": "1747556",
            "zanubrutinib": "2262435"
        }
        df["drug_code_tx"] = df["drug_name_tx"].map(lambda x: drug_mapping.get(x.lower(), x) if isinstance(x, str) else x)

        # Map status_tx to standard codes in a new column
        status_mapping = {
            "active surveillance": "424313000",
            "palliative care": "103735009",
            "remission": "OMOP4997717",
            "treatment": "202111000000106",
            "under review": "721241000000109"
        }
        df["status_tx_code"] = df["status_tx"].map(lambda x: status_mapping.get(x.lower(), x) if isinstance(x, str) else x)

        self.data = df