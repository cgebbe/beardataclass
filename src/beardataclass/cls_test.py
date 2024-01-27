import dataclasses

import pandas as pd

from beardataclass.cls import BearDataClass


@dataclasses.dataclass
class Foo(BearDataClass):
    x: int
    y: str = dataclasses.field()
    z: float = 0.0


def test_cls():
    assert Foo.fields().x == "x"

    df = Foo.create_pandas_df([Foo(1, 2), Foo(3, 4)])
    expected = pd.DataFrame(
        {
            "x": [1, 3],
            "y": [2, 4],
            "z": [0.0, 0.0],
        },
    )
    pd.testing.assert_frame_equal(df, expected)

    recreated = Foo.from_row(df.iloc[0, :])
    assert recreated == Foo(1, 2)
