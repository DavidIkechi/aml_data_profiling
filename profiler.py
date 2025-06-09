import os
import pandas as pd
from abc import ABC, abstractmethod

class BaseProfiler(ABC):
    """
    This class defines the structure for profiling data, including loading,
    cleaning, and saving data.
    """
    def __init__(self, input_dir: str, output_dir: str, filename: str):
        self.input_path = os.path.join(input_dir, filename)
        self.output_path = os.path.join(output_dir, filename)
        print(f"Input Path: {self.input_path}")
        self.data = None

    def load_data(self):
        """
        This method reads a CSV file into a pandas DataFrame.
        """
        self.data = pd.read_csv(self.input_path)

    @abstractmethod
    def clean_data(self):
        """
        This method should be implemented to clean the data.
        """
        pass

    def save_data(self):
        """
        This method saves the cleaned DataFrame to a CSV file.
        """
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        self.data.to_csv(self.output_path, index=False)

    def process(self):
        """
        This method orchestrates the data profiling process by calling
        load_data, clean_data, and save_data in sequence.
        """
        self.load_data()
        self.clean_data()
        self.save_data()