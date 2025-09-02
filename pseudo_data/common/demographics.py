from enum import StrEnum


class AgeRange(StrEnum):
    TEENS = "10"
    TWENTIES = "20"
    THIRTIES = "30"
    FOURTIES = "40"
    FIFTIES = "50"
    SIXTY_PLUS = "60"


class IncomeRange(StrEnum):
    TIER_20K = "0-20"
    TIER_30K = "20-40"
    TIER_40K = "40-60"
    TIER_60K = "60-100"
    TIER_100K = "100+"
