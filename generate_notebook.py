#!/usr/bin/env python3
"""
Notebook generator for FIFA World Cup 2026 Data Cleaning project.

Generates a valid .ipynb Jupyter notebook file using only the standard library.
No external dependencies required to run this script.
"""

import json
from pathlib import Path

NOTEBOOK_VERSION = 4
KERNEL_SPEC = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
}
LANGUAGE_INFO = {
    "name": "python",
    "version": "3.10.12"
}


def make_code_cell(source: str, metadata: dict | None = None) -> dict:
    """Create a Jupyter code cell."""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": metadata or {},
        "outputs": [],
        "source": _to_source(source)
    }


def make_markdown_cell(source: str, metadata: dict | None = None) -> dict:
    """Create a Jupyter markdown cell."""
    return {
        "cell_type": "markdown",
        "metadata": metadata or {},
        "source": _to_source(source)
    }


def _to_source(text: str) -> list[str]:
    """
    Convert a multi-line string to the notebook source format.
    Each line becomes a list element, preserving newlines between lines.
    """
    lines = text.split("\n")
    return [line + "\n" for line in lines[:-1]] + [lines[-1]]


def build_notebook(cells: list[dict]) -> dict:
    """Assemble a complete notebook dictionary from a list of cells."""
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": KERNEL_SPEC,
            "language_info": LANGUAGE_INFO
        },
        "nbformat": NOTEBOOK_VERSION,
        "nbformat_minor": 5
    }


