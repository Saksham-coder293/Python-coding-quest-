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

"""num = int(input("Enter the range : "))

factorial = 1

for i in range(1, num +1):
    factorial *= i 

print(f"The factorial upto {num} is {factorial}") """

#program 51
#write a program to print the square the numbers

"""for i in range(1,11):
    print(f"{i:<7}  {i ** 2} ")"""

#program 52
#write a python program to print the sum of even or odd number separately.


"""n = int(input("Enter the range : "))


odd_sum = 0
even_sum = 0
for i in range(1, n+1):
  if i%2 == 0:
     even_sum += i
  else:
     odd_sum += i

print(f"The sum of odd num are {odd_sum}")
print(f"The sum of even num are {even_sum}")  """


#program 53
#write a python program to count digits in a number

"""num = int(input("Enter a number : "))

temp = num
count = 0

while temp > 0:
    count += 1
    temp //= 10

print(f"The number of digits in input are {count}")  """


#program 54
#write a python program to calculate the sum of digits using while loop

"""num = int(input("Enter the number :"))

n = num
sum = 0

while n > 0:
    sum += n%10     # % 10 gives the last digit 
    n //= 10

print(f"the sum of digits in given input are {sum}")   """


#program 55
#write a python program to calculate the sum of the series (harmonic sum)

"""num = int(input("Enter the number : "))

sum = 0

for i in range(1, num + 1):
    sum += 1/i

print(f"The harmonic sum till n is {sum:.4f}")    """


#program 56
#write a python program to reverse a number 

"""num = int(input("Enter the number : "))

n = num
rev = 0 

while n > 0:
    rev = rev * 10 + n % 10    #kind of left side operator
    n //= 10


print(f"The reversed number is {rev}")   """

#program 57
# write a python program to check whether a number is palindrome is not 


"""num = int(input("Enter the number : "))


n = num
rev = 0

while n > 0:
    rev = rev * 10 + n% 10
    n //= 10

if rev == num:
    print("Number is palindrome")
else:
    print("Number is not palindrome")  """

#another way

"""def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome("Saksham")).  """


#program 58
#write a python program to print fibonacci series. 


"""n = int(input("How many terms : "))

a,b = 0,1    #first we will initialise a and b from 0 

for _ in range(n):
  print(a, end = " ")
  a,b = b, a+b
print()    """



#program 59
#write a program to check the prime number 


"""num = int(input("Enter a number : "))

is_prime = num > 1

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
     is_prime = False
     break

if is_prime:
   print(f"{num} is prime")
else:
   print(f"{num} is not prime")   """

#program 60
#write a program to check a number within a given range : 

"""lower = int(input("Enter the lower range : "))
higher = int(input("Enter the higher range : "))

for num in range(max(lower, 2), higher + 1):
    for i in range(2, int(num ** 0.5) +1 ):
        if num % i == 0:
         break

    else:
       print(num, end = " ")

print()
"""

#program 61
#write a program to check whether a number is armstrong is not 

"""num = int(input("Enter the number : "))

total = 0
n = num
digits = len(str(num))


while n > 0:
    total += (n%10) ** digits
    n //= 10

if total == num:
    print("Given number is armstrong")
else:
    print("Given number is not armstrong") """

#program 62
#write a program to check whether a number is perfect number 

"""num = int(input("ENTER THE NUMBER :"))

total = 0
n = num

for i in range(1, num):
    total += (n%i == 0)   #checks how many divisors exist 
    


if total == num:
    print("Given number is a perfect number")
else:
    print("Given number is not perfect number")  """


#Correct solution 

"""num = int(input("Enter a number : "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i


if total == num:
    print("Given number is a perfect number ")
else:
    print("Given number is not perfect number ") """


#program 63
#write a program to check whether a number is strong number or not 

"""num = int(input("Enter a number : "))

temp = num
total = 0


while temp > 0:
    digit = temp % 10   #extracts the remainder of the value
    fact = 1
    for i in range(1, digit + 1):
      fact * i
    total += fact
    temp //= 10   #Divide by 10 and store the value in temp  (removes the last value)

if total == num:
   print("Given number is not a strong number ")
else:
   print("Given number is a strong number")    """



