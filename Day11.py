#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def  add_two_numbers(n1,n2):
    sum=n1+n2
    return sum
print(add_two_numbers(1,4))
print(add_two_numbers(7,4))
#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi=3.14
    area=pi*(r**2)
    return area
print(area_of_circle(6))
#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    for i in args:
        if not isinstance(i, (int, float)):
            print("All arguments must be numbers")
            return
        total = sum(args)
        return total
print(add_all_nums(1,2,3,4,5.8))
#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def celtofaren(c):
    f=str((c*(9/5))+32)+"F"
    return f
print(celtofaren(0))
#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(args):
    if args in['jan','feb','dec']:
       return 'winter'
    elif args in['may','apr','mar']:
        return 'summer'
    elif args in['jun','jly','aug']:
        return 'autumn'
    elif args in['sep','oct','nov']:
        return 'spring'
    else:
        return "invalid no season will going to return"
print(check_season("jan"))
#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x,y,c):
    if x==0:
        return "INvalid value of x"
    m=(y-c)/x
    return m
print("slope",calculate_slope(1,2,3))
#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath
def solve_quadratic_eqn(a,b,c):
    if a==0:
        print("Invalid")
    d=(b**2)-(4*a*c)
    if d>0:
        X1=(-b+cmath.sqrt(d))/(2*a)
        x2=(-b-cmath.sqrt(d))/(2*a)
        return x1,x2
    elif d==0:
        x=(-b)/(2*a)
        return x,x
    else:
         x1=(-b+cmath.sqrt(d))/(2*a)
         x2=(-b-cmath.sqrt(d))/(2*a)
         return x1,x2
print(solve_quadratic_eqn(1,2,3))
#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for i in list:
     print(i)
print(print_list([1,3,3,4,]))
#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
#print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
#print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
def reverse_list(arr):
    reverse_list=[]
    for array in range(len(arr)-1,-1,-1):
        reverse_list.append(arr[array])
    return reverse_list
print(reverse_list(arr=[1,2,3,4,5]))
print(reverse_list(['a','b','c']))
#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    cap_lst=[]
    for i in lst:
         capital=i.upper()
         cap_lst.append(capital)
    return cap_lst
print(capitalize_list_items(['apple',"balon","cat"]))
#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(food_stuff,item):
  food_stuff.append(item)
  return food_stuff
print(add_item( ['Potato', 'Tomato', 'Mango', 'Milk'],'Meat'))
#food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#print(add_item(food_stuff, 'Meat')) 
 # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
#numbers = [2, 3, 7, 9];
#print(add_item(numbers, 5))  
def add_item(numbers,item):
    numbers.append(item)    
    return numbers
print(add_item([2,3,7,9],5))
#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
#print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
def remove_item(item_list,item):
   item_list.remove(item)
   return item_list
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'],'Mango'))
#numbers = [2, 3, 7, 9]
#print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(numbers,item):
    numbers.remove(item)
    return numbers
print(remove_item([2, 3, 7, 9],3))
#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
#print(sum_of_numbers(5))  # 15
#print(sum_of_numbers(10)) # 55
#print(sum_of_numbers(100)) # 5050
def sum_of_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))
#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    sum=0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i
    return sum
print(sum_of_odds(3))
print(sum_of_odds(2))
#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
    return sum
print(sum_of_even(7))
print(sum_of_even(2))
#Exercises: Level 2
#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    # print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 50.
def evens_and_odds(n):
   even_counter=0
   odd_counter=0
   for i in range(1,n+1):
            if i%2==0:
                even_counter+=1
            else:
                odd_counter+=1
   print("Num of evev:",even_counter) 
   print("Num of odd:",odd_counter)    
evens_and_odds(100)
#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def facto(n):
    mul=1
    for i in range(1,n+1):
        mul*=i
    return mul
print(facto(5))
print(facto(3))
#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(lst):
    if not lst:
        return True
    else:
        return False
print(is_empty([]))
print(is_empty([1,2,3]))
#Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
#    greet()
    # "Hello, Guest!
  #  greet("Alice")
    # "Hello, Alice!"
def greet(name='Guest!'):
  print('HELOO',name)
greet()
greet('Alice!')
#Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
#show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
#show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny
def show_args(**args):
    print("received:",args)
show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")
#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(num):
    total=sum(num)/len(num)
    return total
print(calculate_mean([1,2,3,4,5]))
#calculate_median
def calculate_median(num):
    ordered=sorted(num)
    n=len(ordered)
    if n%2==1:
        return ordered[n//2]
    else:
        left=ordered[n//2-1]
        right=ordered[n//2]
        result=(right+left)/2
        return result
print(calculate_mean([1,2,3,5]))
#calculate_mode
def calculate_mode(num):
    count={}
    for value in num:
        if value in count:
            count[value]+=1
        else:
            count[value]=1
    high=max(count.values())
    for value,frequency in count.items():
        if frequency==high:
            return value
print(calculate_mode([1,2,3,3,4,4,4,5,5]))
#calculate_range
def calculate_range(num):
    range=max(num)-min(num)
    return range
print("Range:",calculate_range([1,2,3]))
#calculate_variance
def calculate_variance(num):
    mean=sum(num)/len(num)
    square_diff=[]
    for x in num:
        diff = x-mean
        square=diff**2
        square_diff.append(square)
    var=sum(square_diff)/len(num)
    return var
print(calculate_variance([2,4,7,8]))
#calculate_std
import math
def calculate_std(num):
    mean=sum(num)/len(num)
    var=sum((x-mean)**2 for x in num) /len(num)
    std = math.sqrt(var)
    return std
print(calculate_std([1,2,3]))
#Exercises: Level 3
#Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
print(is_prime(2))
print(is_prime(10))
print(is_prime(7))
#Write a functions which checks if all items are unique in the list.
def unique(args):
    var=set(args)
    if len(args)==len(var):
        return True
    else:
        return False
print(unique([1,2,'set']))
print(unique([1,2,3,4]))
#Write a function which checks if all the items of the list are of the same data type.
def chech_type(args):
    var=type(args[0])
    for i in range(len(args)):
        if type(args[i])!=var:
            return False
    return True
print(chech_type([1,2,3,4,5]))
print(chech_type([1,2,'set',4,'lotus']))
#Write a function which check if provided variable is a valid python variable
def check_var(var):
    if  var.isidentifier():
     return True
    return False
print(check_var('isurcolab'))
print(check_var('12isurcolab'))
#Go to the data folder and access the countries-data.py file.
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
from Datas.countries_data import countries_data
print(type(countries_data))
def most_spoken_languages(countries_data) :
    languages_count={}
    for country in countries_data:
        for language in country['languages']:
          if language in languages_count:
            languages_count[language]+=1
          else:
            languages_count[language]=1
    result=sorted(languages_count.items(),key=lambda x:x[1],reverse=True)
    return result[:10]
print(most_spoken_languages(countries_data))
#Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

def most_populated_countries(countries_data):
    total=[]
    for country in countries_data:
       total.append((country['name'],country['population']))
    ans=sorted(total,key=lambda x:x[1],reverse=True)
    return ans[:20]
print(most_populated_countries(countries_data))