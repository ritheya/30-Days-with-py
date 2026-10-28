#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first="Thirty"
sec="Days"
third="of"
fourth="python"
all=first+sec+third+fourth
print(all)
#Declare a variable named company and assign it to an initial value "Coding For All".
company="coding for all"
#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
#Cut(slice) out the first word of Coding For All string.
print(company[0:6])
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("coding"))
#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("coding for all ","python"))
#Change "Python for Everyone" to "Python for All" using the replace method or other methods.
lang="Python for everyone"
print(lang.replace("Python for everyone","Python for all"))
#Split the string 'Coding For All' using space as the separator (split()) .
word="Coding For All"
print(word.split())
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
comp2="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(comp2.split(","))
#What is the character at index 0 in the string Coding For All.
comp="Coding For All"
print(comp[0])
#What is the last index of the string Coding For All.
print(comp[-1])
#What character is at index 10 in "Coding For All" string.
print(comp[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
acro="Python For Everyone"
print(acro[0]+acro[7]+acro[11])
#Create an acronym or an abbreviation for the name 'Coding For All'.
acr="Coding For All"
print(acr[0]+acr[7]+acr[11])
#Use index to determine the position of the first occurrence of C in Coding For All.
print(comp.find('C'))
#Use index to determine the position of the first occurrence of F in Coding For All.
print(comp.find('F'))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(comp.rfind('l'))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sent="You cannot end a sentence with because because because is a conjunction"
print(sent.find("because"))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.rindex("because"))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent[30:54])
#Does 'Coding For All' end with a substring coding?
print(comp.endswith("coding"))
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
space='   Coding For All      ' 
print(space.strip(' '))
# Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython,thirty_days_of_python
id="thirty_days_of_python"
print(id.isidentifier())
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
fruit=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(fruit))
print("#".join(fruit))
#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.,I just wonder what is next.
line="I am enjoying this challenge. \n I just wonder what is nex"
print(line)
#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
row1="Name\tAge\tCountry\tCity"
row2="Asabeneh 250\tFinland\tHelsinki"
print(row1)
print(row2)
#Use the string formatting method to display the following:
#The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print("The area of the circle is{}".format(area))
#Make the following using string formatting methods:

a=8
b=6
print(f'{a}+{b}={a+b}')
print(f'{a}/{b}={a/b:.2f}')