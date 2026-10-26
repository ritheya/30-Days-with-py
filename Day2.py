#Exercises: Level 1
#Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
#Write a python comment saying 'Day 2: 30 Days of python programming'
#Declare a first name variable and assign a value to it
first_name="Rithi"
#Declare a last name variable and assign a value to it
last_name="Mahesh"
#Declare a full name variable and assign a value to it
full_name="Rithi Mahesh"
#Declare a country variable and assign a value to it
Country="India"
#Declare a city variable and assign a value to it
City="Theni"
#Declare an age variable and assign a value to it
age=19
#Declare a year variable and assign a value to it
year=2026
#Declare a variable is_married and assign a value to it
is_married=False
#Declare a variable is_true and assign a value to it
is_true= False
#Declare a variable is_light_on and assign a value to it
is_light_on=False
#Declare multiple variable on one line
print(first_name ,last_name ,full_name ,Country ,City ,age, year ,is_married ,is_true, is_light_on)
#Exercises: Level 2
#Check the data type of all your variables using type() built-in function
print(type(age))
#Using the len() built-in function, find the length of your first name
print(list(first_name))
#Compare the length of your first name and your last name
print(len(last_name))
print(len(first_name)==len(last_name))
print(len(first_name)<len(last_name))
print(len(first_name)>len(last_name))
#Declare 5 as num_one and 4 as num_two
num_one=5
num_two=4
#Add num_one and num_two and assign the value to a variable total
add=num_one+num_two
print(add)
#Subtract num_two from num_one and assign the value to a variable diff
sub=num_one-num_two
print(sub)
#Multiply num_two and num_one and assign the value to a variable product
mul=num_one*num_two
print(mul)
#Divide num_one by num_two and assign the value to a variable division
div=num_one/num_two
print(div)
#Use modulus division to find num_two divided by num_one and assign the value to a variable remander
remainder=num_two%num_one
print(remainder)
#Calculate num_one to the power of num_two and assign the value to a variable exp
pow=num_two**num_one
print(pow)
#Find floor division of num_one by num_two and assign the value to a variable floor_division
fd=num_two//num_one
print(fd)
#The radius of a circle is 30 meters.
radius=30
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle=3.14*radius*radius
print(area_of_circle)
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum=2*3.14*radius
print(circum)
#Take radius as user input and calculate the area.
radi=int(input("Radius:"))
area=3.14*radius*radius
print(area)
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first=input("Fname:")
print("Fname:",first)
Age=int(input("Age:"))
print("Age:",Age)
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
