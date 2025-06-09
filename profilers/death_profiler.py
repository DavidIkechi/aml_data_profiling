from profiler import BaseProfiler

class DeathProfiler(BaseProfiler):
    def clean_data(self):
        df = self.data

        # Keep only rows where censor_status_death == 'dead'
        df = df[df["censor_status_death"].astype(str).str.lower() == "dead"]

        # Rename patient_id to ehealth_id
        df = df.rename(columns={"patient_id": "ehealth_id"})

        # Replace 'PT' with 'EHH' in ehealth_id
        df["ehealth_id"] = df["ehealth_id"].astype(str).str.replace("PT", "EHH", regex=False)

        self.data = df