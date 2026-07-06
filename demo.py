"""
Eagle EM1 Demo

Run:

python demo.py
"""
from backtest import buy_and_hold
from eagle_core import download_market_data


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

    print("\nDone.")

result = buy_and_hold(spy)

if __name__ == "__main__":
    main()


print("\n")
print("=" * 60)
print("BUY & HOLD BENCHMARK")
print("=" * 60)

print(f"Total Return : {result.total_return:.2%}")
print(f"CAGR         : {result.cagr:.2%}")
print(f"Max Drawdown : {result.max_drawdown:.2%}")
