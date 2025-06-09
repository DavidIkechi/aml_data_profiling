# AML Data Profiling

This repository contains a small collection of **profilers** used to clean and
standardise CSV files generated from clinical research data. Each profiler
focuses on a single domain (demographics, death, diagnosis and treatment) and
produces a cleaned CSV ready for analysis.

## Installation

1. Create a Python environment (virtualenv or conda).
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

The application is driven by environment variables. The most common ones are:

| Variable | Default | Description |
|----------|---------|-------------|
| `CSV_FOLDER_PATH` | `data/csv` | Directory where raw CSV files are located |
| `OUTPUT_FOLDER_PATH` | `data/output` | Directory to write cleaned files |
| `FILE_NAME` | – | Name of the CSV file to process |
| `PROFILE` | `demo_demographic` | Which profiler to use (`demo_demographic`, `death`, `diagnosis`, or `treatment`) |

Set the variables and run:

```bash
python main.py
```

## Extending

To add a new profiler create a subclass of `BaseProfiler` in the `profilers`
package and implement the `clean_data` method. The base class handles loading
and saving the file so you only need to focus on cleaning logic.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE)
file for details.
