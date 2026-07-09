"""
Project Eagle

Portfolio Engine v1

Supports:
- Multiple assets
- Static allocation
- Daily rebalancing
"""

from eagle.__future__ import annotations

import pandas as pd


class Portfolio:

    def __init__(self, weights: dict[str, float]):

        total = sum(weights.values())

        if abs(total - 1.0) > 1e-8:
            raise ValueError("Portfolio weights must sum to 1.0")

        self.weights = weights

    def build(self, prices: dict[str, pd.Series]) -> pd.DataFrame:
        """
        Build aligned price DataFrame.
        """

        missing = set(self.weights) - set(prices)

        if missing:
            raise ValueError(f"Missing price series: {missing}")

        frame = pd.concat(prices, axis=1)

        frame = frame.dropna()

        return frame

    def daily_returns(
        self,
        prices: dict[str, pd.Series],
    ) -> pd.Series:

        frame = self.build(prices)

        returns = frame.pct_change().fillna(0)

        weights = pd.Series(self.weights)

        portfolio_return = returns.mul(weights, axis=1).sum(axis=1)

        portfolio_return.name = "Portfolio"

        return portfolio_return

    def equity_curve(
        self,
        prices: dict[str, pd.Series],
        initial_value: float = 1.0,
    ) -> pd.Series:

        r = self.daily_returns(prices)

        equity = (1 + r).cumprod()

        equity *= initial_value

        equity.name = "Equity"

        return equity
