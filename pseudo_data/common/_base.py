from enum import StrEnum
from typing import Type

import numpy as np
from pydantic import BaseModel


class WeightedEnumGenerator(BaseModel):
    """
    Examples

    sample = WeightedEnumGenerator.from_str_list("sample", ["A", "B", "C"])
    list(sample.ordered_enum)
     - WeightedEnumGenerator(enum_name='sample', ordered_enum=<enum 'sample'>, weights=[0.54545, 0.27273, 0.18182])


    sample = WeightedEnumGenerator.from_tuples("sample", [("A", 7), ("B", 6),  ("C", 3)])
    - WeightedEnumGenerator(enum_name='sample', ordered_enum=<enum 'sample'>, weights=[0.4375, 0.375, 0.1875])
    """

    enum_name: str
    ordered_enum: Type[StrEnum]
    weights: list[float]

    def __init__(self, enum_name: str, ordered_enum: StrEnum, weights: list[float]):
        total_wt = sum(weights)
        assert np.isclose(total_wt, 1.0, rtol=1e-3), f"weights don't add up to 1.0 -> {total_wt}"
        super().__init__(
            enum_name=enum_name,
            ordered_enum=ordered_enum,
            weights=weights,
        )

    @classmethod
    # @model_validator(mode="before")
    def from_tuples(cls, enum_name: str, list_of_tuples: list[tuple]):
        """Assumes string value is in the first slot"""
        values = [row[0] for row in list_of_tuples]
        str_enum = StrEnum(enum_name, values)

        weights = np.array([row[1] for row in list_of_tuples], dtype=np.float32)
        total_weight = weights.sum()
        normalized = np.round(weights / total_weight, 5)
        return cls(enum_name=enum_name, ordered_enum=str_enum, weights=normalized)

    @classmethod
    # @model_validator(mode="before")
    def from_str_list(cls, enum_name: str, list_of_strs: list[str]):
        str_enum = StrEnum(enum_name, list_of_strs)

        weights = np.arange(len(list_of_strs)) + 1
        weights = 1 / weights
        total_weight = weights.sum()
        normalized = np.round(weights / total_weight, 5)
        return cls(enum_name=enum_name, ordered_enum=str_enum, weights=normalized)

    def generate_random_enums(
        self, n: int = 3, seed: int = -1, replace: bool = True
    ) -> list:
        if seed > 0:
            random_state = np.random.RandomState(seed)
        else:
            random_state = np.random.RandomState()
        return random_state.choices(self.ordered_enum, size=n, replace=replace)

    def generate_random_strings(
        self, n: int = 3, seed: int = -1, replace: bool = True
    ) -> list[str]:
        if seed > 0:
            random_state = np.random.RandomState(seed)
        else:
            random_state = np.random.RandomState()

        return random_state.choices(
            [row.value for row in list(self.ordered_enum)], size=n, replace=replace
        )
