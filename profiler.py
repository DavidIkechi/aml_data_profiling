"""Base class and helpers for CSV profiling."""

import os
from abc import ABC, abstractmethod
from typing import Optional

import pandas as pd


class BaseProfiler(ABC):
    """Common functionality for profilers working with CSV files."""

    def __init__(self, input_dir: str, output_dir: str, filename: str) -> None:
        """Store input and output paths for the profiling run."""
        self.input_path = os.path.join(input_dir, filename)
        self.output_path = os.path.join(output_dir, filename)
        self.data: Optional[pd.DataFrame] = None

    def load_data(self) -> None:
        """Read the CSV file into ``self.data`` using string types."""
        self.data = pd.read_csv(self.input_path, dtype=str, low_memory=False)

    @abstractmethod
    def clean_data(self) -> None:
        """Implement data cleaning logic in subclasses."""

    def save_data(self) -> None:
        """Write ``self.data`` to ``self.output_path``."""
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        if self.data is not None:
            self.data.to_csv(self.output_path, index=False)

    def process(self) -> None:
        """Run the standard profiling workflow."""
        self.load_data()
        self.clean_data()
        self.save_data()

