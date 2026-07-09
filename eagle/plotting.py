"""
plotting.py

Plotting utilities for Eagle
"""

from pathlib import Path

import matplotlib.pyplot as plt


REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)


def plot_equity_curve(result):

    plt.figure(figsize=(12,6))

    plt.plot(
        result.equity.index,
        result.equity["Equity"],
        linewidth=2,
        label="Equity",
    )

    plt.title("Equity Curve")

    plt.xlabel("Date")

    plt.ylabel("Portfolio Value")

    plt.grid(True)

    plt.legend()

    output = REPORT_DIR / "equity_curve.png"

    plt.savefig(
        output,
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()

    return output
