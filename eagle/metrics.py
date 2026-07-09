"""
metrics.py

Performance Metrics for Eagle EM1
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd

TRADING_DAYS = 252


@dataclass
class PerformanceMetrics:
    total_return: float
    cagr: float
    annual_volatility: float
    sharpe_ratio: float
    max_drawdown: float


def calculate_metrics(equity: pd.DataFrame) -> PerformanceMetrics:
    """
    Calculate performance metrics from an equity curve.
    """

    returns = equity["Return"]

    total_return = equity["Equity"].iloc[-1] - 1

    years = (equity.index[-1] - equity.index[0]).days / 365.25

    cagr = equity["Equity"].iloc[-1] ** (1 / years) - 1

    annual_volatility = returns.std() * np.sqrt(TRADING_DAYS)

    if annual_volatility > 0:
        sharpe = cagr / annual_volatility
    else:
        sharpe = 0.0

    max_drawdown = equity["Drawdown"].min()

    return PerformanceMetrics(
        total_return=float(total_return),
        cagr=float(cagr),
        annual_volatility=float(annual_volatility),
        sharpe_ratio=float(sharpe),
        max_drawdown=float(max_drawdown),
    )
