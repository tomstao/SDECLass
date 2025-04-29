"""
Tao Su
April 27, functions
"""
import math


def greeting():
    print("Hello, welcome to Python functions!")


# example 4, function with parameter 'username'

def print_username(username):
    print(f"Welcome to function, {username}!")


def user_country(userName="no name", country="Unknown"): {
    print(f"{userName} is living in {country}!")
}


# example 6: function that returns a value
# function that two numbers and return the product
def product(n1=1, n2=1):
    return n1 * n2


# Example 7 : Boolean function.
# function to check if a number is a multiple of 3

def multiple3(n):
    if n % 3 == 0 and n != 0:
        return True
    else:
        return False


# example 8: composition function
# define function to collect, validate, and return a number between  1 and 9

def collect_num():
    n = float(input("Enter a number between 1 and 9(inclusive): "))
    while n < 1 or n > 9:
        while not (1 <= n <= 9):
            n = float(input("re enter a number between 1 and 9(inclusive): "))
    return n


def summ_numbers(total_numbers=0):
    sum1 = 0
    for i in range(total_numbers):
        sum1 += collect_num()
    return sum1


# function to print result

def print_result(total_sum):
    print(f"Sum of numbers: {total_sum}")


# example 9
# define a function to calculate and return the area of a circle

def area_circle(radius):
    a = math.pi * pow(radius, 2)
    return round(a, 2)


# function to print result
def area_print(area, radius=0):
    print(f"Area of a circle with {radius} , its area is {area}")


# function to return the ration of two numbers (hours)
def ration_hour(hour):
    try:
        day_hour = 24
        return hour / day_hour
    except ZeroDivisionError:
        print("There was an error in the division")
    except ValueError:
        print("There was an error in the input")
        print("Please enter a number")
    except TypeError:
        print("There was an error in the input")
    except:
        print("There was an error in the input")
    else:
        return hour
    finally:
        print("process completed")


# example 11
class Myclass:
    # propety(attribute)
    customer_id = 1234

    # method
    def f(self):
        return "Welcome to Python class!"


# example12:
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


# example13:
class Car:
    # instatiate of the class
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    # set property 'odometer'
    odometer_reading = 0

    # method to return descriptive of the car
    def get_car_description(self):
        return f"{self.make}, with model {self.model}, was made when {self.year}"
    def read_odometer(self):
        return f"This car's odometer is {self.odometer_reading} miles on it."

    # method to update the odometer
    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Odometer Can\'t be roll back!")
    # method to add miles into the odometer

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Can't add negative miles to odometer!")