from enum import StrEnum

import pytest

from pseudo_data.common._base import WeightedEnumGenerator


@pytest.fixture
def even_weight_dummy_generator():
    myenum = StrEnum("some_name", ["AA", "ZZ", "EE", "DD"])
    return WeightedEnumGenerator(
        enum_name="some_name", ordered_enum=myenum, weights=[0.25, 0.25, 0.25, 0.25]
    )


@pytest.fixture
def imbal_dummy_generator():
    myenum = StrEnum("some_name", ["BB", "KK", "GG", "FF"])
    return WeightedEnumGenerator(
        enum_name="some_name", ordered_enum=myenum, weights=[0.90, 0.05, 0.025, 0.025]
    )


def test_creation_from_init__name(even_weight_dummy_generator):
    assert even_weight_dummy_generator.enum_name == "some_name"


def test_creation_from_init__enums(even_weight_dummy_generator):
    assert set(
        [r.value for r in list(even_weight_dummy_generator.ordered_enum)]
    ) == set(["aa", "zz", "ee", "dd"])
