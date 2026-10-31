#Exercises: Level 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age=int(input("Enter age:"))
if age>18:
    print('you are allowed to drive')
else:
  years=18-age
  print("you have remaing {} to drive".format(years))
#Enter your age: 30
#You are old enough to learn to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.
#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
ur_age=int(input("Enter ur age:"))
my_age=20
if my_age>ur_age:
   print("I am older than u")
elif my_age<ur_age:
   print("u older than me")
else:
   print("we are same age")
if my_age!=ur_age:
   diff=abs(my_age-ur_age)
   if diff==1:
      print("we have {} gap".format(diff))
   else:
      print("we have {} gap".format(diff))
else:
   print("We have no gap")
#Enter your age: 30
#You are 5 years older than me.
#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a=int(input("Enter a:"))
b=int(input("Enter b"))
if a>b:
   print("a greater than b")
elif a<b:
   print("a is less than b")
else:
   print("a and b are equal")
#Enter number one: 4
#Enter number two: 3
#4 is greater than 3
#Exercises: Level 2
#Write a code which gives grade to students according to theirs scores:
#90-100, A
#80-89, B
#70-79, C
#60-69, D
#0-59, F
mark=int(input("Enter mark:"))
if mark>=90:
   print("Grade A")
elif mark>=80:
   print("Grade B")
elif mark>=70:
   print("Grade c")
elif mark>=60:
   print("Grade D")
else:
   print("Fail")
#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month=input("Enter Month:")

if month=='September' or month=='October' or month=='November':
   print("The season is Autumn ")
elif month=='December' or month=='January' or month=='February':
   print("The season is winter")
elif month=="March" or month=="April" or month=="May":
   print("The season is spring")
else:
   print("The season is summer")
#The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
if "kiwi" in fruits:
   print("fruit aldeready exist")
else:
   print("No")
   fruits.append("Kiwi")
print(fruits)
#Exercises: Level 3
#Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 #* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print("skills" in person)
if 'skills' in person:
    skills=person['skills']
    midd=len(skills)//2
    print(skills[midd])
else:
   print('skills not available')
 #* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
   if "Python" in person["skills"]:
      print("they have")
else:
   print("NO")
 #* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')

elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')

elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')

else:
    print('unknown title')
#* If the person is married and if he lives in Finland, print the information in the following format: 
#Asabeneh Yetayeh lives in Finland. He is married
per1={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if per1["is_married"] and per1['country']=='Finland':
   print(f"{per1["first_name"]} {per1['last_name']} lives in {per1['country']}")