#Exercises: Level 1
#Create an empty tuple
tup=tuple()
tup1=()
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
siblings1=("keerthi","Rene","Ruthi","sass")
siblings2=("mei","siddh","sridh")
#Join brothers and sisters tuples and assign it to siblings
siblings=siblings1+siblings2
print(siblings)
#How many siblings do you have?
print(len(siblings))
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings=list(siblings)
siblings.append("Appa")
siblings.append("Amma")
family=siblings.copy()
print(family)
#Exercises: Level 2
#Unpack siblings and parents from family_members=
first ,second,third,fourth,*rest,dad,mom=family
print(first)
print(second)
print(third)
print(fourth)
print(rest)
print(dad)
print(mom)
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=("Appe","Banana")
vegetables=("carrot","Beans")
animals=("Dog","Cat")
food=fruits+vegetables+animals
print(food)
#Change the about food_stuff_tp tuple to a food_stuff_lt list
food=list(food)
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

print(food[1:4])
#Slice out the first three items and the last three items from food_stuff_lt list

print(food[:3])

print(food[3:])
#Delete the food_stuff_tp tuple completely
del food
#Check if an item exists in tuple:

#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries )
print("Iceland" in nordic_countries)
