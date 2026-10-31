#Create an empty dictionary called dog
dog={}
#Add name, color, breed, legs, age to the dog dictionary
dog={'name':'Tommy', 'color':'Brown', 'breed':'Lab', 'legs':4, 'age':2 }
print(dog)
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
stu={'first':'Rithi','gender':'F','age':20,'marital_status':'NO','skilss':['js','HTMl','CSS','java'],'addres':{'sreet':'palace','code':65789}}
#Get the length of the student dictionary
print(len(stu))
#Get the value of skills and check the data type, it should be a list
print(stu.get("skilss"))
print(type(stu.get("skilss")))
#Modify the skills values by adding one or two skills
stu["skilss"].append("py")
stu["skilss"].append("jason")
print(stu)
#Get the dictionary keys as a list
key=stu.keys()
print(key)
#Get the dictionary values as a list
val=stu.values()
print(val)
#Change the dictionary to a list of tuples using items() method
print(stu.items())
#Delete one of the items in the dictionary
stu.pop("age")
print(stu)
stu.popitem()
print(stu)
del stu["gender"]
print(stu)
#Delete one of the dictionaries
del dog
print(dog)