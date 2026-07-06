"""
backtest.py

Benchmark Engine (EM1)

Current:

- Buy & Hold
"""

from dataclasses import dataclass

import pandas as pd


@dataclass
class BacktestResult:
    equity: pd.DataFrame
    total_return: float
    cagr: float
    max_drawdown: float


def buy_and_hold(df: pd.DataFrame) -> BacktestResult:
    """
    Buy on the first trading day and hold.
    """

    equity = pd.DataFrame(index=df.index)

    equity["Close"] = df["Close"]

    equity["Return"] = (
        equity["Close"]
        .pct_change()
        .fillna(0)
    )

    equity["Equity"] = (
        1 + equity["Return"]
    ).cumprod()

    equity["Peak"] = (
        equity["Equity"]
        .cummax()
    )

    equity["Drawdown"] = (
        equity["Equity"]
        / equity["Peak"]
        - 1
    )

    total_return = (
        equity["Equity"].iloc[-1]
        - 1
    )

    years = (
        (df.index[-1] - df.index[0]).days
        / 365.25
    )

    cagr = (
        equity["Equity"].iloc[-1]
        ** (1 / years)
        - 1
    )

    max_drawdown = (
        equity["Drawdown"].min()
    )

    return BacktestResult(
        equity=equity,
        total_return=float(total_return),
        cagr=float(cagr),
        max_drawdown=float(max_drawdown),
    )
