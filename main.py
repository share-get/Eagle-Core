"""
Project Eagle

Main Entry
"""

from eagle_core import download_market_data
from backtest import portfolio_backtest
from reports import generate_reports


def main():

    print("=" * 60)
    print("Project Eagle v0.3")
    print("=" * 60)

    print("\nDownloading VOO...")

    voo = download_market_data(
        "VOO",
        start="2011-01-01",
        end="2025-01-01",
    )

    print("Downloading QQQM...")

    qqqm = download_market_data(
        "QQQM",
        start="2020-10-13",   # QQQM inception
        end="2025-01-01",
    )

    prices = {
        "VOO": voo["Close"],
        "QQQM": qqqm["Close"],
    }

    weights = {
        "VOO": 0.70,
        "QQQM": 0.30,
    }

    result = portfolio_backtest(
        prices=prices,
        weights=weights,
    )

    print("\n==========================")
    print("Portfolio")
    print("==========================")

    print(f"VOO : {weights['VOO']:.0%}")
    print(f"QQQM: {weights['QQQM']:.0%}")

    print("\n==========================")
    print("Performance")
    print("==========================")

    print(f"Total Return      : {result.total_return:.2%}")
    print(f"CAGR              : {result.cagr:.2%}")
    print(f"Annual Volatility : {result.volatility:.2%}")
    print(f"Sharpe Ratio      : {result.sharpe:.2f}")
    print(f"Max Drawdown      : {result.max_drawdown:.2%}")

    generate_reports(result)

    print("\nReports Generated.")
    print("\nDone.")


if __name__ == "__main__":
    main()
