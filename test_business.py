from logic_c.business_logic import BusinessLogic


logic = BusinessLogic()

business = logic.check_insert_business({
    "business_id": "test_001",
    "name": "Test Cafe",
    "category": "Кафе",
    "subcategory": "Кофейня",
    "address": "Караганда",
    "latitude": 49.806,
    "longitude": 73.085,
    "rating": 4.5,
    "reviews_count": 100,
    "source": "2gis"
})

print("Business saved:", business.name)
print("ID:", business.business_id)