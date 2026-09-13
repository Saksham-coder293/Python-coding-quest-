#program 1
#print the sum of two numbers

"""a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 : "))


print("Sum of two number is", a + b) """


#program 2
#write a program to swap two variable using temp variable

"""a = 10
b = 5

print("Before swap", "a = ", a, "b = ", b)

temp = a
a = b
b = temp

print("after swap", "a = ", a, "b = ", b)  """


#program 3
#write a program to swap two variables without using temp variables

"""a = 10
b = 5

a , b = b, a

print("After swapping variables", "a = ", a, "b = ", b)  """


#program 4
#write a program to convert the string into different data types 

"""num_str = "40"

int_num = int(num_str)
float_num = float(num_str)
back_to_str = str(99)


print(int_num, type(int_num))
print(float_num, type(float_num))
print(back_to_str, type( back_to_str))  """


#program 5
#write a program to check the data types of particular variables

"""print(type(10))
print(type("hello"))
print(type(3.14))
print(type(True))
print(type([1,5,7]))  """


#program 6
#write a program for f string formatting Given a name and a marks value that shows the marks rounded too two values 

"""name = input("Enter the name ")
marks = float(input("Enter the marks : "))


print(f"{name} scored {marks:.2f} in test")  """


#program 7 

#write a program to caluclate multiple inputs into one line
"""x,y = input("Enter two numbers : ").split()     #breaks the input line at space 
x = int(x)
y = int(y)

print("Product  = ", x * y). """

#program 8
#write a program for calculating the area for the rectangle 

"""length = float(input("Enter length : "))
breadth = float(input("Enter breadth :  "))

area = length * breadth 

print("area of rectangle is ", area)  """

#program 9
#write a program to calculate the average of three numbers 


# map() applies int() to every piece produced by split () 

"""a,b,c = map(int, input("Enter the three inputs : ").split())

average = (a + b + c ) / 3
print("average of three inputs is", average)  """


#program 10
#write a program to convert seconds into hours, minutes, seconds 

"""total = int(input("Enter the input : "))

hours = total // 3600       #converts input seconds into hours 
minutes = (total%3600) // 60       #converts input seconds into minutes  
seconds = total % 60    #converts input seconds into seconds 


print(f"{total} into hours is {hours})")
print(f"{total} into minutes is {minutes})")
print(f"{total} into seconds is {seconds})") """

#program 11
#write a program about converting a value into char type 
#Concept: ord() and chr() for character –ASCII conversion.



"""char = input("Enter the char : ")

print(f"The ASCII Value for {char} is ", ord(char))
print(f"The character for ASCII  65  is ", chr(65))  """


#program 12
#write a program for kilometer to miles conversion 

"""kilometers = float(input("Enter a kilometers value : "))

miles = kilometers * 0.621721

print(f"The conversion for {kilometers} is {miles:.2f}")   """


#program 13
#write a program about string concatenation and repetetion 

"""word = input("Enter a word : ")
frequency = int(input("Enter the frequency : "))

#string concatenation

joined = word + word

#string repetetion 
repeated = word * frequency 


print(f"words after repeating value  is {joined} ")
print(f"words after repeating frequency  is {repeated}")  """

#program 14
#write a program for even and odd

"""num = int(input("enter the num : "))

if num%2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")  """


#program 15
#write a program for floor division and modulo representation 

#For the numbers 17 and 5, show the results of /, //, and %. Also show // and % with -17 to see how Python handles negatives.


"""a = 17
b = 5

print("The divison of a by b is", a //b)
print("The float divison of a by b is", a /b)
print("The remainder for  a and  b is", a%b)
print("The divison of a by b is", -a //b)
print("The divison of a by b is", -a /b) """


#program 16
#write a program for calculating the area of the circle 

"""import math 

radius = float(input("Enter the radius of the circle : "))


area = math.pi * radius ** 2

print(f"The area of the cicle is {area:.2f}") """

#program 17
#write a program for converting a value to a farahneit 

"""C = int(input("Enter then celsius value : "))


faraheneit =(9/5 )* C + 32

print(f"The conversion of {C} into faraheneit is {faraheneit:.2f}") """


#program 18
#conversion of farahneit into celsius 

"""faraheneit = float(input("Enter farahneit value : "))


celsius = (faraheneit - 32) * 5/9

print(f"the conversion for {faraheneit} is {celsius} ")"""


#program 19
#write a program for simple interest 

"""p = int(input("Enter principal : "))
r = int(input("Enter rate (per year): "))
t = int(input("Enter time (per year) : "))


si =(p * r * t) / 100  


print("The simple interest for p,r,t is", si) """

