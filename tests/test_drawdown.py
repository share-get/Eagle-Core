import pandas as pd

from eagle.drawdown import DrawdownEngine


close = pd.Series(

    [

        100,

        105,

        110,

        108,

        102,

        98,

        95,

    ]

)

engine = DrawdownEngine()

state = engine.evaluate(close)

print(state)

assert state.peak_price == 110

assert round(state.drawdown, 4) == 0.1364

assert state.duration == 4

print("Drawdown Test Passed.")
