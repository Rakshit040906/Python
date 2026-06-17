# def avg():
#     a = int(input("Enter the number: "))
#     b = int(input("Enter another number: "))
#     c = int(input("Enter the number again! "))
#     average = (a + b + c)/3
#     print(average)

# avg()
# avg()

## Functions with arguments
# def goodDay(name, ending):
#     print("Good Day, " + name +  ending)
# goodDay("Harry", "Thank You")    

###### "RECURSION" #########
# Q1. WAP using functions to find greatest of three numbers.

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# def greatest(a , b , c):
#     if(a>b and a>c):
#       print("a is  greatest")
#     elif(b>a and b>c):
#        print("b is greatest")
#     elif(c>a and c>b):
#        print("c is greatest")
# greatest(a , b , c)

# ***
# **
# *       for n =3 
# def pattern(n):
#    if (n==0):
#       return 0
#    print("*" * n)
#    pattern(n-1)
   
# pattern(3)
    
# Q7 


# def rem(l, word):
#    n= []
#    for item in l: 
#       if not(item==word):
#          n.append(item.strip(word))
#    return n 
# l = ["Harry", "Rohan", "Shubham", "an"]
# print(rem(l, "an"))


# Q8- Write a python function to print multiplication table of a given number
 
def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")
       
multiply(9)        
    
   
    