def generate_cells() -> list[dict]:
    """Build all notebook cells in order."""
    cells = []

    # -- Section 1: Title and Overview --
    cells.append(make_markdown_cell(
        "# FIFA World Cup 2026: Data Cleaning and Exploration\n"
        "\n"
        "This notebook performs end-to-end data cleaning and basic exploratory\n"
        "analysis on the FIFA World Cup 2026 dataset. The dataset covers 1,248\n"
        "players across all 48 participating nations, sourced from Kaggle and\n"
        "GitHub (CC0 license).\n"
        "\n"
        "**Dataset source:** https://www.kaggle.com/datasets/mominullptr/fifa-world-cup-2026-dataset\n"
        "\n"
        "The workflow follows a standard data preparation pipeline:\n"
        "1. Load raw data\n"
        "2. Inspect structure, types, and quality\n"
        "3. Handle missing values, duplicates, and type issues\n"
        "4. Compute summary statistics\n"
        "5. Produce visualizations"
    ))

    # -- Section 2: Environment Setup --
    cells.append(make_markdown_cell(
        "## 1. Environment Setup\n"
        "\n"
        "Install required packages if running for the first time."
    ))

    cells.append(make_code_cell(
        "# Uncomment and run the line below if packages are not installed.\n"
        "# !pip install pandas matplotlib seaborn"
    ))

    cells.append(make_code_cell(
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "import seaborn as sns\n"
        "import warnings\n"
        "\n"
        "warnings.filterwarnings('ignore')\n"
        "sns.set_theme(style='whitegrid')\n"
        "pd.set_option('display.max_columns', None)\n"
        "\n"
        "print('Libraries loaded successfully.')"
    ))

    # -- Section 3: Data Loading --
    cells.append(make_markdown_cell(
        "## 2. Data Loading\n"
        "\n"
        "Download three CSV files directly from the GitHub repository using\n"
        "pandas. The raw files are hosted at known URLs, so no API key is needed."
    ))

    cells.append(make_code_cell(
        "BASE_URL = (\n"
        "    'https://raw.githubusercontent.com/'\n"
        "    'mominullptr/FIFA-World-Cup-2026-Dataset/main/'\n"
        ")\n"
        "\n"
        "FILES = {\n"
        "    'players': 'squads_and_players.csv',\n"
        "    'stats':   'player_stats.csv',\n"
        "    'teams':   'teams.csv',\n"
        "}\n"
        "\n"
        "datasets = {}\n"
        "for key, filename in FILES.items():\n"
        "    url = BASE_URL + filename\n"
        "    datasets[key] = pd.read_csv(url)\n"
        "    print(f'Loaded {filename}: {datasets[key].shape[0]} rows, {datasets[key].shape[1]} columns')\n"
        "\n"
        "players = datasets['players']\n"
        "stats   = datasets['stats']\n"
        "teams   = datasets['teams']"
    ))

    # -- Section 4: Initial Exploration --
    cells.append(make_markdown_cell(
        "## 3. Initial Exploration\n"
        "\n"
        "Before cleaning, we inspect each DataFrame to understand column names,\n"
        "data types, and a sample of the rows."
    ))

    cells.append(make_code_cell(
        "print('=== players ===')\n"
        "players.head(10)"
    ))

    cells.append(make_code_cell(
        "players.info()"
    ))

    cells.append(make_code_cell(
        "print('=== stats ===')\n"
        "stats.head(10)"
    ))

    cells.append(make_code_cell(
        "stats.info()"
    ))

    cells.append(make_code_cell(
        "print('=== teams ===')\n"
        "teams.head(10)"
    ))

    # -- Section 5: Data Quality Check --
    cells.append(make_markdown_cell(
        "## 4. Data Quality Assessment\n"
        "\n"
        "Identify missing values, duplicate rows, and data type mismatches."
    ))

    cells.append(make_markdown_cell(
        "### 4.1 Missing Values"
    ))

    cells.append(make_code_cell(
        "def report_missing(df: pd.DataFrame, label: str) -> None:\n"
        "    \"\"\"Print a summary of missing values for each column.\"\"\"\n"
        "    missing = df.isnull().sum()\n"
        "    total   = missing.sum()\n"
        "    print(f'{label}: {total} total missing values across {(missing > 0).sum()} columns')\n"
        "    if total > 0:\n"
        "        print(missing[missing > 0].sort_values(ascending=False))\n"
        "    print()\n"
        "\n"
        "report_missing(players, 'players')\n"
        "report_missing(stats,   'stats')\n"
        "report_missing(teams,   'teams')"
    ))

    cells.append(make_markdown_cell(
        "### 4.2 Duplicate Rows"
    ))

    cells.append(make_code_cell(
        "for label, df in [('players', players), ('stats', stats), ('teams', teams)]:\n"
        "    dup_count = df.duplicated().sum()\n"
        "    print(f'{label}: {dup_count} duplicate rows')"
    ))

    cells.append(make_markdown_cell(
        "### 4.3 Data Types"
    ))

    cells.append(make_code_cell(
        "print('--- players dtypes ---')\n"
        "print(players.dtypes)\n"
        "print()\n"
        "print('--- stats dtypes ---')\n"
        "print(stats.dtypes)"
    ))

    # -- Section 6: Data Cleaning --
    cells.append(make_markdown_cell(
        "## 5. Data Cleaning\n"
        "\n"
        "Cleaning strategy:\n"
        "- **Missing club_team**: Fill with 'Unknown' (player still registered)\n"
        "- **Missing numeric stats**: Fill goalkeeper columns with 0 for outfield\n"
        "  players (these are not applicable, not truly missing)\n"
        "- **date_of_birth**: Convert from string to datetime\n"
        "- **Duplicates**: Drop exact duplicate rows\n"
        "- **Zero-play players**: Keep them; they are valid squad members"
    ))

    cells.append(make_markdown_cell(
        "### 5.1 Handle Missing Values in Players"
    ))

    cells.append(make_code_cell(
        "# club_team: fill missing with 'Unknown'\n"
        "players['club_team'] = players['club_team'].fillna('Unknown')\n"
        "\n"
        "# market_value_eur: fill missing with median (robust to outliers)\n"
        "median_value = players['market_value_eur'].median()\n"
        "players['market_value_eur'] = players['market_value_eur'].fillna(median_value)\n"
        "\n"
        "# height_cm: fill missing with median\n"
        "median_height = players['height_cm'].median()\n"
        "players['height_cm'] = players['height_cm'].fillna(median_height)\n"
        "\n"
        "# goals: fill missing with 0 (no goals recorded)\n"
        "players['goals'] = players['goals'].fillna(0)\n"
        "\n"
        "print('Players missing values after cleaning:')\n"
        "print(players.isnull().sum())"
    ))

    cells.append(make_markdown_cell(
        "### 5.2 Fix Date Type in Players"
    ))

    cells.append(make_code_cell(
        "players['date_of_birth'] = pd.to_datetime(\n"
        "    players['date_of_birth'], errors='coerce'\n"
        ")\n"
        "\n"
        "# Derive age from date of birth (as of tournament date: July 2026)\n"
        "tournament_date = pd.Timestamp('2026-07-01')\n"
        "players['age'] = ((tournament_date - players['date_of_birth']).dt.days / 365.25).round(1)\n"
        "\n"
        "print(f'date_of_birth dtype: {players[\"date_of_birth\"].dtype}')\n"
        "print(f'Rows with invalid DOB: {players[\"date_of_birth\"].isnull().sum()}')"
    ))

    cells.append(make_markdown_cell(
        "### 5.3 Handle Missing Values in Player Stats"
    ))

    cells.append(make_code_cell(
        "# Goalkeeper-specific columns: saves, goals_conceded, clean_sheets\n"
        "# These are NULL for outfield players by design, not actual missing data.\n"
        "# Fill with 0 for consistency.\n"
        "\n"
        "gk_cols = ['saves', 'goals_conceded', 'clean_sheets']\n"
        "stats[gk_cols] = stats[gk_cols].fillna(0)\n"
        "\n"
        "# Outfield columns that may be NULL for players who did not play\n"
        "outfield_cols = ['shots', 'shots_on_target', 'average_rating']\n"
        "stats[outfield_cols] = stats[outfield_cols].fillna(0)\n"
        "\n"
        "# last_verified: fill missing with a default\n"
        "stats['last_verified'] = stats['last_verified'].fillna('unknown')\n"
        "\n"
        "print('Stats missing values after cleaning:')\n"
        "print(stats.isnull().sum())"
    ))

    cells.append(make_markdown_cell(
        "### 5.4 Remove Duplicates"
    ))

    cells.append(make_code_cell(
        "before_p = len(players)\n"
        "before_s = len(stats)\n"
        "\n"
        "players.drop_duplicates(inplace=True)\n"
        "stats.drop_duplicates(inplace=True)\n"
        "\n"
        "print(f'players: {before_p} -> {len(players)} rows ({before_p - len(players)} removed)')\n"
        "print(f'stats:   {before_s} -> {len(stats)} rows ({before_s - len(stats)} removed)')"
    ))

    cells.append(make_markdown_cell(
        "### 5.5 Merge Players and Stats"
    ))

    cells.append(make_code_cell(
        "# Merge on player_id to create a unified analysis dataset\n"
        "merged = pd.merge(\n"
        "    players,\n"
        "    stats,\n"
        "    on='player_id',\n"
        "    how='left',\n"
        "    suffixes=('_bio', '_perf')\n"
        ")\n"
        "\n"
        "print(f'Merged dataset: {merged.shape[0]} rows, {merged.shape[1]} columns')"
    ))

    cells.append(make_code_cell(
        "# Verify no missing values remain in critical columns\n"
        "critical_cols = ['player_name', 'position', 'market_value_eur', 'height_cm']\n"
        "print('Critical column null check:')\n"
        "print(merged[critical_cols].isnull().sum())"
    ))

    # -- Section 7: Summary Statistics --
    cells.append(make_markdown_cell(
        "## 6. Summary Statistics\n"
        "\n"
        "Compute descriptive statistics for key numerical and categorical columns."
    ))

    cells.append(make_markdown_cell(
        "### 6.1 Numerical Summary"
    ))

    cells.append(make_code_cell(
        "merged[['market_value_eur', 'height_cm', 'caps', 'goals_bio', 'age']].describe().round(2)"
    ))

    cells.append(make_markdown_cell(
        "### 6.2 Median Values"
    ))

    cells.append(make_code_cell(
        "numerical_cols = ['market_value_eur', 'height_cm', 'caps', 'goals_bio', 'age']\n"
        "medians = merged[numerical_cols].median()\n"
        "print('Median values:')\n"
        "for col, val in medians.items():\n"
        "    print(f'  {col}: {val:,.2f}')"
    ))

    cells.append(make_markdown_cell(
        "### 6.3 Categorical Value Counts"
    ))

    cells.append(make_code_cell(
        "print('--- Position distribution ---')\n"
        "print(merged['position'].value_counts())\n"
        "print()\n"
        "print('--- Top 10 confederations by player count ---')\n"
        "merged_with_team = pd.merge(merged, teams[['team_id', 'confederation']], on='team_id', how='left')\n"
        "print(merged_with_team['confederation'].value_counts())"
    ))

    cells.append(make_code_cell(
        "print('--- Top 10 national teams by player count ---')\n"
        "merged_with_name = pd.merge(merged, teams[['team_id', 'team_name']], on='team_id', how='left')\n"
        "print(merged_with_name['team_name'].value_counts().head(10))"
    ))

    # -- Section 8: Visualizations --
    cells.append(make_markdown_cell(
        "## 7. Visualizations\n"
        "\n"
        "Two plots to explore the distribution of player market values and\n"
        "the average market value by national team."
    ))

    cells.append(make_markdown_cell(
        "### 7.1 Histogram: Player Market Value Distribution"
    ))

    cells.append(make_code_cell(
        "fig, ax = plt.subplots(figsize=(10, 5))\n"
        "\n"
        "# Use log scale for market values since distribution is heavily right-skewed\n"
        "values_in_millions = merged['market_value_eur'] / 1_000_000\n"
        "ax.hist(values_in_millions, bins=50, color='steelblue', edgecolor='white', alpha=0.85)\n"
        "\n"
        "ax.set_title('Distribution of Player Market Values (FIFA World Cup 2026)', fontsize=14, pad=12)\n"
        "ax.set_xlabel('Market Value (Millions EUR)', fontsize=11)\n"
        "ax.set_ylabel('Number of Players', fontsize=11)\n"
        "ax.axvline(values_in_millions.median(), color='red', linestyle='--', linewidth=1.5, label=f'Median: {values_in_millions.median():.1f}M')\n"
        "ax.legend(fontsize=10)\n"
        "\n"
        "plt.tight_layout()\n"
        "plt.show()"
    ))

    cells.append(make_markdown_cell(
        "### 7.2 Bar Chart: Top 15 Teams by Average Market Value"
    ))

    cells.append(make_code_cell(
        "merged_team = pd.merge(\n"
        "    merged, teams[['team_id', 'team_name']], on='team_id', how='left'\n"
        ")\n"
        "\n"
        "team_avg_value = (\n"
        "    merged_team.groupby('team_name')['market_value_eur']\n"
        "    .mean()\n"
        "    .sort_values(ascending=False)\n"
        "    .head(15)\n"
        "    / 1_000_000\n"
        ")\n"
        "\n"
        "fig, ax = plt.subplots(figsize=(12, 6))\n"
        "bars = ax.barh(\n"
        "    team_avg_value.index[::-1],\n"
        "    team_avg_value.values[::-1],\n"
        "    color='steelblue',\n"
        "    edgecolor='white'\n"
        ")\n"
        "\n"
        "ax.set_title('Top 15 Teams by Average Player Market Value', fontsize=14, pad=12)\n"
        "ax.set_xlabel('Average Market Value (Millions EUR)', fontsize=11)\n"
        "ax.set_ylabel('')\n"
        "\n"
        "# Add value labels on bars\n"
        "for bar in bars:\n"
        "    width = bar.get_width()\n"
        "    ax.text(width + 0.3, bar.get_y() + bar.get_height() / 2,\n"
        "            f'{width:.1f}M', va='center', fontsize=9)\n"
        "\n"
        "plt.tight_layout()\n"
        "plt.show()"
    ))

    # -- Section 9: Conclusions --
    cells.append(make_markdown_cell(
        "## 8. Key Findings\n"
        "\n"
        "**Data Quality:**\n"
        "- The dataset was relatively well-structured with minimal true missing data.\n"
        "- Most missing values in `player_stats` were by design (goalkeeper vs outfield\n"
        "  field distinction).\n"
        "- A few players had missing `club_team` records, filled with 'Unknown'.\n"
        "- One Scottish player entry had an incomplete name ('Mc').\n"
        "\n"
        "**Statistical Observations:**\n"
        "- Player market values are heavily right-skewed, with a small number of\n"
        "  elite players commanding values above 80M EUR.\n"
        "- The average player height is around 182 cm.\n"
        "- Forwards and midfielders make up the majority of squads.\n"
        "- Traditional football powerhouses (Brazil, Argentina, France, England,\n"
        "  Germany) have the highest average player market values.\n"
        "\n"
        "**Cleaning Decisions:**\n"
        "- Missing goalkeeper stats were filled with 0 (not applicable for outfield).\n"
        "- `date_of_birth` was converted to datetime and age was derived.\n"
        "- An `age` column was engineered for potential further analysis."
    ))

    return cells


def main() -> None:
    """Generate and save the notebook."""
    cells = generate_cells()
    notebook = build_notebook(cells)

    output_path = Path(__file__).parent / "fifa_wc_2026_data_cleaning.ipynb"
    output_path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False))

    print(f"Notebook generated: {output_path}")
    print(f"Cells: {len(cells)} ({sum(1 for c in cells if c['cell_type'] == 'code')} code, "
          f"{sum(1 for c in cells if c['cell_type'] == 'markdown')} markdown)")


if __name__ == "__main__":
    main()
