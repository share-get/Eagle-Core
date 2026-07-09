"""
reports.py

Reporting utilities for Eagle
"""

from pathlib import Path
import pandas as pd

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def save_metrics(metrics):
    """
    Save metrics to CSV.
    """

    data = {
        "Metric": [
            "Total Return",
            "CAGR",
            "Annual Volatility",
            "Sharpe Ratio",
            "Maximum Drawdown",
        ],
        "Value": [
            f"{metrics.total_return:.2%}",
            f"{metrics.cagr:.2%}",
            f"{metrics.annual_volatility:.2%}",
            f"{metrics.sharpe_ratio:.2f}",
            f"{metrics.max_drawdown:.2%}",
        ],
    }

    df = pd.DataFrame(data)

    output = REPORT_DIR / "metrics.csv"

    df.to_csv(output, index=False)

    return output


def save_summary(metrics):
    """
    Save a human-readable summary.
    """

    output = REPORT_DIR / "summary.txt"

    with open(output, "w", encoding="utf-8") as f:

        f.write("=" * 50 + "\n")
        f.write("Eagle Backtest Report\n")
        f.write("=" * 50 + "\n\n")

        f.write(f"Total Return      : {metrics.total_return:.2%}\n")
        f.write(f"CAGR              : {metrics.cagr:.2%}\n")
        f.write(f"Annual Volatility : {metrics.annual_volatility:.2%}\n")
        f.write(f"Sharpe Ratio      : {metrics.sharpe_ratio:.2f}\n")
        f.write(f"Max Drawdown      : {metrics.max_drawdown:.2%}\n")

    return output
