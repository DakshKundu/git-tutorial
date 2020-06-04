class TestClass():
    def __init__(self, food, favorite):
        self.food = food
        self.favorite = favorite
        self.food_nice = True if food == favorite else False
    def __repr__(self):
        if food_nice:
            print('its my favorite food!')
        else:
            print('its not my favorite, sad')