#program 64
#write a python program to compute the greatest common divisor 

"""a = int(input("Enter number a :"))
b = int(input("Enter number b :"))

x,y = a,b
while y != 0:
    x,y = b, a%b

print(f"GCD of {a} and {b} is {x}"). """


#program 65
#write a python program to convert decimal value to binary


"""num = int(input("Enter a number : "))

temp = num
binary = ""

while temp > 0:
  binary = str(temp%2) + binary
  temp //= 2   #divide by 2

print(f"Binary of {num} is {binary}")  """


 

#program 66
#write a python program to convert binary to decimal 

"""bits = input("Enter a binary number : ")
decimal = 0
for bit in bits:
    decimal = decimal * 2 + int(bit)  #shift left then add the new bit 
print(f"Decimal value : {decimal}")  """


#program 67
#write a python program to find the digital root of a number 

"""n = int(input("Enter a number : "))

while n >= 10:
    s = 0
    temp = n
    while temp > 0:
        s += temp%10
        temp //= 10
    n = s
    print("step:",n)
print(f"Digital root : {n}")  """

#program 68 
#write a program to print the collatz sequence

"""n = int(input("Enter a number :"))

steps = 0
while n != 1:
  if n%2 == 0:
    n//= 2
  else:
    3 * n + 1
steps += 1

print(n)
print(f"Steps taken {steps}")"""


#program 69
#write a python program for a number guessing loop

"""import random

ran_num = random.randint(1, 10)
attempts = 0

num = int(input("Enter the number within ( 1 and 10) :"))

attempts += 1

if num > ran_num:
  print("Guess lower")
elif num < ran_num:
  print("Guess Higher")
elif num == ran_num:
  print("Correctly guessed")
else:
  print("Invalid input, please input within a given range "). """



#program 70
#write a python program to print all coordinate pairs (row, col) 

"""size = 3
for row in range(size):
    for col in range(size):
        print(f"({row},{col})", end = "")   """


#program 71
#write a python program to print the right triangle of stars 

"""rows = 5
for i in range(1, rows + 1):
    print("*" * i)
"""

#program 72
#write a python program to print inverted right triangle

"""rows = 5
for i in range(rows, 0, -1):
    print("*" * i) 
    """


#program 73
#write a python program to print right aligned triangles

"""rows = 5
for i in range(1, rows +1):
    print(" " * (rows - i) + "*" * i)"""

#program 74
#write a python program to print the number triangle

"""rows = 5
for i in range(1, rows+1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()  """

#program 75
#write a python program to print the alphabet character 

"""rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(ord("A") + j), end = "")

    print()"""


#program 76
#write a python program to print the floyd's triangle


"""rows = 5
num = 1

for i in range(rows):
    for j in range(i):
        print(num , end = "")
        num += 1
    print()   """


#program 77
#write a python program to print a pyramid

"""rows = 5

for i in range(1 , rows + 1):

 spaces = " " * (rows - i)
 stars = "*" * (2 * i -1)

 print(spaces + stars)  """


#program 78
#write a python program an inverse pyramid


"""rows = 5

for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i -1))"""

#program 79
#write a python program to print a hollow star pattern


"""size = 5

for i in range(size):
    for j in range(size):
   #border rows and column get a star and the rest of the values a space

     if i == 0 or i == size - 1 or j ==0 or j == size - 1:
        print("*", end = "")

    else:
       print(" ", end = "")
    print ()"""


#program 80
#write a python program to print a hollow right triangle


"""rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):

        #first column diagonal, or last row gets a star
        if j == 1 or j == i or i == rows:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()"""
            
#program 81
#write a python program to print the diamond of stars with 9 - stars pyramid followed by a row inverted pyramid

"""rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) +  "*" *(2 * i - 1))      #including the middle  row 

for j in range(rows-1, 0, -1):
    print(" " * (rows - j) + "*" * ( 2 * j - 1))"""


