"""
Project Eagle

Main Entry
"""

from eagle_core import download_market_data
from backtest import buy_and_hold
from reports import generate_reports


def main():

    print("=" * 60)
    print("Project Eagle")
    print("=" * 60)

    print("\nDownloading SPY...")

    spy = download_market_data(
        symbol="SPY",
        start="2007-01-01",
        end="2025-01-01",
    )

    print("Done.")

    result = buy_and_hold(spy)

    print("\nBacktest Finished\n")

    print(f"Total Return      : {result.total_return:.2%}")
    print(f"CAGR              : {result.cagr:.2%}")
    print(f"Annual Volatility : {result.volatility:.2%}")
    print(f"Sharpe Ratio      : {result.sharpe:.2f}")
    print(f"Max Drawdown      : {result.max_drawdown:.2%}")

    generate_reports(result)

    print("\nReports Generated.")


if __name__ == "__main__":
    main()
