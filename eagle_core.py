"""
Eagle Core
EM1

Minimal Stable System

Only one goal:

Download market data correctly.
"""

from __future__ import annotations

import pandas as pd
import yfinance as yf


REQUIRED_COLUMNS = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
]


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize yfinance output.

    Compatible with:

    Old yfinance

    New MultiIndex yfinance
    """

    data = df.copy()

    if isinstance(data.columns, pd.MultiIndex):

        if "Price" in data.columns.names:

            data.columns = data.columns.get_level_values("Price")

        else:

            data.columns = data.columns.get_level_values(0)

    return data


def _validate(df: pd.DataFrame):

    missing = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing:

        raise ValueError(
            f"Missing columns: {missing}"
        )

    if not isinstance(
        df.index,
        pd.DatetimeIndex,
    ):

        raise ValueError(
            "Index must be DatetimeIndex"
        )

    if df.empty:

        raise ValueError(
            "Empty dataframe."
        )


def download_market_data(
    symbol: str,
    start: str,
    end: str,
) -> pd.DataFrame:

    raw = yf.download(
        symbol,
        start=start,
        end=end,
        progress=False,
        auto_adjust=False,
    )

    data = _normalize_columns(raw)

    data = data[
        [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
        ]
    ].copy()

    data.columns.name = None

    data.index.name = "Date"

    _validate(data)

    return data