#program 82
#write a python program to print a number pyramid (palindromic rows)

"""rows = 5

for i in range(1, rows+1):
    print( " " * (rows - i), end = "")
    for j in range(1, i + 1):
        print(j, end = "")
    for j in range(i - 1, 0, -1):
        print(j, end = "")
    print() """


#program 83
#write a python program to print pascal's triangle

"""n = 5
for i in range(n):
    val = 1
    row = []
    for j in range(i + 1):
        row.append(str(val))
        val = val * (i - j) // (j + 1).  #next bionomial coeffecient """

#program 84
#write a python program to print the butterfly pattern 

"""n = 4
for i in range(1, n+1):
    print("*" * i + " " * (2 * (n- i)) + "*" * i)

for j in range(n, 0, -1):
    print("*" * j + " " * (2 * (n - j)) + "*" * j)
"""
#program 85
#write a python program to print the zig-zag pattern 


"""rows,cols = 3, 9
for i in range(1, rows + 1):
  for j in range(1,cols + 1):
# stars sit on the diagonals of the wave or themiddle row anchors
     if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
       print("*",end="")
     else:
       print(" ",end="")
  print()"""


#program 86
#write a python program to reverse a string 

"""string1 = input("Enter a string : ")

 
reversed = string1[::-1]

print(f"Reversed string : {reversed}")"""

#program 87
#write a python program to count the number of vowels in a string 

"""input_str = input("Enter a string : ")

vowels = "aeiou"
count = 0


for ch in input_str.lower():
    if ch in vowels:
        count += 1
print(f"Vowels : {count}")"""



#program 88
#write a python program to count the consonant in a given string

"""input_str = input("Enter a string :")

count = 0
vowels = "aeiou"

for ch in input_str.lower():
    if ch not in  vowels:
        count += 1

print(f"The number of consonants are {count}")    """


#program 89
#write a python program to check the palindrome 

"""text = input("Enter the input :")

reversed_text = text[::-1]

if text == reversed_text:
    print("Given string is a palindrome")
else:
    print("Given string is not palindrome")"""

#program 90
#write a python program to coun the words in a sequence

"""sentence = input("Enter the input : ")

words = sentence.split()

print("The mumber of words in a given sentence is: " , len(words))  """

#program 91
#write a python program to to convert lower case into upper case and upper case into lower case

"""sentence = input("Enter the input : ")


result = ""

for ch in sentence:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch   #keep sentences and spaces unchanged 


print(f"The result is {result}")"""

#program 92
#write a python program which counts uppercase and lowercase letters in a word or a sentence



"""input_str = input("Enter a string :")

lower_case = 0
upper_case = 0

for ch in input_str:
    if ch.islower():
        lower_case += 1
    elif ch.isupper():
        upper_case += 1
    else:
        print("Dont enter digit")

print("Upper case :", upper_case)
print("lower case :", lower_case)"""


#program 93
#write a python program to remove all spaces without using replace

"""input_str = input("Enter a string : ")


result_str = ""


for ch in input_str:
    if ch != " ":
        result_str += ch
print(f"The resulting string without spaces are : ", result_str)"""

#program 94
#write a python program to check whether a string is present in another string 

"""text = "programming"
sub = "gram"
found = -1    #not found yet


for i in range(len(text) - len(sub) + 1):  
  if text[i:i + len(sub)] == sub:
        found = i
        break  



if found == -1:
     print("Substring not found")
else:
    print("Found at index", found)         
"""


#program 95
# Write a python program to replace a substring without replace                         


"""text = "the cat sat on the cat mat"
old = "cat"
new = "dog"
result = ""
i = 0
while i < len(text):
  if text[i:i + len(old)] == old:
     result += new
     i += len(old) # jump past the matched word
  else:
    result += text[i]
    i += 1
print(result)
"""

#program 96
#write a python program to capitalize each word without title()

