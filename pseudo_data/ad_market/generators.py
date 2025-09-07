from datetime import datetime
from datetime import timedelta

import numpy as np
import pandas as pd
from pydantic import BaseModel

from pseudo_data.admarket.campaigns import AD_BANK
from pseudo_data.common._base import even_weight_generator
from pseudo_data.common.generators import CountryGenerator

DATEFORMAT = "%Y-%m-%d"
MIN_USERS = 100


class AdCampaign(BaseModel):
    name: str
    ad_category: str
    budget: int
    start_date: str
    end_date: str
    duration_days: int
    countries: list[str]
    target_user_count: int | None = None
    is_active: bool | None = None

    def model_post_init(self, __context=None):
        today = datetime.now().date().strftime(DATEFORMAT)
        self.is_active = (today > self.start_date) & (today < self.end_date)
        # can never be less than 2$ per click
        self.target_user_count = np.random.randint(MIN_USERS, self.budget // 2)


def generate_ad_budget(n: int = 10):
    return np.random.randint(100, 10_000, size=n) * 1_000


def generate_campaign_run_dates(
    n: int = 10, plus_minus_days: int = 45, max_duration: int = 45
):
    today = datetime.now().date()
    start_dates = np.random.randint(-plus_minus_days, 7, size=n)
    start_dates = [today + timedelta(days=int(sd)) for sd in start_dates]
    durations = np.random.randint(7, max_duration, size=n)
    end_dates = [
        sd + timedelta(days=int(dur))
        for sd, dur in zip(start_dates, durations, strict=True)
    ]
    return start_dates, end_dates


def generate_ad_campaigns(n: int = 10):
    budgets = generate_ad_budget(n=n)
    campaign_names = even_weight_generator(AD_BANK, n=n)
    start_dates, end_dates = generate_campaign_run_dates(n=n)
    collector = []
    for b, cn, sd, ed in zip(budgets, campaign_names, start_dates, end_dates):
        _, ad_category, ad_name = cn
        countries = CountryGenerator.generate_random_strings(n=3, replace=False)
        collector.append(
            AdCampaign(
                name=ad_name,
                ad_category=ad_category,
                budget=b,
                start_date=sd.strftime(DATEFORMAT),
                end_date=ed.strftime(DATEFORMAT),
                countries=countries,
                duration_days=(ed - sd).days,
            )
        )
    return collector


def calculate_current_ad_rates(list_of_ad_campaigns: list[AdCampaign]):
    df = pd.DataFrame.from_records([r.model_dump() for r in list_of_ad_campaigns])
    m = df["is_active"]
    agg_df = (
        df[m]
        .explode("countries")
        .groupby(["is_active", "countries"], as_index=False)
        .size()
        .sort_values("size", ignore_index=True)
    )

    agg_df["ad_rate"] = agg_df["size"].map(
        lambda x: np.exp2(np.random.rand() * 2 + (x - 1))
    )
    agg_df["ad_rate"] = agg_df["ad_rate"].map(lambda x: float(np.round(x, 2)))
    agg_df = agg_df[["countries", "size", "ad_rate"]].copy()
    agg_df.columns = ["country", "existing_ads", "ad_rate_per_user"]
    return agg_df
