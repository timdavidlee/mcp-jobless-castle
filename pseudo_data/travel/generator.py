import datetime
from datetime import timedelta
from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field

from pseudo_data.travel.entities import Country
from pseudo_data.travel.entities import HotelCompany
from pseudo_data.travel.entities import LodgingClass
from pseudo_data.travel.entities import generate_countries
from pseudo_data.travel.entities import generate_durations
from pseudo_data.travel.entities import generate_hotel
from pseudo_data.travel.entities import generate_lodging
from pseudo_data.travel.entities import generate_start_dates


class VacationOpening(BaseModel):
    vid: str = Field(default_factory=lambda: str(uuid4()))
    start_date: datetime.date
    end_date: datetime.date
    country: Country
    lodging_class: LodgingClass
    day_rate: float
    hotel_company: HotelCompany


class Reservation(BaseModel):
    rid: str = Field(default_factory=lambda: str(uuid4()))
    vacation_opening: VacationOpening
    reservation_people_count: int
    user: str
    home_country: Country
    phone_number: str
    start_date: datetime.date
    end_date: datetime.date


def generate_vacation_openings(n: int = 100):
    countries = generate_countries(n)
    hotels = generate_hotel(n)
    lodge_classes = generate_lodging(n)
    start_dates = generate_start_dates(n)
    durations = generate_durations(n)

    collector = []
    zip_package = zip(countries, hotels, lodge_classes, start_dates, durations)

    for c, h, lc, s, d in zip_package:
        l, r = lc
        collector.append(
            VacationOpening(
                start_date=s,
                end_date=s + timedelta(days=int(d)),
                country=c,
                lodging_class=l,
                day_rate=r,
                hotel_company=h,
            )
        )
    return collector
