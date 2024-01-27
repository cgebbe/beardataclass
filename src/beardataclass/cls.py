import dataclasses
import pandas as pd
from typing import Iterable, TypeVar, Type

from typing import ClassVar, Dict, Protocol


# See https://stackoverflow.com/a/55240861/2135504
class IsDataclass(Protocol):
    __dataclass_fields__: ClassVar[Dict]


T = TypeVar("T", bound="BearDataClass")


@dataclasses.dataclass
class BearDataClass:
    @classmethod
    def fields(cls: Type[T]) -> T:
        # TODO: How to deal with init=False fields? we can exclude them, but then repr error...
        dct = {f.name: f.name for f in dataclasses.fields(cls)}
        return cls(**dct)

    @classmethod
    def create_pandas_df(cls: Type[T], items: Iterable[IsDataclass]) -> pd.DataFrame:
        return pd.DataFrame.from_records(
            data=(dataclasses.asdict(i) for i in items),
            columns=[f.name for f in dataclasses.fields(cls)],
        )

    @classmethod
    def from_row(cls: Type[T], row: pd.Series) -> T:
        return cls(**row)
