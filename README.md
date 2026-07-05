# FIFA World Cup 2026: Data Cleaning and Exploration

Week 1 assignment for the VortexTech AI/ML track. This project takes a raw, slightly messy dataset and prepares it for analysis using Python and Pandas.

## Dataset

**FIFA World Cup 2026** from [Kaggle](https://www.kaggle.com/datasets/mominullptr/fifa-world-cup-2026-dataset) (CC0 license).

- 1,248 players across all 48 participating nations
- 3 CSV files: player registrations, tournament statistics, and team info
- Downloaded directly from GitHub in the notebook (no API key needed)

## What This Project Does

1. Loads raw CSV data from GitHub
2. Identifies missing values, duplicates, and incorrect data types
3. Cleans the dataset (fills missing values, removes duplicates, converts types)
4. Merges player bio and performance data into a unified DataFrame
5. Produces summary statistics (mean, median, value counts)
6. Creates 2 visualizations (histogram of market values, bar chart of team averages)

## Files

| File | Description |
|------|-------------|
| `fifa_wc_2026_data_cleaning.ipynb` | Main Jupyter notebook with all analysis |
| `generate_notebook.py` | Script that generated the notebook (stdlib only) |
| `venv/` | Python virtual environment |

## How to Run

1. Clone this repository
2. Create and activate the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn
   ```
4. Launch Jupyter:
   ```bash
   jupyter notebook fifa_wc_2026_data_cleaning.ipynb
   ```
5. Run all cells (Kernel > Restart & Run All)

## Requirements

- Python 3.10+
- pandas
- matplotlib
- seaborn
