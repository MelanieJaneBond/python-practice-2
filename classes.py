class Cow:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.sex = ""
        self.health = ""
        self.purpose = ""
        self.story = ""
    
    def update_health(self, wellness):
        self.health = wellness

    def cow_story(self):
        print(f'{self.name} is a {self.sex} cow who is {self.age} years old and has been {self.health} for a long time. If {self.name} continues this way, the end of the story will be {self.purpose}.')
    
bessy = Cow()
bessy.name = "Bessy"
bessy.health = "ill"
bessy.purpose = "sad"
bessy.sex = "female"
bessy.age = 2
bessy.cow_story()

class Pizza:
    def __init__(self):
        self.size = 0
        self.crust = ""
        self.topping = ""
        self.order = ""
    
    def print_order(self):
        print(f'The customer would like a {self.size} inch pizza with {self.crust} and additional toppings: {self.topping}.')
    
    def add_topping(self, topping1, topping2):
        self.topping = topping1 + " and " + topping2


chicken_alfredo = Pizza()
chicken_alfredo.size = 24
chicken_alfredo.crust = "thin crust"
chicken_alfredo.add_topping("spinach", "tomato")
chicken_alfredo.print_order()