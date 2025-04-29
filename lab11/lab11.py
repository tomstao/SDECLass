"""
Tao Su
April 27, Python applications
"""
# importing all function from another file
from lab11_function import *

print("\n--------------- Example 1: Pythong dictionary--------------")

# create a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# print a complete dictionary
print(car)
# accessing items in a dictionary by using its key use [key]
print(f"The year of the car is {car["year"]}")
# update the value of the key
car["year"] = 1980
print(f"The year of the car is updated to {car['year']}")
# add jey: value pair
car["color"] = "red"
print(car)
print("\n Loop thorough each key in the dictionary")
for k in car:
    print(f"{k}")

print("\n Loop thorough each value in the dictionary")
for k in car:
    print(f"{car[k]}")

for k in car:
    print(f"{k} has value = {car[k]}")

print("\n--------------- Example 2: Pythong dictionary--------------")
# given the following list, create a dictionary that will count the number of times that a word appears in the string.
# create a dictionary to organize the words as the keys, and the number of occurrence of the word as the value of the key

phrase = "to be or not to be"
print(f"original: {phrase}")
phrase_split = phrase.split()
print(f"split: {phrase_split}")
# create a dictionary
word_count_dictionary = {}
# loop to each word in the list

for word in phrase_split:
    if word in word_count_dictionary:
        word_count_dictionary[word] += 1
    else:
        word_count_dictionary[word] = 1

#  print the result:
for w in word_count_dictionary:
    print("Result of dictionary:")
    print(f"{w}: appears {word_count_dictionary[w]} times")

print("\n ------------------ Example 3: Function that doesn't return values---------------")

# running a function
greeting()

# call the function 'print username'
print_username("Peter Pan")
print_username("Tao Su")

print("\n ------------------ Example 5: Function with default parameters---------------")
user_country("Martha", "Chile")
user_country("Anna")
user_country("", "France")

print("\n ------------------ Example 6: Function with return value---------------")
num1 = 2
num2 = 5
product1 = product(num1, num2)
print(f"Product of {num1} and {num2}: {product1}")
product2 = product()

check1 = multiple3(num1)
check2 = multiple3(num2)
print(f"Is {num1} a multiple of 3? {check1}")
print(f"Is {num2} a multiple of 3? {check2}")

print("\n ------------------ Example 8: composition function---------------")
number = collect_num()
print(number)

# test collect_num()
# number = collectnum()
# print(number)
# test sumnumbers()

sumall = summ_numbers(3)
print(sumall)

sumall = summ_numbers(3)
print(sumall)

print("\n ------------------ Example 9: built-in function---------------")
r = 2
area = area_circle(r)
# print(area)
area_print(area, r)

print("\n ------------------ Example 10: exception ---------------")
ration = ration_hour(0)
print(ration)

try:
    ration = ration_hour(0)
except ZeroDivisionError:
    print("Division by zero")

r1 = ration_hour(0)
r2 = ration_hour(3)
r3 = ration_hour("peter")
print(r1, r2, r3)

print("\n ------------------ Example 11: class ---------------")
# instantiate an instance of the class
x = Myclass()
print(f"Instance of the class {x}")
# call the class's property
use_id = x.customer_id
print(f"Customer ID: {use_id}")
# user message
print(x.f())

print("\n ------------------ Example 12: instantiation of classes ---------------")
# creat an instance of the class
pairComplexNumber = ComplexNumber(2, 3)
# call the instantiated object of the class
real = pairComplexNumber.real
imag = pairComplexNumber.imag
print(f"The real and imaginary consists of {real} and {imag}")

print("\n ------------------ Example 13: classes application ---------------")
# create an instance of the class
car1 = Car("Tesla", "S", 2023)
# call the property 'odometer_reading'
car_reading = car1.odometer_reading
print(f"Car miles reading is {car_reading}")
# call method 'get_car_description'
print(car1.get_car_description())
# call method 'read_odometer'
print(car1.read_odometer())
# update the mileage to 10
car1.update_odometer(10)
print(car1.read_odometer())
car1.update_odometer(10)
print(car1.read_odometer())

# add 20 miles to the odometer
car1.increment_odometer(20)
print(car1.read_odometer())
car1.increment_odometer(-5)
print(car1.read_odometer())
car1.increment_odometer(8)
print(car1.read_odometer())
