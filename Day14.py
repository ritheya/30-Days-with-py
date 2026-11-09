#Exercises: Level 1
#Explain the difference between map, filter, and reduce.
#map is used to apply particular condtion to each item in list
# reduce- will comite multiple itemx into one
#filter-will prit the item that pass the condition
#Explain the difference between higher order function, closure and decorator
#higher order function is used to perform  Takes another function as an argument.Returns another function as its result.
#Define a call function before map, filter or reduce, see examples.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mapping=list(map(lambda x:x**2,numbers))
print(mapping)
def is_even(numbers):
    if numbers%2==0:
        return True
    return False
filtering=filter(is_even,numbers)
print(list(filtering))
from functools import reduce
reducing=reduce(lambda x,y:int(x)+int(y),numbers)
print(reducing)
#Use for loop to print each country in the countries list.
for i in countries:
    print(i)
#Use for to print each name in the names list.
for i in names:
    print(i)
#Use for to print each number in the numbers list.
for i in numbers:
    print(i)
#Exercises: Level 2
#Use map to create a new list by changing each country to uppercase in the countries list
def upper_case(countries):
    resut=countries.upper()
    return resut
map_country=list(map(upper_case,countries))
print(map_country)
#Use map to create a new list by changing each number to its square in the numbers list
square_map=list(map(lambda x:x**2,numbers))
print(square_map)
#Use map to change each name to uppercase in the names list
#Use filter to filter out countries containing 'land'.
def check(countries):
    if 'land' in countries:
        return True
    return False
fil=list(filter(check,countries))
print(fil)
#Use filter to filter out countries having exactly six characters.
lamb=list(filter(lambda x:len(x)==6,countries))
print(lamb)
#Use filter to filter out countries containing six letters and more in the country list.
lambd=list(filter(lambda x:len(x)>6,countries))
print(lambd)
#Use filter to filter out countries starting with an 'E'
def efil(countries):
    if countries[0]=='E':
        return True
    return False
efiltre=list(filter(efil,countries))
print(efiltre)
#or
efill=list(filter(lambda x:x.startswith('E'),countries))
print(efill)
#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
num = map(lambda x: x**2, numbers)
fil = filter(lambda x: x % 2 == 0, num)
red = reduce(lambda x, y: x * y, fil)
print(red)
#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string item 
def get_string_lists(lst):
 ans=list(filter(lambda x:isinstance(x,str),lst))
 return ans
print(get_string_lists([1,2,'3','Rithi','Geets','2007']))
#Use reduce to sum all the numbers in the numbers list.
redd=reduce(lambda s,q:s+q,numbers)
print(redd)
#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
reduction=reduce(lambda x,y:x+' , '+y,countries[:-1])
reduction=reduction+' and '+ countries[-1]
reduction=reduction+' are north european countries'
print(reduction)
#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from Datas.countries import countries
def categorize_countries(pattern):
    answer=list(filter(lambda x:pattern in x,countries))
    return answer
print(categorize_countries('ia'))
print(categorize_countries('stan'))
print(categorize_countries('land'))
#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def return_dict():
 result={}
 for country in countries:
   letter=country[0]
   if letter in result:
      result[letter]+=1
   else:
      result[letter]=1
 return result     
print(return_dict())
#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
   count=[]
   for i in range(10):
         count.append(countries[i])
   return count
print(get_first_ten_countries())
#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
   count=[]
   count.append(countries[-10:])
   return count
print(get_last_ten_countries())
#Exercises: Level 3
#Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
from Datas.countries_data import countries_data
#Sort countries by name, by capital, by population
def sorting_name():
   result=sorted(
      countries_data,key=lambda x:x['name']
   )
   name=list(map(lambda x:x['name'],result))
   return name
print(sorting_name())

def sorting_capital():
   result=sorted(
      countries_data,key=lambda x:x['capital']
   )
   name=list(map(lambda x:x['capital'],result))
   return name
print(sorting_capital())
def sorting_pop():
   result=sorted(
      countries_data,key=lambda x:x['population']
   )
   name=list(map(lambda x:x['population'],result))
   return name
print(sorting_pop())
#Sort out the ten most spoken languages by location.
def most_spoken_lang():
   result={}
   for country in countries_data:
      for language in country['languages']:
       if language in result:
          result[language]+=1
       else:
          result[language]=1
   total=sorted(result.items(),key=lambda x:x[1],reverse=True)
   top_ten=total[:10]
   lang=list(map(lambda x:x[0],top_ten))
   return lang
print(most_spoken_lang())     
#Sort out the ten most populated countries.
def pop_countries():
   total=sorted(countries_data,key=lambda x:x['population'],reverse=True)
   top_ten=total[:10]
   popu=list(map(lambda x:x['name'],top_ten))
   return popu
print(pop_countries())