#program 20
#write a program for calculating compound interest 

"""p = int(input("Enter the principal : "))
r = int(input("Enter the rate (per percent in years) : "))
t = int(input("Enter the time (per years) : "))


amount = p * (1 + r/100) ** t 
ci = amount - p 

print("The final amount is ", amount)
print("The compound interest is", ci)  """

#program 21
#write a program to calculate the sum of digits 

"""num = int(input("Enter the input integer : "))

total = 0
n = num

while n > 0:
    total += n%10.   #extracts the last integer and add it in total
    n //= 10.   #removes the rest of the integers 


print("The sum of the integers is ", total )"""


#program 22
#write a program to reverse a number 

"""num = int(input("Enter a number : "))


rev = 0
n = num

while n > 0:
 rev = rev * 10 + n % 10
 n //= 10

print("The reversed num is ", rev)   """

#program 23
#write a program to count the digits in a number


"""num = int(input("Enter a number : "))


count = 0


while num > 0:
    count += 1
    num //= 10

print("The number of digits in the number entered is ",count)   """


#program 24
#write a program to calculate the power of a number without using **

"""base  = int(input("Enter the base : "))
exponent = int(input("Enter the exponent : "))

result = 1

for _ in range(exponent):
    result *= base 

print("The resulting exponent after without using ** is", result)"""

#program 25
#write a program to check if a number is palindrome is not 

"""num = int(input("Enter a number : "))


rev = 0
n = num

while n > 0:

 rev = rev * 10 + n % 10
 n //= 10

if num == rev:
 print("num is palindrome")
else:
 print("num is not palindrome") """

 #concept -  reversing a number and comparing it with original 

#another way

#(i) String palindrome

"""def is_palindrome(str):
 return str == str[::-1]

print(is_palindrome("NitiN"))

#(ii) Num palindrome 

def is_palindrome(n):
 return str(n) == str(n)[::-1]

print(is_palindrome(191))  """


#program 26
#write a program to cslculate the factorial of number

"""num = int(input("Enter the input : "))

factorial = 1

for i in range(1, num+1):
    factorial *= i 

print("factorial of the number is", factorial)"""

#program 27
#write a program to calculate all the factors of the number 


"""num = int(input("Enter a number : "))

for i in range(1, num+1):
    if num%i == 0:
        print("factors of the num are", i)  """

#program 28
#write a program to check whether the number is prime or not 

"""num = int(input("Enter the input number : "))

is_prime  = num > 1 # 2 is the smallest prime number 

for i in range(2,int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print("Number is prime")
else:
    print("Number is not prime")  """


#program 29
#write a program to check whether a number is armstrong is not 

"""num = int(input("Enter the number : "))

digits = len(str(num))

total = 0
n = num

while n > 0:
    total += (n%10) ** digits
    n //= 10

if total == num:
    print("num is armstrong number")
else:
    print("num is not armstrong")  """


#program 30
#write a program to check whether a number is perfect number 

"""num = int(input("Enter a number : "))


total = 0
for i in range(1, num):    #stop before num itself
    if num %i == 0:
        total += i

if total == num:
    print("The input number is perfect number")
else:
    print("The input number is not perfect number")   """


#program 31
#write a program to calculate the greatest common divisor program 

"""a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))

x,y = a,b

while y != 0:        


 x , y = y, x % y   #replace (x, y) with (y, remainder) until remainder is 0 

print(f"The GCD for {a} and {b} is {x} ")   """


#concept - use the euclidean algorithm using repeated modulo 

#program 32
#write a program to find the LCM of two numbers


