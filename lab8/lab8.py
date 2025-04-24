"""
Tao Su
April 20, introduction Python
"""

# Single comment. This line will not run
print('n------- Example 1: string characters ------')
print("\tGood morning! \nThis is my first \"Python\" code!")

print('\n------Example 2: data type ------')
print(f"Data type of 3.56 = {type(3.56)}")
print(f"Data type of -25 = {type(-25)}")
print(f"Data type of 'Hello World!' = {type('Hello World!')}")
print(f"Data type of character '$' = {type('$')}")
print(f"Data type of False = {type(False)}")

print('n--------- Example 3: variables ---------')
# declare variables
number1 = 25.50
number2 = -12
userName = "Peter Pan"
add_numbers = number1 + number2
is_raining = True
# prompt results
print(f"{userName}, the sum of {number1} and {number2} is {add_numbers}")

print('\n------- Example 4: assigning values to multiple variables ----')
# declare multiple variables
item1, item2, item3 = "apples", 25, False
print(f"item1 = {item1}, item2 = {item2}, item3 = {item3}")
# declare multiple variables with the same value
score1 = score2 = score3 = 88
print(f"score1 = {score1}, score2 = {score2}, score3 = {score3}")

print('\n--------- Example 5: input command -------')
print("Enter username: ")
userName = input()
print(f"Collected user name = {userName}")

print("Enter a lucky number: ")
luckyNumber = input()
print(f"Lucky number = {luckyNumber}")

# double the lucky number. Cast string to int
dlLucky = int(luckyNumber) * 2
print(f"Double Lucky number = {dlLucky}")

# cast integer(or float) into string
triNumber = str(dlLucky) * 3
print(f"Double Lucky number = {triNumber}")

# cast int to bool value
# 0 = False, otherwise will be True
completed_task = 20
print(f"Completed task = {bool(completed_task)}")

print('\n--------- Example 6: arithmetic operators -------')
num1 = 15
num2 = 9
print(f"The sum of {num1} + {num2} = \t{num1 + num2}")
print(f"The difference between {num1} and {num2} = \t{num1 - num2}")
print(f"The product of {num1} and {num2} = \t{num1 * num2}")
print(f"The quotient of {num1} and {num2} = \t{num1 / num2}")
print(f"The remainder of {num1} and {num2} = \t{num1 % num2}")
print(f"The int quotient of {num1} and {num2} = \t{num1 // num2}")
print(f"The result of {num2} to the power of 3 = \t{num2 ** 3}")

print('\n--------- Example 7: finding the hypotenuse -------')
x = float(input("Enter side1: "))
y = float(input("Enter side2: "))
# calculate the hypotenuse
hyp = (x ** 2 + y ** 2) ** 0.5
# prompt the result
print(f"The hypotenuse of {x} and {y} is {hyp:5.2f}")

print('\n--------- Example 8: assignment operators -------')

n = 2
print(f"n = {n}")
n += 3
print(f"Number + 3 = {n + 3}")

n -= 2
print(f"n - 2= {n - 4}")

n *= 2
print(f"n * 2 = {n}")

n /= 3
print(f"n / 3 = {n / 3}")

n // 2
print(f"n //(quotient) 2 = {n / 2}")

n ** 2
print(f"n ** 2 = {n}")

n % 5
print(f"n % 5 = {n}")

print('\n--------- Example 9: comparison operators -------')

n1 = 10
n2 = 3
n3 = 7

compare1 = n1 == n2
compare2 = n1 == (n2 + n3)
print(f"is n1 equal to n2? {compare1}")
print(f"is n1 equal to n2 + n3? {compare2}")

compare3 = n1 > n2
compare4 = n2 <= n3
print(f"is n1 greater than n2? {compare3}")
print(f"is n2 less or equal to n3? {compare4}")

print('\n--------- Example 10: String indexing -------')
userName = "PeterPan123"
print(f"The fifth character = {userName[4]}")

# negative indexing
print(f"The fifth last character = {userName[-5]}")

