#Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zero=[i for i in numbers if i<=0]
print(numbers)
#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list=[number for row in list_of_lists for number in row ]
print(flat_list)
#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Using list comprehension create the following list of tuples:
#[(0, 1, 0, 0, 0, 0, 0),
#(1, 1, 1, 1, 1, 1, 1),
#(2, 1, 2, 4, 8, 16, 32),
#(3, 1, 3, 9, 27, 81, 243),
#(4, 1, 4, 16, 64, 256, 1024),
#(5, 1, 5, 25, 125, 625, 3125),
#(6, 1, 6, 36, 216, 1296, 7776),
#(7, 1, 7, 49, 343, 2401, 16807),
#(8, 1, 8, 64, 512, 4096, 32768),
#(9, 1, 9, 81, 729, 6561, 59049),
#(10, 1, 10, 100, 1000, 10000, 100000)]
numbers_list=[tuple( i**j for j in range(0,6)) for i in range(0,11) ]
for item in numbers_list:
 print(item)
#Flatten the following list to a new list:
#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result=[
    [country.upper(),
    country[:3].upper(),
    capital.upper()]
    
    for inner in countries
    for country,capital in inner
  ]
print(result)
#Change the following list to a list of dictionaries:
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]
count = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
total=[
    {
        'country':country.upper(),
        'city':city.upper()
    }
    for inner in count
    for country,city in inner
]
print(total)
#Change the following list of lists to a list of concatenated strings:
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
res=[
    first_name+ ' ' + last_name
    for full in names
    for first_name,last_name in full
]
print(res)