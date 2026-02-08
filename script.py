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

inputUserName = input("Enter your name: ").capitalize()
inputUserLastname = input("Enter your lastname: ").capitalize()

admins = [("Danny", "Brogno"), ("Franco", "Trentalance")]
bannedPeople = [("Mario", "Rossi"), ("Pileria", "Feliway")]
current_user = (inputUserName, inputUserLastname)

if current_user in admins:
    print(f"Welcome Admin {inputUserName} {inputUserLastname}!")
elif current_user not in admins and current_user not in bannedPeople:
    print(f"Welcome guest {inputUserName} {inputUserLastname}! You are cleared to enter.")
else:
    print("ACCESS DENIED: You are on the blacklist.")
    
print("--------------------------------------------------------------------------------------------")

def is_even(number):
    return number % 2 == 0    
print(is_even(6))

print("--------------------------------------------------------------------------------------------")

horror = input("Do you like horror films (yes/no): ").lower() == "yes"
thriller = input("Do you like thriller films (yes/no): ").lower() == "yes"
comedy = input("Do you like comedy films (yes/no): ").lower() == "yes"

if horror and thriller and not comedy:
    genre = "Horror-thriller"
elif comedy and horror and not thriller:
    genre = "Horror-comedy"
elif thriller and comedy and not horror:
    genre = "Comedy-thriller"
elif horror:
    genre = "Horror"
elif thriller:
    genre = "Thriller"
elif comedy:
    genre = "Comedy"
else:
    genre = "Unknown"
    
if genre == "Horror-thriller":
    print(f"Recommended movies for Horror-thriller: Prey, Alone, the Innocent")
elif genre == "Horror-comedy":
    print(f"Recommended movies for Horror-comedy: Jennifer's Body, Shaun of the Dead, Scary Movie")
elif genre == "Comedy-thriller":
    print(f"Recommended movies for Comedy-thriller: Knives our, Idiocracy, the Menu")
elif genre == "Horror":
    print(f"Recommended movies for horror: IT, Alone in the Dark, Saw")
elif genre == "Thriller":
    print(f"Recommended movies for thriller: American psyco, Zodiac, Split")
elif genre == "Comedy":
    print(f"Recommended movies for comedy: Without a paddle, Night shift, Naked Gun")
else:
    print(f"Sorry, we couldn't determine your movie preferences.")
    
print("--------------------------------------------------------------------------------------------")

my_list = [1,2,3,4,5]
my_list.insert(5,6)
my_list.insert(0,0)
print(my_list)

print("--------------------------------------------------------------------------------------------")

# Create a list of test scores
scores = [8, 8, 8, 8, 8, 7, 7, 9, 9]

# Calculate the average score using floor division
total_score = sum(scores)
num_tests = len(scores)
average_score = total_score // num_tests

print(average_score)

# Determine the grade using comparison operators
if average_score == 10:
    grade = "Ottimo"
elif average_score == 9:
    grade = "Distinto"
elif average_score == 8:
    grade = "Buono"
elif average_score == 7:
    grade = "Discreto"
elif average_score == 6:
    grade = "Sufficiente"
else:
    grade = "Insufficiente"
    
print(grade)

# This turns "Discreto" into "Discreto+"
if average_score % 1 >= 0.5:
    grade += "+"

#Check if there is a lower average (than 5)
if average_score <= 5:
    print(f"Oh no, your average is insufficient -> {average_score}!")
else:
    print(f"Your average is looking good -> {average_score}!")
    

print("--------------------------------------------------------------------------------------------")

# TUPLE (IMMUTABLE list -> cannot be edited, NOT unique (can have duplicates), ORDERED)
# TUPLE (IMMUTABLE list -> cannot be edited, NOT unique (can have duplicates), ORDERED)
# TUPLE (IMMUTABLE list -> cannot be edited, NOT unique (can have duplicates), ORDERED)

names = ("danny", "karl", "tricsy", "rhyz", "buffy", "tricsy")
for i in names:
    print(i)
if "tricsy" in names:
    print(f"Tricsy is inside the Tuple!")
else:
    print(f"Tricsy is NOT inside the Tuple!")
print(f"Tricsy ->  times in the Tuple: {names.count("tricsy")}")
print(f"TUPLE: {names}")

#LIST (can be edited, NOT unique (can have duplicates), ORDERED)
#LIST (can be edited, NOT unique (can have duplicates), ORDERED)
#LIST (can be edited, NOT unique (can have duplicates), ORDERED)

myList1 = [1,2,3]
myList2 = [4,5,6]

myList3 = myList1 + myList2 

print(f"LISTS: {myList3}")

#SET (can be edited, unique (diplicates disappear), UNORDERED)
#SET (can be edited, unique (diplicates disappear), UNORDERED)
#SET (can be edited, unique (diplicates disappear), UNORDERED)

mySet1 = {1, 2, 3}
mySet2 = {4, 5, 6}

mySets3 = mySet1 | mySet2

print(f"SETS: {mySet1 | mySet2}")
testSet = {1, 2, 2, 3, 3, 3}
print(f"TEST DUCPLICATES IN SET: {testSet}")

#FROZEN SET ->IMMUTABLE
#FROZEN SET ->IMMUTABLE
#FROZEN SET ->IMMUTABLE
my_frozen_set = frozenset({1,2,3})
print(my_frozen_set)

print("--------------------------------------------------------------------------------------------")

student1 = ("Danny", "Brogno", 15, 1)
student2 = ("Tricsy", "Brogno", 14, 2)
student3 = ("Rhyz", "Maclan", 13, 3)

students = (student1, student2, student3)
print(f"number of students: {len(students)}")
print(f"Index of Tricsy Brogno: {students.index(student2)+1}")

studentSetId = {19, 69, 100}
studentCourses = {"Maths", "English", "Robotics"}
print(f"Student IDs: {studentSetId}")
print(f"Courses: {studentCourses}")

new_students = {23, 88}
studentSetId.update(new_students)
print(f"Updated Student IDs: {studentSetId}")

print("--------------------------------------------------------------------------------------------")

