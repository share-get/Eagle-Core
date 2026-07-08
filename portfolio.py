"""
Project Eagle
Portfolio Engine v1

Support multi-asset portfolio returns.

Current Version:
- Static allocation
- Daily rebalancing
- Unlimited assets

Future:
- Cash
- Transaction Cost
- Rebalance Frequency
"""

from __future__ import annotations

import pandas as pd


class Portfolio:
    """
    Portfolio Engine

    Parameters
    ----------
    prices : dict[str, pd.Series]

        Example

        {
            "VOO": voo_close,
            "QQQM": qqqm_close,
        }

    weights : dict[str, float]

        Example

        {
            "VOO": 0.7,
            "QQQM": 0.3,
        }
    """

    def __init__(self, prices, weights):

        self.prices = prices
        self.weights = weights

        self._validate()

    def _validate(self):

        if len(self.prices) == 0:
            raise ValueError("No assets supplied.")

        if set(self.prices.keys()) != set(self.weights.keys()):
            raise ValueError(
                "Price assets and weight assets do not match."
            )

        total = sum(self.weights.values())

        if abs(total - 1.0) > 1e-8:
            raise ValueError(
                "Portfolio weights must sum to 1."
            )

    def price_frame(self):

        frame = pd.DataFrame(self.prices)

        frame = frame.dropna()

        return frame

    def return_frame(self):

        returns = self.price_frame().pct_change()

        returns = returns.fillna(0)

        return returns

    def portfolio_return(self):

        returns = self.return_frame()

        w = pd.Series(self.weights)

        portfolio = returns.mul(w, axis=1).sum(axis=1)

        return portfolio

    def equity_curve(
        self,
        initial_value=1.0,
    ):

        r = self.portfolio_return()

        equity = (1 + r).cumprod()

        equity *= initial_value

        return equity
