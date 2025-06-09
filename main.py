from profilers.demo_profiler import DemoDemographicProfiler
from profilers.death_profiler import DeathProfiler
from profilers.diag_profiler import DiagnosisProfiler
from profilers.treatment_profiler import TreatmentProfiler
# load the loadenv
from dotenv import load_dotenv
import os

load_dotenv()


# CLI handler
def main():

    csv_folder_path = os.getenv("CSV_FOLDER_PATH", "data/csv")
    output_folder_path = os.getenv("OUTPUT_FOLDER_PATH", "data/output")
    filename = os.getenv("FILE_NAME")
    profile = os.getenv("PROFILE", "demo_demographic")

    print(filename)
    profiler_map = {
        "demo_demographic": DemoDemographicProfiler,
        "death": DeathProfiler,
        "diagnosis": DiagnosisProfiler,
        "treatment": TreatmentProfiler
    }

    profiler_class = profiler_map.get(profile)
    profiler = profiler_class(csv_folder_path, output_folder_path, filename)
    profiler.process()

if __name__ == "__main__":
    main()