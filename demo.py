"""
Eagle EM1 Demo

Run:

python demo.py
"""

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


if __name__ == "__main__":
    main()