"""sentence = input("Enter a sentence : ")

words = sentence.split()

capitalized = []

for word in words:
  capitalized.append(word.upper[0] + word[1:])

print(" ".join(capitalized))  """

#program 97
#write a program to count the frequency of every item 

"""str = input("Enter a sentence :")

freq = {}
for ch in str:
  freq[ch]  = freq.get(ch, 0)

for ch, count in freq.items():
  print(ch, " > "<count)  """

#program 98
#write a python program for removing duplicates

"""input_str = input("Enter a string :")
result = ""

for ch in input_str:
  if ch not in result:
    result += ch

print("The final string is ", result)"""

#program 99
#write a python program to check whether the two string are anagram or not 


"""s1 = input("Enter a string : ").lower()
s2 = input("Enter another string :").lower()

if sorted(s1) == sorted(s2):
    print("They are anagrams")
else:
    print("They are not anagrams")"""

#program 100
#write a python program to print the longest word in a sentence

"""sentence = input("Enter the sentence :")


longest = ""
for word in sentence.split():
    if len(word) > len(longest):
        longest = word
print("Longest word : ",longest)  """

#program 101
#write a python program to print the acronym generator
#acronym = first letter of each word to be capital 

"""input_str = input("Enter the string : ")
acronym = ""

for words in input_str.split():     #indexing the first letter of each character
 acronym += words[0].upper()

print("The acronym are ", acronym)"""



#program 102
#write a python program to print the first non-repeating character. #find the first character in a string that appears exactly once 


"""text = input("Enter a string : ")
freq = {}

for ch in text:
    freq[ch] = freq.get(ch,0) + 1
    answer = None

   
for ch in text:
    if freq[ch] == 1:
        answer = ch
        break


if answer is None:
    print("No non repeating character")
else:
    print("Th first non repeating character is", answer)
"""

#program 103
#write a python program to print pangram check 
#it contains each and every alphabet from A to Z at least once 

"""sentence = input("Enter the input sentence :")
letters = set()

for words in sentence:
    if words.isalpha():
        letters.add(words)
if len(letters) == 26:
     print("The sentence is panagram")
else:
    print("The sentence is not panagram")    """


#program 104
#write a python progrtam to remove the punctuation 

"""text = input("Enter the input string :")

result = ""
for ch in text:
    if ch.isalnum() or ch == " ":
        result += ch
  
print("The cleaned text is", result)   """


#program 105
#write a python program to print caesar cipher 
#encrypt a message by shifting every letter forward by a given number of places in the alphabet



"""text = input("Enter a message: ")
shift = int(input("Enter shift: "))
result = ""

for ch in text:
 if ch.isupper():
# ord() gives the character code; % 26 wraps zback to a
    result += chr((ord(ch) - ord("") + shift) % 26 +ord(""))
 elif ch.islower():
    result += chr((ord(ch) - ord("a") + shift) % 26 +ord("a"))
 else:
    result += ch
print("Encrypted:", result)
"""


#program 106
#write a python program to check string rotation 

"""s1 = "abcde"
s2 = "cdeab"


if len(s1) == len(s2) or s2 in s1 + s1:
    print("The string is rotated")
else:
    print("The string is not rotated")"""


#program 107
#write a python program to find the longest common prefix


"""words = ["flower", "flow", "flight"]

prefix = words[0]

while not words.startswith(prefix):
    prefix = prefix[:-1]
    if prefix == "":
        break

if prefix:
    print("The longest common prefix is", prefix)
else:
    print("No longer prefix exists"). """


#LISTS
#program 108
#write a python program to find the maximum element without using max() 


"""numbers =[23,45,67,83,22]

largest = numbers[0]


for n in numbers:
    if n > largest:
        largest = n

print("The largets number in list of numbers is", largest)     """


#program 109
#write a python program to find the minimum element in the list

"""numbers =[23,45,67,83,22]

smallest = numbers[0]


for n in numbers:
    if n < smallest:
        smallest = n

print("The largets number in list of numbers is", smallest)    """


#program 110
#write a python program to compute the sum and average of a list of numbers without using sum and average

