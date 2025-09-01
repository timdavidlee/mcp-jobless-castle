from enum import StrEnum
from pydantic import dataclass, Field

"""
Based on data
- from https://consumergoods.com/top-100-consumer-goods-companies-2024
"""


class CompanyCategory(StrEnum):
    BEVERAGES = "beverages"
    FOOD_PRODUCTS = "food-products"
    HOUSEHOLD_DURABLES = "household-durables"
    HOUSEHOLD_PRODUCTS = "household-products"
    INTERACTIVE_MEDIA = "interactive-media-and-services"
    MISCELLANEOUS = "miscellaneous"
    PERSONAL_CARE = "personal-care"
    PHARMACEUTICALS = "pharmaceuticals"
    TEXTILES_APPAREL_LUXURY = "textiles-apparel-luxury"
    TOBACCO = "tobacco"


@dataclass
class CpgCompany:
    name: str
    revenue_billions: float
    category: CompanyCategory
    alias: str | None = None
    products: list[str] = Field(default_factory=list)


COMPANIES = [
    CpgCompany(
        rank=3, name="PepsiCo", revenue=91.471, category=CompanyCategory.BEVERAGES,
        alias="PEPSICO"
    ),
    CpgCompany(
        rank=7,
        name="Anheuser-Busch InBev",
        revenue=59.38,
        category=CompanyCategory.BEVERAGES,
        alias="ANHEUSER"
    ),
    CpgCompany(
        rank=10,
        name="Coca-Cola Co.",
        revenue=45.754,
        category=CompanyCategory.BEVERAGES,
        alias="COCACOLA"
    ),
    CpgCompany(
        rank=12,
        name="Heineken Holding N.V.",
        revenue=39.857,
        category=CompanyCategory.BEVERAGES,
        alias="HEINEKEN"
    ),
    CpgCompany(
        rank=29, name="Diageo PLC", revenue=20.555,
        category=CompanyCategory.BEVERAGES,
        alias="DIAGEO"
    ),
    CpgCompany(
        rank=35,
        name="Asahi Group Holdings",
        revenue=18.733,
        category=CompanyCategory.BEVERAGES,
    ),
    CpgCompany(
        rank=46,
        name="Kirin Holdings",
        revenue=15.154,
        category=CompanyCategory.BEVERAGES,
    ),
    CpgCompany(
        rank=48,
        name="Keurig Dr Pepper",
        revenue=14.814,
        category=CompanyCategory.BEVERAGES,
    ),
    CpgCompany(
        rank=54, name="Pernod Ricard", revenue=12.72,
        category=CompanyCategory.BEVERAGES
    ),
    CpgCompany(
        rank=59,
        name="MolsonCoors Brewing Co.",
        revenue=11.702,
        category=CompanyCategory.BEVERAGES,
    ),
    CpgCompany(
        rank=63,
        name="Carlsberg A/S",
        revenue=10.685,
        category=CompanyCategory.BEVERAGES,
    ),
    CpgCompany(
        rank=69,
        name="Constellation Brands",
        revenue=9.453,
        category=CompanyCategory.BEVERAGES,
    ),
    CpgCompany(
        rank=76,
        name="Thai Beverage Public Co.",
        revenue=8.415,
        category=CompanyCategory.BEVERAGES,
    ),
    CpgCompany(
        rank=89,
        name="San Miguel Food & Beverage",
        revenue=6.754,
        category=CompanyCategory.BEVERAGES,
    ),
    CpgCompany(
        rank=1,
        name="Nestle SA",
        revenue=103.984,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=5, name="JBS S.A.", revenue=72.918, category=CompanyCategory.FOOD_PRODUCTS
    ),
    CpgCompany(
        rank=8,
        name="Tyson Foods",
        revenue=52.881,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=15,
        name="Mondelez International",
        revenue=36.016,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=19, name="Danone", revenue=29.892, category=CompanyCategory.FOOD_PRODUCTS
    ),
    CpgCompany(
        rank=20,
        name="Kraft Heinz",
        revenue=26.64,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=23,
        name="Associated British Foods",
        revenue=24.233,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=26,
        name="Grupo Bimbo",
        revenue=22.85,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=31,
        name="General Mills",
        revenue=20.094,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=37,
        name="Yili Group",
        revenue=17.612,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=38,
        name="Kellogg Co.",
        revenue=16.46,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=43,
        name="Fonterra Cooperative Group",
        revenue=15.32,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=44,
        name="Uni-President Enterprises",
        revenue=15.205,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=45,
        name="Arla Foods",
        revenue=15.199,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=49,
        name="Royal Friesland Campina N.V.",
        revenue=14.53,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=52,
        name="China Mengniu Dairy Co.",
        revenue=13.891,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=53,
        name="Saputo, Inc.",
        revenue=13.234,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=56,
        name="Conagra Brands",
        revenue=12.277,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=57,
        name="Hormel Foods",
        revenue=12.11,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=61,
        name="Hershey Co.",
        revenue=11.165,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=62,
        name="BRF - Brasil Foods",
        revenue=10.739,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=65,
        name="First Pacific Co.",
        revenue=10.511,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=67,
        name="Danish Crown",
        revenue=10.03,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=70,
        name="Campbell Soup Co.",
        revenue=9.357,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=74,
        name="NH Foods Ltd.",
        revenue=8.708,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=75,
        name="J.M. Smucker Co.",
        revenue=8.529,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=77, name="ITC Ltd.", revenue=8.375, category=CompanyCategory.FOOD_PRODUCTS
    ),
    CpgCompany(
        rank=83,
        name="Savencia SA",
        revenue=7.517,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=86,
        name="Post Holdings",
        revenue=6.991,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=92,
        name="McCormick & Co.",
        revenue=6.662,
        category=CompanyCategory.FOOD_PRODUCTS,
    ),
    CpgCompany(
        rank=14,
        name="Haier Smart Home Co., Ltd.",
        revenue=36.529,
        category=CompanyCategory.FOOD_DURABLES,
    ),
    CpgCompany(
        rank=34,
        name="Whirlpool Corp.",
        revenue=19.455,
        category=CompanyCategory.FOOD_DURABLES,
    ),
    CpgCompany(
        rank=41,
        name="BSH Hausgeräte",
        revenue=15.433,
        category=CompanyCategory.FOOD_DURABLES,
    ),
    CpgCompany(
        rank=55,
        name="AB Electrolux",
        revenue=12.679,
        category=CompanyCategory.FOOD_DURABLES,
    ),
    CpgCompany(
        rank=72,
        name="Groupe SEB",
        revenue=8.861,
        category=CompanyCategory.FOOD_DURABLES,
    ),
    CpgCompany(
        rank=79,
        name="Newell Brands",
        revenue=8.133,
        category=CompanyCategory.FOOD_DURABLES,
    ),
    CpgCompany(
        rank=82,
        name="Arcelik A.S.",
        revenue=7.544,
        category=CompanyCategory.FOOD_DURABLES,
    ),
    CpgCompany(
        rank=4,
        name="Procter & Gamble",
        revenue=82.006,
        category=CompanyCategory.HOUSEHOLD_PRODUCTS,
    ),
    CpgCompany(
        rank=24,
        name="Henkel AG",
        revenue=23.285,
        category=CompanyCategory.HOUSEHOLD_PRODUCTS,
    ),
    CpgCompany(
        rank=30,
        name="Kimberly-Clark Corp.",
        revenue=20.431,
        category=CompanyCategory.HOUSEHOLD_PRODUCTS,
    ),
    CpgCompany(
        rank=33,
        name="Colgate-Palmolive Co.",
        revenue=19.457,
        category=CompanyCategory.HOUSEHOLD_PRODUCTS,
    ),
    CpgCompany(
        rank=36,
        name="Reckitt Benckiser",
        revenue=18.647,
        category=CompanyCategory.HOUSEHOLD_PRODUCTS,
    ),
    CpgCompany(
        rank=85,
        name="Clorox Co.",
        revenue=7.389,
        category=CompanyCategory.HOUSEHOLD_PRODUCTS,
    ),
    CpgCompany(
        rank=58,
        name="Nintendo Co.",
        revenue=11.852,
        category=CompanyCategory.INTERACTIVE_MEDIA,
    ),
    CpgCompany(
        rank=84,
        name="Electronic Arts",
        revenue=7.426,
        category=CompanyCategory.INTERACTIVE_MEDIA,
    ),
    CpgCompany(
        rank=88,
        name="Bandai Namco Holdings Inc.",
        revenue=6.822,
        category=CompanyCategory.INTERACTIVE_MEDIA,
    ),
    CpgCompany(
        rank=100,
        name="Mattel, Inc.",
        revenue=5.441,
        category=CompanyCategory.INTERACTIVE_MEDIA,
    ),
    CpgCompany(
        rank=18, name="3M Co.", revenue=32.681,
        category=CompanyCategory.MISCELLANEOUS
    ),
    CpgCompany(
        rank=21,
        name="WH Group Ltd.",
        revenue=26.236,
        category=CompanyCategory.MISCELLANEOUS,
    ),
    CpgCompany(
        rank=40,
        name="Stanley Black & Decker",
        revenue=15.781,
        category=CompanyCategory.MISCELLANEOUS,
    ),
    CpgCompany(
        rank=81,
        name="Masco Corporation",
        revenue=7.967,
        category=CompanyCategory.MISCELLANEOUS,
    ),
    CpgCompany(
        rank=6,
        name="Unilever N.V.",
        revenue=64.509,
        category=CompanyCategory.PERSONAL_CARE,
    ),
    CpgCompany(
        rank=11, name="L’Oréal", revenue=44.572,
        category=CompanyCategory.PERSONAL_CARE
    ),
    CpgCompany(
        rank=39,
        name="Estée Lauder Companies",
        revenue=15.91,
        category=CompanyCategory.PERSONAL_CARE,
    ),
    CpgCompany(
        rank=50, name="Essity", revenue=14.436,
        category=CompanyCategory.PERSONAL_CARE
    ),
    CpgCompany(
        rank=51, name="Haleon", revenue=14.059,
        category=CompanyCategory.PERSONAL_CARE
    ),
    CpgCompany(
        rank=64, name="Kao Corp.", revenue=10.54,
        category=CompanyCategory.PERSONAL_CARE
    ),
    CpgCompany(
        rank=66,
        name="Beiersdorf AG",
        revenue=10.453,
        category=CompanyCategory.PERSONAL_CARE,
    ),
    CpgCompany(
        rank=87,
        name="Shiseido Co.",
        revenue=6.867,
        category=CompanyCategory.PERSONAL_CARE,
    ),
    CpgCompany(
        rank=91,
        name="Unicharm Corp.",
        revenue=6.687,
        category=CompanyCategory.PERSONAL_CARE,
    ),
    CpgCompany(
        rank=97,
        name="Church & Dwight Co., Inc.",
        revenue=5.868,
        category=CompanyCategory.PERSONAL_CARE,
    ),
    CpgCompany(
        rank=99,
        name="Coty, Inc.",
        revenue=5.554,
        category=CompanyCategory.PERSONAL_CARE,
    ),
    CpgCompany(
        rank=42,
        name="Johnson & Johnson Consumer Health",
        revenue=15.4,
        category=CompanyCategory.PHARMACEUTICALS,
    ),
    CpgCompany(
        rank=78,
        name="Abbott - Nutrition",
        revenue=8.154,
        category=CompanyCategory.PHARMACEUTICALS,
    ),
    CpgCompany(
        rank=90,
        name="Bayer Consumer Health",
        revenue=6.699,
        category=CompanyCategory.PHARMACEUTICALS,
    ),
    CpgCompany(
        rank=2,
        name="LVMH Moet Hennessy Louis Vuitton",
        revenue=94.444,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=9,
        name="Nike, Inc.",
        revenue=51.217,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=25,
        name="Adidas AG",
        revenue=23.19,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=27,
        name="Kering",
        revenue=21.176,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=28,
        name="Richemont",
        revenue=20.779,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=47,
        name="Hermes International",
        revenue=15.019,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=60,
        name="VF Corp.",
        revenue=11.612,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=68,
        name="Puma",
        revenue=9.521,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=71,
        name="PVH Corp.",
        revenue=9.024,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=73,
        name="Swatch Group AG",
        revenue=8.786,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=80,
        name="Skechers",
        revenue=8.0,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=93,
        name="Tapestry, Inc.",
        revenue=6.661,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=94,
        name="Ralph Lauren Corp.",
        revenue=6.444,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=95,
        name="Levi Strauss",
        revenue=6.179,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=96,
        name="Under Armour",
        revenue=5.904,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=98,
        name="Hanesbrands Inc.",
        revenue=5.637,
        category=CompanyCategory.TEXTILES_APPAREL_LUXURY,
    ),
    CpgCompany(
        rank=13,
        name="Imperial Tobacco Group",
        revenue=39.847,
        category=CompanyCategory.TOBACCO,
    ),
    CpgCompany(
        rank=16,
        name="Philip Morris International",
        revenue=35.174,
        category=CompanyCategory.TOBACCO,
    ),
    CpgCompany(
        rank=17,
        name="British American Tobacco PLC",
        revenue=33.937,
        category=CompanyCategory.TOBACCO,
    ),
    CpgCompany(
        rank=22, name="Altria Group", revenue=24.483, category=CompanyCategory.TOBACCO
    ),
    CpgCompany(
        rank=32,
        name="Japan Tobacco, Inc.",
        revenue=19.59,
        category=CompanyCategory.TOBACCO,
    ),
]
