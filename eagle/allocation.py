"""
Project Eagle

Allocation Model
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Allocation:
    """
    Portfolio allocation.

    Example
    -------
    Allocation(
        voo=0.70,
        qqqm=0.30,
    )
    """

    voo: float
    qqqm: float

    def __post_init__(self):

        total = self.voo + self.qqqm

        if abs(total - 1.0) > 1e-8:
            raise ValueError(
                "Allocation must sum to 1.0"
            )

        if self.voo < 0:
            raise ValueError("VOO weight cannot be negative.")

        if self.qqqm < 0:
            raise ValueError("QQQM weight cannot be negative.")

    def to_dict(self):

        return {
            "VOO": self.voo,
            "QQQM": self.qqqm,
        }

    @property
    def voo_weight(self):

        return self.voo

    @property
    def qqqm_weight(self):

        return self.qqqm

    def __str__(self):

        return (
            f"VOO {self.voo:.0%} | "
            f"QQQM {self.qqqm:.0%}"
        )
