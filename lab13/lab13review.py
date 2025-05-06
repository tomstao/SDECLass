"""
Tao Su
May 4, Python Class
"""
from symtable import Class


# example 1 1) review of __init__
class Person:
    def __init__(self, name, age):
        self.userName = name
        self.userAge = age

    def __str__(self):
        return f"UserName: {self.userName}\nUserAge: {self.userAge}"

    def intro(self):
         return f"Hi! I'm {self.userName} and I'm {self.userAge} years old."


# creat an object of the class
print("\n ------ Example 1------")
user1 = Person('Peter', 23)

print(user1)
print(user1.intro())

print("\n ------ Example 2------")
# example 2, private properties

class Chair:

    # accessible property
    chair_color = "brown"


    def __init__(self, height, width, length):
        self._chair_price = None
        self.height = height
        self.__width = width # define the private property 'width' to be very private
        self.chairLength = length * 2
    def get_chair_width(self):
        return self.__width

    def get_chair_length(self):
        return self.chairLength

    def chair_volume(self):
        return self.height * self.chairLength * self.get_chair_width()

    # method that returns the color
    def get_color(self):
        return self.chair_color

    # method to return the description of the chair

    def chair_description(self):
        return f"The total volume is {self.chair_volume()}.\n The chair color is {self.get_color()}"

    # method with a private property

    def set_price(self, price):
        self._chair_price = price

    @property
    def chair_price(self):
        return self._chair_price


# Create an object
userChair1 = Chair(2, 5, 9)
print(f"The chair length is: {userChair1.chairLength}")
#print(f"The chair width is: {userChair1.__width}") this will give error because it's a private property

# call method pass_length
print(f"The chair has length: {userChair1.get_chair_length()}")
print(f"The chair has volume: {userChair1.chair_volume()}")
print(f"{userChair1.chair_description()}")
userChair1.set_price(25)
print(f"The price of the chair is $ {userChair1.chair_price}")






