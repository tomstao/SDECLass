"""
Tao Su
April 24, conditional statement
"""
print(f"\n------------ example 1 and 2: if statement ------------")

age = 20
ageCode = 123
if age >= 21:
    print("You are an adult!")
    ageCode = 200
else:
    print("You are under 21!")
    ageCode = 100

print(f"After the 'if' statement, ageCode is {ageCode}")

print(f"\n------------ example 3: multi statement ------------")
age = 50
if 0 <= age < 21:
    print("You are a minor!")
elif 21 <= age < 65:
    print("You are a adult!")
elif 65 <= age <= 130:
    print("You are a senior!")
else:
    print("Unable to reade the age!")

print(f"\n------------ example 4: and operator ------------")
temperature = 90
humidity = 60

if 70 <= temperature <= 90 and humidity < 80:
   print("The weather is pleasant!")
else:
    print("The weather is not ideal!")

print(f"\n------------ example 5: or operator ------------")

day = "Monday"

is_holiday = True

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("You can relex today!")
else:
    print("It's a workday!")

print(f"\n------------ example 6: nested conditional statement ------------")

number = int(input("Enter a number: "))
if number >= 0:
    if number == 0:
        print("The number is zero!")
    else:
        print(f"{number} is positive!")
else:
    print(f"{number} is negative!")

print(f"\n------------ example 7: nested conditional statement ------------")
# username validation. username must have 3+ characters
userName = input("Enter your name: ")
len_username = len(userName.strip())
if len_username >= 3:
    print(f"{userName} has {len_username} characters!")
    index_whiteSpace = userName.find(" ")
    if index_whiteSpace == -1:
        print(f"{userName} is valid!")
    else:
        print(f"Username cannot contain spaces!")

else:
    print(f"{userName} is an invalid username. username must have 3 or more characters.")

print(f"\n------------ example 8: match-case statement ------------")

response_code = 400

match response_code:
    case 400:
        print(f"Code = {response_code}. Server cannot understand")
    case 401 | 403:
        print(f"Code = {response_code}. Server refuse to send back")
    case 404:
        print(f"Code = {response_code}. Server cannot find")
    case _:
        print(f"Invalid code")

print(f"\n------------ Lab exercise ------------")
grade1 = float(input("Enter a grade1: "))
grade2 = float(input("Enter a grade2: "))

average = (grade1 + grade2) / 2
GPA = ""
if average >= 90:
    GPA = "A"
elif average >= 70:
    GPA = "B"
elif average >= 60:
    GPA = "C"
elif average >= 0:
    GPA = "Fail"
else:
    GPA = "UNDEFINED"
print(f"Your GPA is {GPA}!")