"""def compute_lcm(x,y):
    if x > y:
     greater = x
    else:
     greater = y
    while(True):
     if ((greater % x == 0)) and ((greater % y == 0)):
       lcm = greater
       break
     greater += 1
    return lcm

num1 = input("Enter number 1 : ")
num2 = int(input("Enter number 2 :"))

print(compute_lcm(num1, num2))  """




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
num2 = int(input("Enter the second number :")   



print("The LCM of num1 and num2 is", compute_lcm(num1,num2))    """

#another way (through GCD)
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while y != 0:
 x, y = y, x % y
# first find the GCD
lcm = a * b // x # // keeps the result an integer
print(f"LCM of {a} and {b} is {lcm}") """

#program 33
#write a program of finding the roots of quadratic equations

"""import math

a = float(input("Enter number 1 : "))
b = float(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))

d = b ** 2 - 4 * a * c

if d > 0:
    root1 = (-b + math.sqrt(d))/ (2 * a)
    root2 = (-b - math.sqrt(d))/ (2 * a)
    print(f"Two real roots : {root1} and {root2}")

elif d == 0:
    root = -b / 2 * a
    print(f"One repeated root : {root}")
else:
    real = -b/ 2 * a
    imag = math.sqrt(-d) / ( 2 * a)
    print(f"complex roots : {real} + {imag}i and {real} - {imag}i") """


#program 34
#write a program to check whether a number is positive,negative or zero 

"""num = int(input("Enter the number: "))

if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is zero")
else:
    print("Number is negative")  """

#program 35
#write a program to check whether a particular program is vowel or constant

"""ch = input("Enter the character : ")

vowels = "aeiou"

if ch.lower() in vowels:
    print("Character is vowel")
else:
    print("character is consonant")  """

#program 36
#write a program to check whether someone is eligible for voting

"""age = int(input("Enter the age : "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting ") """


#program 37
#write a program to print the largest number of the three digits 

"""a,b,c = map(int, input("Enter the numbers : ").split())

if a > b and a > c:
    print("a is greatest")
elif b > a and b > c:
    print("b is greatest")
else:
    print("c is greatest")  """

#program 38
#write a python program to check a leap year

"""year = int(input("Enter the year : "))

if (year%4 == 0) and (year % 100 != 0):
    print("It's a leap year")
elif (year % 400 == 0):
    print("Given year is a leap year")
else:
    print("Given year is not leap year") """



#program 39
#write a program to check whether a given input is digit,alphabet or special character 

"""char = input("Enter a character : ")

if char.isalpha():
    print("Given input is a character")
elif char.isdigit():
    print("Given input is digit")
else:
    print("Given input is special character") """

#program 40
#write a program for a grade calculator


"""marks = int(input("Enter marks (1 - 100) : "))

if marks >= 90:
  print("Grade A")
elif marks >= 80:
  print("Grade B ")
elif marks >= 70:
  print("Grade C")
elif marks >= 60:
  print("Grade D")
elif marks >= 50:
  print("Grade E")
else:
  print("Grade F")  """

#program 41
#write a python program for BMI Calculation 

""" height = float(input("Enter height in meters. :"))
weight = float(input("Enter weight in kgs : "))

bmi = weight/height ** 2

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.5:
    print("Normal")
elif bmi < 29.5:
    print("Overweight")
else:
    print("Obese")   """

#program 42
#write a python program which checks whether it is  divisible by 5 and 11, neither or one of them

"""num = int(input("Enter the number : "))

by5 = (num % 5) == 0
by11 = (num % 11) == 0

if by5 and by11:
    print("Divisbile by both 5 and 11")
elif by5 or by11:
    print("Divsible by either of 5 and 11")
else:
    print("Divisible by neither of them")"""


#program 43
#write a python program to print the season from month number 

"""month = int(input("Enter month number (1-12)"))

if month in (12,1,2):
    print("yeah baby! winter season is here")
elif 3 <= month >= 6:
   print("its spring or idk")
elif 6<= month >=11:
    print("its autumn")
else:
    print("Invalid month number")"""


#program 44
#write a python program to check the type of the triangle 

"""a,b,c = map(int, input("Enter the sides of the triangle : ").split())

if a==b==c:
    print("Given triangle is equilteral triangle")
elif a==b or b ==c or c ==a:
    print("Given triangle is isoceles triangle")
else:
    print("Given triangle is scalene triangle ")"""

#program 45
#write a python program of making a calculator

"""income = float(input("Enter annual income: "))
tax = 0.0
if income > 1000000:
 tax += (income - 1000000) * 0.30 # 30% slab
income = 1000000 # remaining incomefalls in lower slabs
if income > 500000:
 tax += (income - 500000) * 0.20 # 20% slabincome = 500000
if income > 250000:
 tax += (income - 250000) * 0.05 # 5% slabO
print(f"Total tax = Rs. {tax:.2f}")  """





#program 46
#write a python program that print the number from 1 to 20


"""for i in range(1,11):
 print(i)  """


 #program 47
 #write a python program to caculate a multiplication table

"""num = int(input("Enter a number : "))


for i in range(1,11):
  print(f"{num} * {i} = {num * i}") """

#program 48
#write a python program to sum the first natural numbers N

"""num = int(input("Enter the range for N : "))



total = 0

for i in range(1, num+1):
    total += i

print(f"The total sum till{num} is {total}") """

#program 49
#write a python program for reversed counting 

"""for i in range(10, 0 , -1):
    print(i)
print()
"""

#program 50
#wrie a python program to calculate factorial

num = int(input("Enter the range : "))

factorial = 1

for i in range(1, num +1):
    factorial *= i 

print(f"The factorial upto {num} is {factorial}")


