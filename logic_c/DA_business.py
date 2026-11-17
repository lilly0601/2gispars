from sqlalchemy import select

from database.db import SessionLocal
from database.models import Business


class DataAccessor:

    def output_business(self, business_id: str):
        with SessionLocal() as session:
            business = session.execute(
                select(Business).where(
                    Business.business_id == business_id
                )
            ).scalar_one_or_none()

            return business

    def insert_business(
        self,
        business_id,
        name,
        category=None,
        subcategory=None,
        address=None,
        latitude=None,
        longitude=None,
        rating=None,
        reviews_count=None,
        source="2gis"
    ):
        with SessionLocal() as session:

            business = Business(
                business_id=business_id,
                name=name,
                category=category,
                subcategory=subcategory,
                address=address,
                latitude=latitude,
                longitude=longitude,
                rating=rating,
                reviews_count=reviews_count,
                source=source
            )

            session.add(business)
            session.commit()
            session.refresh(business)

            return business

    def update_business(
        self,
        business,
        name,
        category=None,
        subcategory=None,
        address=None,
        latitude=None,
        longitude=None,
        rating=None,
        reviews_count=None,
        source="2gis"
    ):
        with SessionLocal() as session:

            business = session.merge(business)

            business.name = name
            business.category = category
            business.subcategory = subcategory
            business.address = address
            business.latitude = latitude
            business.longitude = longitude
            business.rating = rating
            business.reviews_count = reviews_count
            business.source = source

            session.commit()
            session.refresh(business)

            return business