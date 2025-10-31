# def check_positive_or_negative():
#     a = int(input("Enter a number to check whether it is positive or not: "))
#     if a > 0:
#         print("The entered number is positive.")
#     elif a < 0:
#         print("The entered number is negative.")
#     else:
#         print("The entered number is zero, which is neither positive nor negative.")

# check_positive_or_negative()

# a = int(input("Enter a number to check whether it is even or odd : "))
# def check_even_or_odd(a):
#     if a % 2 == 0:
#         print("The entered number is even.")
#     else:
#         print("The entered number is odd.")
        
#         return check_even_or_odd(a )

#sum of n natural numbers 
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(f"The sum of first {i} natural numbers is: {sum}")

#greatest of two numbers
# input_1 = int(input("Enter the first number: "))
# input_2 = int(input("Enter the second number: "))
# if input_1 > input_2:
#     print(f"The greatest number is {input_1}")
# else:
#     print(f"The greatest number is {input_2}")    

#greatest of three numbers
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# if a > b and a > c:
#     print(f"The greatest number is {a}")
# elif b > a and b > c:
#     print(f"The greatest number is {b}")
# else:
#     print(f"The greatest number is {c}")

#leap yr or not
# a = int(input("Enter a year to check if it is a leap year: "))

# if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#     print(f"{a} is a leap year.")
# else:
#     print(f"{a} is not a leap year.")

# # to check if a number is prime
# def is_prime(a):
#     if a <= 1:
#         return False
#     if a <= 3:
#         return True
#     if a % 2 == 0 or a % 3 == 0:
#         return False
#     i = 5
#     while i * i <= a:
#         if a % i == 0 or a % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# a = int(input("Enter a number to check if it is prime: "))
# if is_prime(a):
#     print(f"{a} is a prime number.")
# else:
#     print(f"{a} is not a prime number.")

##reverse a number
# a = int(input("Enter a number to reverse: "))

# print(f"Reversed number: {int(str(a)[::-1])}")

# palindrome_check = input("Enter a string to check if it is a palindrome: ")

# def is_palindrome(s):
#     return s == s[::-1]
# if is_palindrome(palindrome_check):
#     print(f"{palindrome_check} is a palindrome.")
# else:
#     print(f"{palindrome_check} is not a palindrome.") 

#finding the fibonacci sequence up to nth termin
#second method to reverse a number
# num = int(input("Enter a number to reverse: "))
# temp = num 
# reverse = 0
# while num > 0:
#     remainder = num % 10
#     reverse = reverse * 10 + remainder
#     num = num // 10
# print(f"Reversed number: {reverse}")   
#factorial of a number
# n =input("Enter a number to calculate its factorial: ")
# i =1  
# for n in range(1, int(n) + 1):
#     i *= n
# print(f"The factorial of {n} is: {i}")    
# another method to calculate factorial is 
# def getfactorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * getfactorial(n - 1)
# num = input("Enter a number to calculate its factorial: ")
# print(f"The factorial of {num} is: {getfactorial(int(num))}")

# perfect number

# def perfect_number(num):
#     if num <0:
#         False
        
#     sum = 0
#     for i in range(1, num):
#         if num%i ==0:
#             sum+=i
# num = int(input("Enter a number to check if it is perfect: "))            
# if sum == num:
2
# else:
#     print(f"{num} is not a perfect number")               

# pairs method
# 
# a =int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print(a**b)
#automorphic number
# n = input("Enter a number to check if it is automorphic: ")
# 
# a =  pow(int(n), 2)
# if a% 10 ==int(n):
    # print(f"{n} is an automorphic number.")
# else:
#     print(f"{n} is not an automorphic number.")

#harshad number
# n = input("Enter a number to check if it is harshad: ")
# 
# sum =0 
# for digits in str(n):
    # sum += int(digits)
    # 
# if int(n) % sum == 0:
    # print(f"{n} is a harshad number.")
# else:
    # print(f"{n} is not a harshad number.")    

