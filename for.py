fibbonaci Series 
# a = 0
# b = 1
# print(a , b, end = " ")
# for _ in range(8):
#     next_term = a + b
#     print(next_term, end=" ") 
#     a,b = b,next_term 

# Factorial of a number   
# fact = 1
# for i in range(1,6):
#     fact = i*fact 
# print("",fact)

 
# age=25
# print(type(age))
# age_str=str(age)
# print(age_str)
# Continue
#it skips the current iteration
# for i in range(10):
#     if i%2==0:
#         continue 
#     print(i)
#

#Pass statement is a null opeation, it does nothing.
# for i in range(5):
#    if i==3:
#       print("NO")
#       pass
#    print(i)


### NESTED LOOPS ###
# for i in range(3):
#     for j in range(2):
#         print(f"i:{i} and j:{j}")

### WHILE LOOP ###
# n=10
# sum=0
# count=1
# while count<=n:
#     sum=sum+count
#     count=count+1
# print("Sum of first ten natural numbers:",sum)

### PRIME NUMBERS BETWEEN 1 AND 100 ###
# for num in range(1,101):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)





















# for num in range(1,101):
#     if num>1:
#        for i in range(2,num):
#            if num%i==0:
#                break
#        else:
#           print(num)

# n = int(input("Enter N: "))
# for i in range(n):
#     print(" * " * n)

#### Q1 Print sum of numbers from 1 to 10
# sum = 0
# for i in range(1,11):
#     sum = sum + i 
#     print(sum) 
#### Q2 sum of first N nu  mbers 
# N = int(input("Enter the number")) 
# sum = 0
# for i in range(1,N):
#     sum = sum + i
#     print(sum)

#### Print Table of 5 
# for i in range(1,6):
#     i = i*5
#     print(i)

#### Count digits in a number 
# num = 12345
# count = 0
# while num > 0:
#     num = num//10
#     count = count + 1
# print(count)


### revese a number
# num = 12345 
# reverse = 0 
# while num > 0: 
#     digit = num % 10
#     reverse = reverse * 10 + digit 
#     num = num // 10
#print(reverse) 
##### num =1234 
# num = 1234 
# reverse = 0
# while num > 0:
#     digit = num % 10 
#     reverse = reverse * 10 + digit 
#     num = num // 10
# print(reverse)

####check whether the number is prime or not
# num = int(input("Enter a number: "))
# for i in range(2,num):
#     if(num % i == 0):
#         print("not prime")
#         break
# else:
#      print("prime")

#### Factorial series 
# n = int(input("Enter the number"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)
 
### Star pattern 
# n = int(input("Enter the number : "))
# for i in range(1,n+1):
#     print("*"*i)

## Floyd's Triangle 

  


###### Amstorng number
# num = 153 
# temp = num 
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** 3
#     temp = temp // 10  
# if (sum == num):
#     print("Amsrong")
# else:
#     print("Not Amstrong")






### Find the area of the circle 
# variable = input("Enter the r or d: ")
# if variable == "r":
#       r = int(input("Enter the radius "))
#       if r <= 0:
#         print("area cant be calculated!")
#       else:
#        area = 3.14*r**2
#        print(area)
# elif variable == "d":
#     d = int(input("Enter the number"))
#     area = 3.14*d**2/4 
#     print(area)
# else: 
#    ("invalid choice!")

### Find the volume of 3D shapes
# Shape = input("Enter the shape: ")
# if Shape == "Cube":
#     s = int(input("Enter the side: "))
#     v = s**3
#     print(v)
# elif Shape == "Cylinder":
#     r = int(input("Enter the radius: "))
#     h = int(input("Enter the height: "))
#     v = 3.14*r**2*h 
#     print(v)
# elif Shape == "Cone":
#     r = int(input("Enter the radius: "))
#     h = int(input("Enter the height: "))
#     v = 1/3 * 3.14 * r**2 * h
#     print(v)
# else:
#     print("Invalid Choice!")

# n = int(input("Enter the number"))
# def fib(n):
#     if n <= 1:
#         print("Invalid")
#     else:
#         return fib(n-1) + fib(n-2)


# num = 12345
# count = 0
# while num > 0:
#     num = num//10
#     count += 1
# print(count)

# num = 12345 
# reverse = 0
# while num>0:
#     digit = num%10
#     reverse = reverse*10 + digit
#     num = num//10
# print(reverse)
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1,n+1):
#         fact *= i 
# print(fact)   
# num = 153 
# temp = num
# sum = 0 
# while num>0:
#     digit = temp%10
#     sum += digit**3 
#     temp = temp//10
# if sum == num:
#     print("Amstrong")
# else:
#     print("Not Amstrong")


#### Palindrome 
# num = (int(input("Enter the number: ")))
# reverse = 0
# temp = num
# while temp>0:
#     digit = temp%10
#     reverse = reverse*10 + digit
#     temp = temp//10
# if(num == reverse):
#     print("palindrome")
# else:
#     print("palindrome")

# import numpy as np 
# print("Numpy successfully installed! Version:",np.__version__)


















num = 232
temp = num 
reverse = 0
while temp>0:
    digit = temp%10
    reverse = reverse*10 + digit
    temp = temp//10
if num == reverse:
        print("Palindrome")
else:
    print("Not palindrome")

 
      


    