"""numbers = [10,20,30,40]

sum = 0

for n in numbers:
    sum += n

average = sum/len(numbers)

print(f"The average of numbers are ", average)      """

#pprogram 111
#write a python program to print the linear search 

"""numbers = [3,5,6,9,4]
target = 9
index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        index = i
        break

print(f"The index for", target,"is",index)  """


#program 112
#write a python program to count the occurences of a value without using count operator ()


"""numbers = [4,5,2,2,2,3,4,2]

target = 2
count = 0

for n in numbers:
    if n == target:
        count += 1

print(f"{target} appears {count} times.")    """

#program 113
#write a python program to print the list of squares 

"""list = [1,5,6,8,3,4]


squares = [n ** 2 for n in list]

print(f"Thje square of given list is", squares)
"""

#program 114
#write a python program to reverse a list in a place 

"""numbers = [1,2,3,4,5]

left = 0
right = len(numbers) - 1
while left < right:
    numbers[left], numbers[right] = numbers[right],numbers[left]
    left += 1
    right -= 1
print("Reversed:", numbers)        """
#Two pointer swapping for both -ends 


#program 115
#write a python program to check if a list is sorted 

"""
def is_sorted(num):

    for i in range(len(num) - 1):
      if num[i] > num[i + 1]:
         return False
    return True

print(is_sorted([1,3,5,7]))
print(is_sorted([4,7,9,6,7]))

"""
#program 116
#write a python program to find the second largest element 


"""numbers = [10, 40, 30, 40, 20]
largest = None
second = None
for n in numbers:
  if largest is None or n > largest:
   second = largest # old largest becomes second
   largest = n
  elif n != largest and (second is None or n > second):
   second = n

print("Second largest:", second)       """


#program 117
#write a python program to remove duplicates

"""numbers = [1,2,2,2,3,3,3,5,5]
unique = []

for n in numbers:
  if n not in unique:
    unique.append(n)

print(f"The updated list is {unique}")  """


#program 118
#write a python program to split the list into odd list and even list 


"""list = [1,2,3,4,5,6,7,8,9]

even_list = []
odd_list = []

for n in list:
    if n%2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)

print(f"Odd list is {odd_list}")
print(f"Even list is {even_list}")    """


#program 119
#write a python program to print the cumulative sum of number in the list

"""list = [1,2,3,6]


running = 0
cumulative = []

for n in list:
    running += n
    cumulative.append(n)
print("Cumulative sum :", cumulative)"""


#program 120
#write a python program to remove all occurences in a list


"""list_1 = [1,2,2,3,4,4,4,5,5]
value = 4

removal = [n for n in list_1 if n != value]

print(f"The final list after removal is ", removal)     """


#program 121
#write a python program to print the common elements of two lists

"""list1 = [1,2,3,4]
list2 = [3,4,5,6]

common = []


for x in list1:
    if x in list2 and x not in common:
        common.append(x)

print(f"list with common  elements is {common}")    """

#program 122
 #write a python program to add two lists 

"""list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]


union_list = []


for x in list1 + list2:
    if x not in union_list:
        union_list.append(x)

print(f"The updated list is {union_list}")    """


#program 123
#write a python program to find the duplicate items


"""numbers = [1, 2, 3, 2, 4, 1, 5]
seen = set()
duplicates = []
for n in numbers:
  if n in seen and n not in duplicates:
    duplicates.append(n) # second time we meet n
  seen.add(n)

print("Duplicates:",duplicates)   """


#program 124
#write a python program to find the missing number


"""numbers = [1,2,4,5,6]
n = 6


total = n * (n + 1) // 2

actual = sum(numbers)

missing = total - actual

print(f"Missing value is {missing}")     """


#program 125
#write a python program to move zeros to the end 


"""numbers = [0,4,0,2,0,1,0,0]

non_zero = [n for n in numbers if n != 0]

no_of_zeros = len(numbers) - len(non_zero)

result = non_zero + [0] * no_of_zeros


print(f"zeros at the end are", result)     """