#abundant number
# n = input("Enter a number to check if it is abundant: ")
# sum = 0
# for factor in range(1, int(n/2)):
    # if n % factor == 0:
        # sum += factor
# print()
# 
#highest common factor
# num1 = int(input("enter the number 1 to find its hcf:",))
# num2 = int(input("enter the number 2 to find its hcf:",))
# for i in range(1,min(num1,num2)):
    # if num1%i ==0 and num2 % i ==0:
        # hcf =i
# print(f"hcf of {num1},and {num2}is ,{hcf}")    
# 2nd methid to finf the hcf
# num1 = int(input("enter the number 1 to find its hcf:",))
# num2 = int(input("enter the number 2 to find its hcf:",))
# while num1!=num2:
    # if num1>num2:
        # num1-=num2
    # else:
        # num2 -=num1
# print(f"hcf of {num1} and {num2} is {num1}")
# method 3

# to etermine the lcm of the number

# Taking input from the user for num1 and num2
# Taking input from the user for num1 and num2
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# 

# start = max(num1, num2)  # Starting point is the larger of num1 or num2
# end = num1 * num2 + 1    # Ending point is 1 more than the product of num1 and num2


# for i in range(start, end):
    # if i % num1 == 0 and i % num2 == 0:
        # lcm = i
        # break
# 

# print(f"The LCM of {num1} and {num2} is {lcm}")
# method 3
# num1 = 12
# num2 = 14
# for i in range(1,max(num1,num2)):
    # if num1%i ==num2%i ==0:
        # hcf =i
# lcm = (num1*num2)//hcf  
# print()     
# def getHcf(num1,num2):
    # while num1!=num2:
        # if num1>num2:
            # num1-=num2
        # else:
            # num2-=num1
    # return num1        
# num1 = 12
# num2 =14
# hcf =getHcf(num1,num2)
# lcm = (num1*num2)//hcf
# print(f"lcm of{num1} and {num2} is {lcm}")                

# from math import sqrt
# def isPerfectSquare(x):
#     if x >=0:
#         s = int(sqrt(x))
#         return(s*s)==x
#     return False 
# n = int(input())
# if isPerfectSquare(n):
#     print("true")
# else:
#     print("false")    

# import math
# def checkPerfectSquare(x):
#     if(math.ceil(math.sqrt(n))) == math.floor(math.sqrt(n)):
#         print("true")
#     else:
#         print("false")
# n =int(input())
# print(math.sqrt(n)) 
# checkPerfectSquare(n) 

# import math
# def findRoots(a, b, c):
#     if a==0:
#         print("invalid")
#         return -1
#     d = b**2 - 4*a*c
#     sqrt_val = math.sqrt(abs(d))
#     if d > 0:
#         print("Two distinct real roots exist.")
#         print("root1 : ", (-b + sqrt_val) / (2*a))
#         print("root2 : ", (-b - sqrt_val) / (2*a))
#     elif d ==0:
#         print("Two equal and real roots exist.")
#         print("root1 : root2 : ", -b / (2*a))
#     else:
#         print("Two distinct and complex roots exist.")
#         print("root1 : ", (-b + sqrt_val) / (2*a))
#         print("root2 : ", (-b - sqrt_val) / (2*a))
#         print("Imaginary part : ", sqrt_val / (2*a)) 

# a =1 
# b = 4
# c = 4
# findRoots(a, b, c) 
# n = int(input("Enter a number: "))
# divisors = []

# # Iterate from 1 to n and find divisors
# for i in range(1, n + 1):
#     if n % i == 0:
#         divisors.append(i)

# # Print the divisors
# print(f"The divisors of {n} are:", divisors)

# method 2
# number =100
# divisor = 2
# count =0 
# for i in range(1, number + 1):    the ............................................
#     count_factors = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count_factors += 1
#         else:
#             pass
#     if count_factors == divisor:
#         count+=1
        
# print(count)                   
    
# digits = int(input("Enter a number: "))
# def Convert_to_string(digits):
#     a = str(digits)
#     print(a)    
# Convert_to_string(a)


















    
    

    
    
    