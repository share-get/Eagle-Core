"""
Project Eagle

Eagle Allocation Strategy v1
"""

from eagle.allocation import Allocation


class EagleStrategy:
    """
    Eagle Allocation Strategy

    Rules
    -----
    Drawdown < entry_threshold
        -> Hold normal allocation

    entry_threshold <= Drawdown < deep_threshold
        -> Hold normal allocation

    Drawdown >= deep_threshold
        -> Hold deep allocation
    """

    def __init__(
        self,
        entry_threshold: float = 0.05,
        deep_threshold: float = 0.10,
        normal: Allocation | None = None,
        deep: Allocation | None = None,
    ):

        self.entry_threshold = entry_threshold
        self.deep_threshold = deep_threshold

        self.normal = normal or Allocation(
            voo=0.70,
            qqqm=0.30,
        )

        self.deep = deep or Allocation(
            voo=0.60,
            qqqm=0.40,
        )

    def allocate(
        self,
        drawdown: float,
    ) -> Allocation:
        """
        Parameters
        ----------
        drawdown

            Positive drawdown value.

            Example:

            0.08 = 8%
        """

        if drawdown < 0:
            raise ValueError("Drawdown cannot be negative.")

        if drawdown >= self.deep_threshold:
            return self.deep

        return self.normal

    def __str__(self):

        return (
            f"EagleStrategy("
            f"Entry={self.entry_threshold:.0%}, "
            f"Deep={self.deep_threshold:.0%})"
        )
