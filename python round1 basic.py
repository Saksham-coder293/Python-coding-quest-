#program 1 
"""Write a python program to do arithmetical operations addition and division
#Addition

num1 = int(input("Enter the first number for addition: "))
num2 = int(input("Enter the second number for addition: "))

sum_result = num1 + num2

print(f"sum: {num1} + {num2} = {sum_result}")


num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

div = num1/num2

print(f"Divsion: {num1} / {num2} is {div}") """

#program2 
#Write a python program to find the area of the triangle 

"""base = float(input("Enter the base of the traingle : "))
height = float(input("Enter the height of the traingle :  "))

area = 0.5 * base * height 

print(f"the area of the triangle is {area}")"""

#program 3 
#Write a python program to swap two variables 

"""a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of second variable (b) : ")

#Display the original values
print(f"Original values:a = {a}, b = {b}")
#swap the values using temp variable
temp = a
a = b
b = temp

print(f"Swapped values are a = {a}, b = {b}") """

#program 4
#program to generate a random number

"""import random

print(f"Random number : {random.randint(1,100)}")"""

#program 5 
#Write a python program to convert kilometers to miles

"""kilometers = float(input("Enter distance in kilometers : "))

#Conversion factor : 1 kilometers = 0.6213171 miles
conversion_factor = 0.6213171

miles = kilometers * conversion_factor

print(f"the conversed of {kilometers} km  is {miles} miles") """


#program 6
#write a python program to convert celsius to faraneheit 

"""celsius = int(input('Enter celsius :'))

#conversion value  fahrenheit = (Celsius * 9/5) + 32

fahrenheit = (celsius * 9/5) + 32

print(f"The {celsius} celsius is equal to {fahrenheit} fahrenheit")"""

#program 7 
#Write a python program to display calendar

"""import calendar

year = int(input("Enter year : "))
month = int(input("Enter month : "))

cal = calendar.month(year, month)
print(cal)"""

#program 8 
#Write a python program to solve  quadratic equation
#Input coeffecients 

"""import math 

#Input coeffecients
a = float(input("Enter coeffecient a : "))
b = float(input("Enter coeffecient b : "))
c = float(input("Enter coeffecient c : "))

#Calculate the discriminant 
discriminant = b **2 - 4*a*c

#check if discriminant is positive, negative or zero 
if discriminant > 0:
    #two real and distinct roots
   root1 = (-b + math.sqrt(discriminant)) / (2 * a)
   root2 = (-b - math.sqrt(discriminant)) / (2 * a)
   print(f"Root 1 : {root1}")
   print(f"Root 2: {root2}")
elif discriminant == 0 :
   #One real and distinct roots
   root = -b / (2* a)
   print(f"Root: {root}")
else:
   #complex roots 
   real_part = -b / (2 * a)
   imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
   print(f"Root 1: {real_part} + {imaginary_part}i")
   print(f"Root 2: {real_part} - {imaginary_part}i")"""


#program 9 
#Write a python program to swap two variables without temp variables

"""a = 5
b = 10

#swapping without temp variable
a,b = b,a

print("after swapping")
print("a=",a)
print("b=", b)  """

#program 10
#write a program to check if a number is positive, negative or zero 

"""num = int(input("Enter the number:"))

if num > 0:
    print("Num is positive")
elif num == 0 :
    print("Num is 0")
else:
    print("Num is positive") """



#program 11
#Write a program if a number is even or odd

"""num = int(input("Enter the number :"))

if num%2 == 0:
    print("The num is even")
else:
    print("The num is odd")"""


#program 12
#Write a python program to check leap year 

"""year = int(input("Enter a year : "))

#divided by 100 means century year (ending with 00)


#divided by 100 means century year (ending with 00)
#divide by 400 means it's a leap year 
if (year%400 == 0 )and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif(year% 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))"""


#program 13
#write a python program to check prime number