print('\n--------- Example 11: String slice -------')
# slice from beginning to 4 th
print(f"Slice from the beginning to 4th character = {userName[:4]}")
# slice from the 5 th to the end
print(f"Slice from the 7th to the last end character = {userName[6:]}")
# slice from the 3rd to 8th
print(f"Slice form 3rd to 8 the = \t{userName[2:8]}")
# slice from the 4th to the 6th character using negative index
print(f"Slice form 4th to 6th using negative index = {userName[-8:-5]}")

print('\n--------- Example 12: total character in a string (len) -------')
print(f"The username has = {len(userName)} characters")

print('\n--------- Example 13: Strip method -------')
userName = "      peterpan123"
print(f"The username = {userName}. End of username")
userName = userName.strip()
print(f"The username = {userName}. End of username")

print('\n--------- Example 14: upper and lower method -------')

userName = userName.lower()
print(f"The username = {userName}. End of username")

userName = userName.upper()
print(f"The username = {userName}. End of username")

print('\n--------- Example 15: replace method -------')
userName = userName.replace('P', '%')
print(f"The username after replacing = {userName}. End of username")
print('\n--------- Example 16: split method -------')

msg = "Introduction to Python Programming! Today we are learning string methods"
print(f"Message =          {msg}")
print(f"Message after split method =          {msg.split()}")
print(f"Message after split method =          {msg.split('!')}")
print('\n--------- Example 17: find method -------')
# find the letter 'P'
index_P = msg.find('P')
print(f"The index of P =                {index_P}")
# find the second letter 'P'
sec_index_P = msg.find('P', index_P + 1)
print(f"The index of next P =           {sec_index_P}")
# find a non-existing letter 'Y'
index_Y = msg.find('Y')
print(f"The index of Y =           {msg.find('Y')}")

print('\n--------- Example 18: in, not in statement -------')
# check if the word 'we' is in the msg string
answer_we = "we" in msg
print(f"is the word 'we' in the 'msg' string? = {answer_we}")
answer_today = "Today" not in msg
print(f"is the word 'Today' in the 'msg' string? = {answer_today}")

print('\n--------- Example 19: list -------')
colors = ["orange", "magenta", "olive"]
numbers = [6, 20, --9, 5, -12]
emptyList = []
mixedList = [False, 20, "Peter", True, -9,"peter"]
print(f"colors =          {colors}")
print(f"numbers =         {numbers}")
print(f"emptyList =      {emptyList}")
print(f"mixedList =      {mixedList}")
print(f"2nd colors =          {colors[1]}")
print(f"first number =         {numbers[0]}")
# print(f"3rd item in emptyList =      {emptyList[2]}") # out of bond, can not return empty value.

print(f"last color =         {colors[-1]}")
print(f"3rd last number =         {numbers[-3]}")

print('\n--------- Example 20: * operator on list -------')

new_color = colors[0] + colors[-1]
print(f"The new color is {new_color}")

# concatenate the 2nd color with the 3rd number
# new_word = colors[1] + numbers[2] # data type error, this will cause error
# print(f"The new word is {new_word}")

print('\n--------- Example 21: remove the item from the list -------')
colors.pop(-1)
print(f"Remove the last value color =           {new_color}")

print('\n--------- Example 22: add the item to the list -------')
colors.append("pink")
print(f"add pink to colors =              {colors}")

# add multiple items to a list
# colors.append("RED", "PURPLE")
print('\n--------- Example 23: sort the items to the list -------')
colors.sort()
print(f"Sort colors  =    {colors}")
mixedList.sort()
print(f"mixed list sorted =       {mixedList}")

bool_list = [True, True, False]
bool_list.sort()
print(f"sorted bool list = {bool_list}")

print('\n--------- Example 24: count method -------')

count_true = bool_list.count(True)
print(f"The count of True is {count_true}")
count_red = colors.count("red")
print(f"The count of Red is {count_red}")

print('\n--------- Example 25: length of list -------')

length_colors = len(colors)
print(f"The length of colors is {length_colors}")

print('\n--------- Example 26: index method of list -------')

# index of color "olive"

index_olive = colors.index('olive')
print(f"The index of olive is {index_olive}")

# index of color green
# print(f"The index of green is {colors.index('green')}") value error
