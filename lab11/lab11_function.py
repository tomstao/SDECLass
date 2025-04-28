"""
Tao Su
April 27, functions
"""


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
def product(n1 = 1, n2 = 1):
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

def summ_numbers(total_numbers = 0):
    sum1 = 0
    for i in range(total_numbers):
        sum1 += collect_num()
    return sum1

# function to print result

def print_result(total_sum):
    print(f"Sum of numbers: {total_sum}")