from logic_c.DA_business import DataAccessor


class BusinessLogic:

    def __init__(self):
        self.DA_business = DataAccessor()

    def check_insert_business(self, business_info: dict):

        business_id = business_info.get("business_id")

        business = self.DA_business.output_business(
            business_id
        )

        if not business:

            business = self.DA_business.insert_business(
                business_id=business_id,
                name=business_info.get("name"),
                category=business_info.get("category"),
                subcategory=business_info.get("subcategory"),
                address=business_info.get("address"),
                latitude=business_info.get("latitude"),
                longitude=business_info.get("longitude"),
                rating=business_info.get("rating"),
                reviews_count=business_info.get("reviews_count"),
                source=business_info.get("source", "2gis")
            )

        else:

            business = self.DA_business.update_business(
                business=business,
                name=business_info.get("name"),
                category=business_info.get("category"),
                subcategory=business_info.get("subcategory"),
                address=business_info.get("address"),
                latitude=business_info.get("latitude"),
                longitude=business_info.get("longitude"),
                rating=business_info.get("rating"),
                reviews_count=business_info.get("reviews_count"),
                source=business_info.get("source", "2gis")
            )

        return business