#Exercises: Level 1
#Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print (i)

count=0
while count<11:
    print(count)
    count+=1
#Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i)


    
count=10
while count>=0:
    print(count)
    count=count-1
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
for i in range(1,8):
    print("#"*i)

count=1
while count<8:
 print("#"*count)
 count+=1
#Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(1,9):
 for j in range(1,9):
    print("#",end='')
 print()       
#Print the following pattern:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
count=0
while count<11:
   print(count,"x",count,'=',count**2)
   count+=1
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst=['Python', 'Numpy','Pandas','Django', 'Flask']
for code in lst:
   print(code)
#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,101,2):
   print(i)
#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1,101,2):
   print(i)
 #Exercises: Level 2
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#The sum of all numbers is 5050.
sum=0
for i in range(0,101):
   sum+=i
print(sum)
#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#The sum of all evens is 2550. And the sum of all odds is 2500.
sum=0
for i in range(0,101,2):
   sum+=i
print("Sum of even:",sum)
sum=0
for i in range(1,101,2):
   sum+=i
print("Sum of odd:",sum)
#Exercises: Level 3
#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print("Program started")
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
for i in range(-1, -5, -1):
    print(fruits[i])
print("Program ended")
#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from Datas.countries import countries
for country in countries:
   if "land" in country:
      print(country)
#Go to the data folder and use the countries_data.py file.
  #i)What are the total number of languages in the data
  #ii)Find the ten most spoken languages from the data
  #iii)Find the 10 most populated countries in the world
from Datas.countries_data import countries_data
languages=set()
for country_data in countries_data:
   for language in country_data['languages']:
     languages.add(language)
print(len(languages))
#ii

print("Program started")
lang_count = {}
for country in countries_data:
    for language in country['languages']:
        if language in lang_count:
            lang_count[language] += 1
        else:
            lang_count[language] = 1
print("Language counting completed")
print(len(lang_count))
sorted_lang = sorted(
    lang_count.items(),
    key=lambda x: x[1],
    reverse=True
)
print(sorted_lang[:10])
#iii
print("Population section started")
sorted_count = sorted(
    countries_data,
    key=lambda x: x['population'],
    reverse=True
)
for country in sorted_count[:10]:
    print(country['name'], country['population'])