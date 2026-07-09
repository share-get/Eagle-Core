"""
Project Eagle

Drawdown Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import pandas as pd


class DrawdownZone(Enum):

    NORMAL = "NORMAL"

    WATCH = "WATCH"

    ACCUMULATE = "ACCUMULATE"

    DEEP = "DEEP"


@dataclass(frozen=True)
class DrawdownState:

    peak_price: float

    current_price: float

    drawdown: float

    zone: DrawdownZone

    duration: int

    def __str__(self):

        return (
            f"Peak={self.peak_price:.2f} | "
            f"Current={self.current_price:.2f} | "
            f"Drawdown={self.drawdown:.2%} | "
            f"Zone={self.zone.value} | "
            f"Duration={self.duration}"
        )


class DrawdownEngine:

    """
    Drawdown Engine

    Zone Rules

    0~5%        NORMAL

    5~8%        WATCH

    8~12%       ACCUMULATE

    >12%        DEEP
    """

    def __init__(

        self,

        watch=0.05,

        accumulate=0.08,

        deep=0.12,

    ):

        self.watch = watch

        self.accumulate = accumulate

        self.deep = deep

    def zone(self, drawdown):

        if drawdown < self.watch:
            return DrawdownZone.NORMAL

        if drawdown < self.accumulate:
            return DrawdownZone.WATCH

        if drawdown < self.deep:
            return DrawdownZone.ACCUMULATE

        return DrawdownZone.DEEP

    def evaluate(self, close: pd.Series):

        peak = close.cummax()

        dd = (peak - close) / peak

        duration = []

        days = 0

        for x in dd:

            if x == 0:

                days = 0

            else:

                days += 1

            duration.append(days)

        latest_peak = float(peak.iloc[-1])

        latest_close = float(close.iloc[-1])

        latest_dd = float(dd.iloc[-1])

        latest_duration = int(duration[-1])

        return DrawdownState(

            peak_price=latest_peak,

            current_price=latest_close,

            drawdown=latest_dd,

            zone=self.zone(latest_dd),

            duration=latest_duration,

        )
