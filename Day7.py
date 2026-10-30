# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Exercises: Level 1
#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
li=("twit","tesla")
it_companies.update(li)
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.remove("Google")
print(it_companies)
#What is the difference between remove and discard
it_companies.discard("tesla")
print(it_companies)
#Exercises: Level 2
#Join A and B
print(A.union(B))
#Find A intersection B
print(A&B)
#Is A subset of B
print(A.issubset(B))
#Are A and B disjoint sets
print(A.isdisjoint(B))
#Join A with B and B with A
print(A|B)
print(B|A)
#What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#Delete the sets completely
del A
del B
del it_companies
#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
sets=set(age)
print(len(age))
print(len(sets))
print(len(age)==len(sets))
#Explain the difference between the following data types: string, list, tuple and set
lis=[1,2,3]
strig="apple"
tup=(1,2,3)
sets={1,2,3}
lis.insert(0,5)
print(lis)
print(strig.split())
print(tup.index(1))
sets.remove(1)
print(sets)
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
words="I am a teacher and I love to inspire and teach people"
spli=words.split()
print(spli)
sets=set(spli)
print(sets)
print(len(sets))