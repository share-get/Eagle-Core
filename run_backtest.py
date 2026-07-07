"""
Eagle EM1 Demo

Run:
python demo.py
"""

from eagle_core import download_market_data
from backtest import buy_and_hold
from metrics import calculate_metrics
from plotting import plot_equity_curve
from reports import save_metrics, save_summary


def main():

    print("=" * 60)
    print("Eagle EM1")
    print("=" * 60)

    print("\nDownloading SPY...")

    spy = download_market_data(
        symbol="SPY",
        start="2007-01-01",
        end="2025-01-01",
    )

    print("✓ Download Successful\n")

    print(f"Rows: {len(spy)}")
    print(f"Columns: {list(spy.columns)}")

    print("\nFirst Five Rows:\n")
    print(spy.head())

    print("\nLast Five Rows:\n")
    print(spy.tail())

    print("\nSummary:\n")
    print(spy.describe())

    print("\nValidation Passed.")

    # ==========================
    # Backtest
    # ==========================

    result = buy_and_hold(spy)

    metrics = calculate_metrics(result.equity)

    chart = plot_equity_curve(result)
    metrics_file = save_metrics(metrics)
    summary_file = save_summary(metrics)

    print("\n")
    print("=" * 60)
    print("BUY & HOLD BENCHMARK")
    print("=" * 60)

    print(f"Total Return      : {metrics.total_return:.2%}")
    print(f"CAGR              : {metrics.cagr:.2%}")
    print(f"Annual Volatility : {metrics.annual_volatility:.2%}")
    print(f"Sharpe Ratio      : {metrics.sharpe_ratio:.2f}")
    print(f"Max Drawdown      : {metrics.max_drawdown:.2%}")

    print("\nGenerated Reports")
    print("-" * 60)
    print(f"Chart   : {chart}")
    print(f"Metrics : {metrics_file}")
    print(f"Summary : {summary_file}")

    print("\nDone.")


if __name__ == "__main__":
    main()
