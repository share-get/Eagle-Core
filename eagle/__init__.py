"""
Project Eagle

Core Package
"""

__version__ = "0.3.0"

from .allocation import Allocation
from .strategy import EagleStrategy
from .portfolio import Portfolio
from .backtest import portfolio_backtest

__all__ = [
    "Allocation",
    "EagleStrategy",
    "Portfolio",
    "portfolio_backtest",
]
