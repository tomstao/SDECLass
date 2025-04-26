"""

Tao Su
April 25, loops
"""
from operator import index

print("\n ----------- example 1: for loop as a counter ------------")

# print Hello from 0 to 4
for x in range(0, 5):
    print(f"Hello = {x}")

print("\n ----------- example 2 :for loop in a list ------------")
fruits = ["apple", "orange", "grapes", "kiwis", "pineapple"]
for each_fruitIndex in range(0, 5):
    print(f"Fruit with index {each_fruitIndex} = {fruits[each_fruitIndex]}")

# alternative way to loop through a list
print("\n ----------- Alternative way to loop through a list ------------")
for each_fruit in fruits:
    print(each_fruit)

print("\n ----------- example 3 :for loop with different increment ------------")

# for loop to print from 2 to 30, with
for num in range(2, 30, 3):
    print(num)

print("\n ----------- example 4 :for loop with different increment ------------")
# for loop to print 10 to 0, with decrement of 2
for num in range(10, 0, -2):
    print(num)

print("\n ----------- example 5 :for loop through a string ------------")
userName = "peterpan123"
for each_character in userName:
    print(each_character)

print("\n ----------- example 6 : nested conditional statement ------------")
numbers = [5, -2, 0, 8, 9, -1]
negative_counter = 0
for each_number in numbers:
    if each_number < 0:
        negative_counter += 1

# prompt result
print(f"There is/are {negative_counter} negative number/s")

print("\n ----------- example 7 :nested conditional statement: operation ------------")
# for loop to add all 'odd' numbers
sum_odd = 0
for each_number in numbers:
    if each_number % 2 != 0:
        sum_odd += each_number

# prompt the result
print(f"The sum of the odd numbers is: {sum_odd}")
# for loop to print from 0 to 10(exclusive), and terminate the loop when it reaches to 5
for n in range(0, 10):
    if n == 5:
        print("Counter reaches to 5")
        break
    else:
        print(n)

print("\n ----------- example 9 :continue statement in a loop ------------")
# for loop to add numbers from 0 to 10(exclusive), except
sumall = 0
for n in range(10):
    if n == 5:
        print("Skipping 5")
        continue

    sumall += n
    print(n)
    print(f"\tsum = {sumall}")

print("\n ----------- example 10:continue statement in a for loop ------------")
for n in range(6):
    if n == 3:
        break
    print(n)
else:
    print("Loop completed.")

print("\n ----------- example 11: while loop as a counter ------------")
n = 0

# while loop to print from 0 to 5 (inclusive) --> 0 1 2 3 4 5
while n < 6:
    print(n)
    n += 1

print("\n ----------- example 12: while loop as a checkpoint ------------")
# a while loop to collect and add numbers between 05 and 5.
# if the user enters a number that is not between -5 and 5, the while will terminate
sum_user_number = 0
while True:
    number  = int(input("Enter a number between -5 and 5: "))
    if number < -5 or number > 5:
        break
    sum_user_number += number

print(f"Ths sum is {sum_user_number}")


print("\n ----------- example 13: while loop as a a counting operator ------------")
numbers = [ 2, 0, -5, 1, 8, -6, 7, -3]
len_numbers = len(numbers)
even_count = 0
index = 0
while index < len_numbers:
    if index % 2 == 0 and (numbers[index] != 0):
        even_count += 1
    index += 1
else:
    print(f"There is/are {even_count} even numbers")
print("\n ----------- Lab10: exercise ------------")
"""
Given the following list:
colors = ['red', 'orange', 'olive', 'magenta', 'green']
complete the code by writing a Python program that:
Takes a color input from the user using the keyboard.
Strips any leading/trailing whitespace from the input.
Converts the input to lowercase.
Uses a for loop and a nested conditional statement to check whether the entered color is in the list colors.
Uses a flag to indicate when the color is found, and breaks the loop once a match is found.
Prints a message depending on whether the color was found in the list.

If the color is found:

_____ color is in the list


If the color is not found:

_____ color IS NOT in the list
"""

colors = ['red', 'orange', 'olive', 'magenta', 'green']

color = str(input("Enter a color: ")).lower().strip()
for each_color in colors:
    if each_color == color:
        print(f"The {color} color is in the list!")
        break;
else:
    print(f"The {color} color IS NOT in the list!")