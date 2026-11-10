# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries,es,ru=names
print('Nordic_countries:',nordic_countries)
print(es)
print(ru)
# Exercise 1: Student Marks Analyzer
# you are developing a student marks management program.
def stu_marks(*args):
     for index,item in enumerate(args):
           print(f'Marks at index{index}:{item}') 
     total=sum(args)
     avg=total/len(args)
     print('Total:',total)
     print("Average:",avg)
print(stu_marks(98,97,98,87,65,90))
#Exercise 2: Employee Information System
def emp(**employee):
      try:
       print(f"Name':{employee['name']}")
       print(f"deparment:{employee['department']}")
       print(f"salary:{employee['salary']}")
       print(f"experience:{employee['experience']}")
       return employee
      except KeyError as e:
           print(e)
employee1 = {
    'name': 'Ravi',
    'department': 'IT',
    'salary': 35000,
    'experience': 2
}
employee2 = {
    'name': 'Rani',
    'department': 'IT',
    'salary':55000,
    'experience': 9
}
print(emp(**employee1))
print(emp(**employee2))