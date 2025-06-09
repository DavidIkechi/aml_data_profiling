"""Profiler that maps treatment information to standard codes."""

from profiler import BaseProfiler


class TreatmentProfiler(BaseProfiler):
    """Clean treatment related CSV files."""

    def clean_data(self) -> None:
        df = self.data
        assert df is not None

        # Map raw drug names to standardised codes
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
            "zanubrutinib": "2262435",
        }
        df["drug_code_tx"] = df["drug_name_tx"].map(
            lambda x: drug_mapping.get(x.lower(), x) if isinstance(x, str) else x
        )

        # Map treatment status to standard codes
        status_mapping = {
            "active surveillance": "424313000",
            "palliative care": "103735009",
            "remission": "OMOP4997717",
            "treatment": "202111000000106",
            "under review": "721241000000109",
        }
        df["status_tx_code"] = df["status_tx"].map(
            lambda x: status_mapping.get(x.lower(), x) if isinstance(x, str) else x
        )

        self.data = df

