#Declare your age as integer variable
age=20
#Declare your height as a float variable
height=5.1
#Declare a variable that store a complex number
comp=1+1j
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base=int(input("Enter base:"))
height=int(input("Enter height:"))
area_of_tri=0.5*base*height
print("Area:",area_of_tri)
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a=int(input("Enter side a:"))
b=int(input("Enter side b:"))
c=int(input("Enter side c:"))
peri=a+b+c
print("Perimeter of tri:",peri)
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lenth=int(input("Length:"))
wid=int(input("Width:"))
peri_rec=2*(lenth+wid)
print("peri of rec:",peri_rec)
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x_inter=int(input("x intercept:"))
slope=2
y=(2*x_inter)-2
print("Y=:",y)
print("slope:",slope)
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1=2
y1=2
x2=6
y2=10
m=((y2-y1)/(x2-x1))
print("slope:",m)
eucle=(((x2-x1)**2)+((y2-y1)**2))**1/2
print("Euclidian:",eucle)
#Compare the slopes in tasks 8 and 9.
print(slope == m)
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python")!= len("dragon"))
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in ('python'  and 'dragon'))
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
#There is no 'on' in both dragon and python
print('on' not in ('python' and 'dragon'))
#Find the length of the text python and convert the value to float and convert it to string
length=len("Rithi")
print("length:" ,length)
floa=float(length)
print("Float:", floa)
word=str(floa)
print("string:",word)
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num=int(input("Enter a num:"))
if num%2==0:
    print("Even")
else:
    print("odd")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
#Check if type of '10' is equal to type of 10
print(type('10') == type(10))
#Check if int('9.8') is equal to 10
print(int(float('9.8') )== 10)
#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Your weekly earning is", pay)
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
age=int(input("age:"))
seconds=365*24*60*60
remaining=100-age
lives=remaining*seconds
print("you have",lives ,"to live")
#Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125
for i in range(1,6):
    print(i,"1",i,i**2,i**3)