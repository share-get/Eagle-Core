"""
Project Eagle

Backtest Engine
"""

from dataclasses import dataclass
import numpy as np
import pandas as pd

from portfolio import Portfolio


@dataclass
class BacktestResult:

    equity: pd.Series

    returns: pd.Series

    total_return: float

    cagr: float

    volatility: float

    sharpe: float

    max_drawdown: float


def _calculate_metrics(
    equity: pd.Series,
    returns: pd.Series,
) -> BacktestResult:

    total_return = equity.iloc[-1] / equity.iloc[0] - 1

    years = len(equity) / 252

    cagr = (equity.iloc[-1] / equity.iloc[0]) ** (1 / years) - 1

    volatility = returns.std() * np.sqrt(252)

    if volatility == 0:
        sharpe = 0
    else:
        sharpe = cagr / volatility

    running_max = equity.cummax()

    drawdown = equity / running_max - 1

    max_drawdown = drawdown.min()

    return BacktestResult(
        equity=equity,
        returns=returns,
        total_return=total_return,
        cagr=cagr,
        volatility=volatility,
        sharpe=sharpe,
        max_drawdown=max_drawdown,
    )


def buy_and_hold(price: pd.DataFrame) -> BacktestResult:
    """
    Legacy API

    Keep compatibility with current project.
    """

    prices = {
        "SPY": price["Close"]
    }

    weights = {
        "SPY": 1.0
    }

    return portfolio_backtest(
        prices,
        weights,
    )


def portfolio_backtest(
    prices: dict,
    weights: dict,
) -> BacktestResult:
    """
    Multi Asset Backtest
    """

    portfolio = Portfolio(weights)

    returns = portfolio.daily_returns(prices)

    equity = portfolio.equity_curve(prices)

    return _calculate_metrics(
        equity,
        returns,
    )
