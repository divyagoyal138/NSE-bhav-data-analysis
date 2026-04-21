# Weekly Stock Report Generator

This project processes NSE bhav data (CSV files) for 5 trading days and generates a weekly stock report using Python and pandas.

## Features

* Filters only **EQ series stocks**
* Calculates:

  * Opening (Monday)
  * Closing (Friday)
  * Weekly High & Low
  * Weekly Average Price
* Computes **Fibonacci levels**
* Outputs a clean CSV report

## Requirements

* Python 3.x
* pandas

Install:

```
pip install pandas
```

## Usage

1. Place your 5 CSV files in the project folder.
2. Update file names in the script if needed.
3. Run:

```
python code.py
```

## Output

* `Weekly_Stock_Report.csv` containing all calculated fields.

## Notes

* Ensure all CSV files have the same structure.
* Data is filtered for `SERIES = EQ`.

---