"""num = int(input("Enter the number : "))

#flag variable 
flag = False 

if num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
         flag = True
         break

if flag:
 print(f"{num} is not a prime number")
else:
  print(f"{num} is a prime number") """


#program 14 
#write a python program to print all the prime numbers witin an interval

"""lower = 0
upper = 10

print("The prime numbers between", lower, "and", upper, "are : ")

for num in range( lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num)  """


#program 15 
#write a program to find the factorial of a number

"""num = int(input("Enter a number :"))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers ")
elif num == 0:
    print("Factorial for 0 is 1")
else:
    for i in range(1, num +1):
        factorial = factorial * i 
    print(f"The factorial for {num} is {factorial}")"""

#program 16
#write a program to display the multiplication table 

"""num = int(input("Multiplication table for : "))

for i in range(1, 11):
    print(f"{num} * {i} = {num*i}") """

#program 17
#write a python program to print the fibonacci sequence 

"""Fibonacci sequence:
The Fibonacci sequence is a series of numbers where each number is the sum of the two
preceding ones, typicaly starting with 0 and 1. So, the sequence begins with 0 and 1, and
the next number is obtained by adding the previous two numbers. This pattern continues
indefinitely, generating a sequence that looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
Mathematicaly, the Fibonacci sequence can be defined using the folowing recurrence
relation:
𝐹(0
) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛 − 1) + 𝐹(𝑛 − 2)𝑓𝑜𝑟𝑛 > 1"""

"""nterms = int(input("How many terms? "))

#first two terms 
n1, n2 = 0, 1
count = 0

#check if the numbers of term is valid 

if nterms <= 0:
    print("Please enter a positive number ")
elif nterms  == 1:
    print("fibonacci series up to", nterms, ":")
    print(n1)
#generate fibonacci series 
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count += 1  """

#program 18
#write a python program to check armstrong number
"""Armstrong Number:
It is a number that is equal to the sum of its own digits, each raised to a power equal to the
number of digits in the number.
For example, let's consider the number 153:
It has three digits (1, 5, and 3).
If we calculate + , we get , which is equal to .
13 +
53 33 1 + 125 + 27 153
So, 153 is an Armstrong number because it equals the sum of its digits raised to the power
of the number of digits in the number.
Another example is 9474:
It has four digits (9, 4, 7, and 4). """


"""num = int(input("Enter a number: "))
# Calculate the number of digits in num
num_str = str(num)
num_digits = len(num_str)
# Initialize variables
sum_of_powers = 0
temp_num = num
# Calculate the sum of digits raised to the power of num_digits
while temp_num > 0:
  digit = temp_num % 10
sum_of_powers += digit ** num_digits
temp_num //= 10
# Check if it's an Armstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.") """

#program 20
# Write a python program to find armstrong number in an interval

#Input the interval from the user


"""lower = int(input("Enter the lower range :"))
   upper = int(input("Enter the upper range :"))


for num in range(lower, upper + 1):
   order = len(str(num))
   temp_num = num
   sum = 0

   while num > 0:
      digit = num % 10
      sum += digit ** num
      temp_num //= 10

#check if num is an armstrong number
   if num == sum:
     print(num)
"""

#program 20
#write a python program to find the sum of natural numbers

"""limit = int(input("Enter the limit : "))

sum = 0

for i in range(1, limit + 1):
   sum += i

print(f"The sum of the natural numbers up to ", limit,"is", sum)"""


#program 22
#write a program to find the LCM

"""def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0)) and ((greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))


print("The LCM of num1 and num2 is", compute_lcm(num1,num2)) """

#program 23
#write a program to find HCF of two numbers

# Python program to find H.C.F of two numbers
# define a function

"""def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if((x%i == 0)) and ((y %i == 0)):
            hcf = i
    return hcf

num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

print("The HCF of num1 and num2 is", compute_hcf(num1, num2))  """


#program 24 
#Write a program to convert decimal to binary,octal and hexadecimal  





      