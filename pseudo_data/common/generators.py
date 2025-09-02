import numpy as np
from time import perf_counter
from pseudo_data.common._base import WeightedEnumGenerator
from pseudo_data.common.consumer_brands import COMPANIES
from pseudo_data.common.demographics import AgeRange, IncomeRange
from pseudo_data.common.country import COUNTRIES_AND_GDP
from pseudo_data.common.people_names import FIRST_NAMES, LAST_NAMES


CompanyGenerator = WeightedEnumGenerator.from_tuples(
    "CpgCompany",
    [(row.alias, row.revenue) for row in COMPANIES],
)


AgeGenerator = WeightedEnumGenerator(
    enum_name="AgeRange",
    ordered_enum=AgeRange,
    weights=[1.0 / len(AgeRange) for _ in range(len(AgeRange))],
)


IncomeGenerator = WeightedEnumGenerator(
    enum_name="IncomeRange",
    ordered_enum=IncomeRange,
    weights=[1.0 / len(IncomeRange) for _ in range(1, len(IncomeRange))],
)


# based on GDP
CountryGenerator = WeightedEnumGenerator.from_tuples(
    "Country", [(row.alias, row.gdp) for row in COUNTRIES_AND_GDP]
)


class NameGenerator:
    def __init__(self, seed: int | None = None):
        seed = seed or int(perf_counter() * 100)
        self.state = np.random.RandomState(seed=seed)
        self._first_names = FIRST_NAMES
        self._last_names = LAST_NAMES

    def generate_full_names(self, n: int = 3):
        return [
            (fn, ln)
            for fn, ln in zip(
                self.state.choice(self._first_names, size=n),
                self.state.choice(self._last_names, size=n),
                strict=True,
            )
        ]

    def generate_usernames(self, n: int = 3):
        return [
            "{}.{}.{}".format(fn[0], ln, self.state.randint(1, 9000))
            for fn, ln in zip(
                self.state.choice(self._first_names, size=n),
                self.state.choice(self._last_names, size=n),
                strict=True,
            )
        ]
