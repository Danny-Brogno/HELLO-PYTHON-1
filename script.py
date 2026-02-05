print("--------------------------------------------------------------------------------------------")

x = 1
y = 2
sum = x + y
subtraction = y - x
multiplication = y * x 
division = y / x 

print(f"Sum -> 1+2={sum}   Subtraction -> 2-1={subtraction}   Multiplication -> 2x1={multiplication}   Division -> 2/1={division}")

if x > y:
    print(f"{x} is bigger than {y}")
elif x == y:
    print(f"{x} and {y} are the same")
else:
    print(f"{y} is bigger than {x}")
print("--------------------------------------------------------------------------------------------")

fruits = ["banana", "cherry", "oranges"]
x, y, z = fruits
print(fruits)
print(x,y,z)

print("--------------------------------------------------------------------------------------------")

a = 1
b = "hello"
is_raining = True

print(b, a, is_raining)
print(f"{b} {a} {is_raining}")

print("--------------------------------------------------------------------------------------------")

#string
c = str(1)
#integer
d = int(2)
#float (number as well, but DECIMAL)
e = float(3.1)
#complex (number as well, but mixed)
cde = 12j
print(f"{cde} IS A {type(cde)}")
print(f"{c} and {d} and {e}")
#CONVERSION
print(int(c))
print(str(c))

print("--------------------------------------------------------------------------------------------")

f = "awesome"

def myFunction():
    print(f"Python is {f}")
myFunction()

print("--------------------------------------------------------------------------------------------")

#MY EXERCISE
def dannyBrogno():
    name = "Danny"
    surname = "Brogno"
    age = 38
    city = "Edinburgh"
    hobby = "running"
    is_italian = True
    print(f"The 'name' variable is a {type(name)} = {name}")
    print(f"The 'age' variable is a {type(age)} = {age}")
    print(f"The 'is_italian' variable is a {type(is_italian)} = {is_italian}")
    print(f"My name is {name}, my surname is {surname}, I am {age} years old and I live in {city}. In my free time I like {hobby}")
dannyBrogno()

print("--------------------------------------------------------------------------------------------")

import random

# Generating a random number between 1 and 100
random_number = random.randrange(1,101)

# Printing the random number along with its data type
print(f"Random Number: {random_number}")
print("Data Type:", type(random_number))

print("--------------------------------------------------------------------------------------------")


fullName = "Danny Brogno"
job = "web developer"
print(fullName[0:5])
print(fullName[0], fullName[4])
print(job.upper())
print(job.replace("developer", "manager").upper())
if "Danny" not in fullName:
    print(f"There is no Danny")
elif "Danny" in fullName:
    print(f"There is Danny")
    
for fullName in fullName:
    print(fullName)

print("--------------------------------------------------------------------------------------------")

nineteen = 19
string_and_number = f"I am {nineteen}"
status = "   i am feeling STRESSED and overwhelmed   "
# Task: 
# 1. Remove the extra spaces at the start and end using .strip()
# 2. Replace "STRESSED" with "CALM"
# 3. Make the whole thing UPPERCASE
# 4. Print the result
stripped = status.strip()
replaced = stripped.replace("STRESSED", "calm")
toUpperCase = replaced.upper()
print(status.strip().replace("STRESSED", "calm").upper())
print(toUpperCase)
print(string_and_number)
print("--------------------------------------------------------------------------------------------")


# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Display the string manipulation menu
print("\nString Manipulation Menu:")
print("1. Convert to uppercase")
print("2. Convert to lowercase")
print("3. Slice the string")
print("4. Calculate string length")
print("5. Loop through characters")

# Prompt the user to enter their choice
choice = int(input("Enter your choice (1-5): "))

# Perform the selected string manipulation
if choice == 1:
    result = input_string.upper()
    print("Uppercase:", result)
elif choice == 2:
    result = input_string.lower()
    print("Lowercase:", result)
elif choice == 3:
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    result = input_string[start:end]
    print("Sliced string:", result)
elif choice == 4:
    length = len(input_string)
    print("String length:", length)
elif choice == 5:
    print("Characters:")
    for char in input_string:
        print(char)
else:
    print("Invalid choice.")
    
print("--------------------------------------------------------------------------------------------")

nameUser = input("Enter your name: ")
lastnameUser = input("Enter your lastname: ")
ageUser = int(input("Age: "))
locationUser = input("Where you live: ")
occupationUser = input("Your occupation: ")
fullNameUser = nameUser + " " + lastnameUser
modified_name = fullNameUser.upper()

if ageUser == 1:
    year_label = "year"
else:
    year_label = "years"
    
print(f"{modified_name} is a {ageUser} {year_label} old \"{occupationUser}\"\nthat lives in {locationUser}")

print("---------------------------------")

vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
article = "an" if occupationUser.startswith(vowels) else "a"
profile_desc = f"{modified_name} is {ageUser} years old, lives in {locationUser}, and works as \n{article} \"{occupationUser}\"."
print(profile_desc)

print("--------------------------------------------------------------------------------------------")
