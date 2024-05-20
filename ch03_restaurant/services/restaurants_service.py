from models.restaurant import Restaurant


class RestaurantService:
    def __init__(self):
        self.restaurant_db = Restaurant()

    def get_restaurants(self):
        return self.restaurant_db.get()