#program 1
#print the sum of two numbers

a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 : "))


print("Sum of two number is", a + b)


#program 2
#write a program to swap two variable using temp variable

a = 10
b = 5

print("Before swap", "a = ", a, "b = ", b)

temp = a
a = b
b = temp

print("after swap", "a = ", a, "b = ", b)


#program 3
#write a program to swap two variables without using temp variables

a = 10
b = 5

a , b = b, a

print("After swapping variables", "a = ", a, "b = ", b)


