"""
Project Eagle

Unit Tests for Eagle Strategy
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from allocation import Allocation
from strategy import EagleStrategy


def test_default_strategy():

    strategy = EagleStrategy()

    assert strategy.allocate(0.00) == Allocation(0.70, 0.30)

    assert strategy.allocate(0.03) == Allocation(0.70, 0.30)

    assert strategy.allocate(0.05) == Allocation(0.70, 0.30)

    assert strategy.allocate(0.08) == Allocation(0.70, 0.30)

    assert strategy.allocate(0.10) == Allocation(0.60, 0.40)

    assert strategy.allocate(0.15) == Allocation(0.60, 0.40)


def test_custom_strategy():

    strategy = EagleStrategy(
        entry_threshold=0.04,
        deep_threshold=0.08,
        normal=Allocation(0.80, 0.20),
        deep=Allocation(0.50, 0.50),
    )

    assert strategy.allocate(0.02) == Allocation(0.80, 0.20)

    assert strategy.allocate(0.07) == Allocation(0.80, 0.20)

    assert strategy.allocate(0.09) == Allocation(0.50, 0.50)


def test_negative_drawdown():

    strategy = EagleStrategy()

    try:

        strategy.allocate(-0.01)

        assert False

    except ValueError:

        pass


if __name__ == "__main__":

    test_default_strategy()

    test_custom_strategy()

    test_negative_drawdown()

    print("All Strategy Tests Passed.")
