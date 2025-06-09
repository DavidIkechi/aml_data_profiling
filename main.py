"""Entry point for running the data profilers."""

from dotenv import load_dotenv
import os

from profilers.demo_profiler import DemoDemographicProfiler
from profilers.death_profiler import DeathProfiler
from profilers.diag_profiler import DiagnosisProfiler
from profilers.treatment_profiler import TreatmentProfiler


load_dotenv()


def main() -> None:
    """Load configuration, select the profiler and run it."""

    csv_folder_path = os.getenv("CSV_FOLDER_PATH", "data/csv")
    output_folder_path = os.getenv("OUTPUT_FOLDER_PATH", "data/output")
    filename = os.getenv("FILE_NAME")
    profile = os.getenv("PROFILE", "demo_demographic")

    # Map profile names to their corresponding classes
    profiler_map = {
        "demo_demographic": DemoDemographicProfiler,
        "death": DeathProfiler,
        "diagnosis": DiagnosisProfiler,
        "treatment": TreatmentProfiler,
    }

    profiler_class = profiler_map.get(profile)
    if not profiler_class:
        raise ValueError(f"Unknown profile '{profile}'")

    profiler = profiler_class(csv_folder_path, output_folder_path, filename)
    profiler.process()


if __name__ == "__main__":
    main()
