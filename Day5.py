#Exercises: Level 1
#Declare an empty list
lst=list()
print(lst)
#Declare a list with more than 5 items
age=[1,2,3,4,5]
#Find the length of your list
print(len(age))
#Get the first item, the middle item and the last item of the list
print(age[0])
print(age[1])
print(age[2])
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mix=["Rithi",20,151.2,False]
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.i
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
#Print the list using print()
print(it_companies)
#Print the number of companies in the list
print(len(it_companies))
#Print the first, middle and last company
first,*middle,last=it_companies
print(first)
print(middle)
print(last)
#Print the list after modifying one of the companies
it_companies[0]="Turing"
print(it_companies)
#Add an IT company to it_companies
it_companies.append("Renault")
#Insert an IT company in the middle of the companies list
it_companies.insert(2,"Foxcon")
#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1]=it_companies[1].upper()
print(it_companies)
#Join the it_companies with a string '#;  '
var="#".join(it_companies)
print(var)
#Check if a certain company exists in the it_companies list.
print("Google" in it_companies)
#Sort the list using sort() method
it_companies.sort()
print(it_companies)
#Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
#Slice out the first 3 companies from the list
print(it_companies[0:3])
#Slice out the last 3 companies from the list
print(it_companies[4:])
#Slice out the middle IT company or companies from the list
print(it_companies[2:4])
#Remove the first IT company from the list
print(it_companies.pop(0))
#Remove the middle IT company or companies from the list
del it_companies[2:4]
#Remove the last IT company from the list
print(it_companies.pop())
#Remove all IT companies from the list
it_companies.clear()
#Destroy the IT companies list
del it_companies
#Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
link1=back_end+front_end
print(link1)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
link2=link1.copy()
link2.insert(5,"Python")
link2.insert(6,"sql")
print(link2)
#Exercises: Level 2
#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print(ages)
print(max(ages))
print(min(ages))
#Add the min age and the max age again to the list
ages.append(max(ages))
ages.append(min(ages))
print(ages)
#Find the median age (one middle item or two middle items divided by two)

ages.sort()
n=len(ages)
if n%2==0:
    median=(ages[n//2-1]+ages[n//2])/2
else: 
    median=(ages[n//2])
print(median)
#Find the average age (sum of all items divided by their number )
avg=(sum(ages))/len(ages)
print(avg)
#Find the range of the ages (max minus min)
avg_range=max(ages)-min(ages)
print(avg_range)
#Compare the value of (min - average) and (max - average), use abs() method
print(abs(min(ages)-avg))
print(abs(max(ages) - avg))
print(abs(min(ages)-avg) < abs(max(ages) - avg))
#Find the middle country(ies) in the countries list
country=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway',"Nyc"]
middle=len(country)//2
print(country[middle])
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
middle=(len(country)+1)//2
firsthalf=country[:middle]
secondhalf=country[middle:]
print(firsthalf)
print(secondhalf)
#Unpack the first three countries and the rest as scandic countries.
one,two,three,*scandic=country
print(one)
print(two)
print(three)
print(scandic)