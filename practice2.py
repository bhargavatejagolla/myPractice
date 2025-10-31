# import turtle

# # Define the coordinates for the parts of the Iron Man helmet
# part_1 = [
#     [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100),
#      (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],
#     [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40),
#      (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]
# ]

# part_2 = [
#     [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30),
#      (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],
#     [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40),
#      (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]
# ]

# Part_3 = [
#     [(-60, -220), (-80, -240), (-110, -220), (-120, -250),
#      (-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],
#     [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280),
#      (120, -250), (110, -220), (80, -240), (60, -220), (0, -220)]
# ]

# # Set up the Turtle environment
# turtle.hideturtle()
# turtle.bgcolor('black')
# turtle.setup(500, 600)
# turtle.title("Iron Man")

# # Define the initial positions for each part of the drawing
# part_1Goto = (0, 120)
# part_2Goto = (0, -30)
# Part_3Goto = (0, -220)

# turtle.speed(2)

# # Function to draw parts of the Iron Man helmet


# def draw_parts(parts, partsGoto):
#     turtle.penup()
#     turtle.goto(partsGoto)
#     turtle.pendown()
#     turtle.color('red')
#     turtle.begin_fill()

#     for i in range(len(parts[0])):
#         x, y = parts[0][i]
#         turtle.goto(x, y)

#     for i in range(len(parts[1])):
#         x, y = parts[1][i]
#         turtle.goto(x, y)

#     turtle.end_fill()


# # Draw each part of the Iron Man helmet
# draw_parts(part_1, part_1Goto)
# draw_parts(part_2, part_2Goto)
# draw_parts(Part_3, Part_3Goto)

# # Finalize the drawing
# turtle.hideturtle()
# turtle.done()
# import calendar
# year = int(input())
# if calendar.isleap(year):
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")
# is_leap_year = lambda year :(year% 4 ==0 and year%100!=0) or(year%400 ==0)
# year = int(input())
# if is_leap_year(year):
#     print("is a leap year")
# else:
#     print("it is not a leap year")
# num = 15
# flag = 0
# for i in range(2, num):
#     if num % i == 0:
#         flag = 1
#         break
# if flag == 1:
#     print("not prime")
# else:
#     print("is prime")
# num = 7
# flag = 0
# if num <2 :
#     flag = 1
# else:
#     for i in range(2,int(pow(num,0.5))+1):
#         if num%i==0:
#             flag =1
#             break
# if flag == 1:
#     print("it is not prime")
# else:
#     print("It is prime")
# low = int(input())
# high = int(input())
# primes =[]
# for i in range(low,high+1):
#     flag = 0
#     if i<2:
#         continue
#     if i==2:
#         primes.append(2)
#         continue
#     for x in range(2,i):
#         if i%x == 0:
#             flag = 1
#             break
#     if flag ==0:
#         primes.append(i)
# print(primes)
# low = int(input())
# # print(primes)
# high = int(input())
# primes = []
# for i in range(low,high+1):
#     flag = 0
#     if i<2:
#         continue
#     if i==2:
#         primes.append(2)
#         continue
#     for x in range(2,i):
#         if i%x ==0:
#             flag =1
#             break
#     if flag ==0:
#             primes.append(i)
# print(primes)
# number = 371
# num = number
# digit, sum = 0, 0
# length = len(str(num))
# for i in range(length):
#   digit = int(num % 10)
#   num = num/10
#   sum += pow(digit, length)
# if sum == number:
#   print("Armstrong")
# else:
# #   print("Not Armstrong")
# number = 371
# num = number
# sum = 0
# length = len(str(num))
# def checkArmstrong(num,length,sum):
#     if num ==0:
#         return sum
#     sum+=pow(int(num%10),length)
#     return checkArmstrong(num/10,length,sum)
# if checkArmstrong(num,length,sum)==number:
#     print("Armstrong")
# else:
# print("not a armstrong")
# n = int(input("Enter the range value: "))
############################## printing armstrong number########################################################################
# print("Armstrong numbers are:", end=' ')
# for num in range(100, n + 1):
#     sum_of_powers = 0
#     length = len(str(num))
#     temp = num  # Use a temporary variable to preserve the original number

#     while temp > 0:
#         digit = temp % 10
#         sum_of_powers += pow(digit, length)
#         temp //= 10  # Use integer division to discard the last digit

#     if sum_of_powers == num:
#         print(num, end=' ')
######################################## FIBONACCI SERIES IN RANGE #########################################################
# num =10
# n1,n2 = 0,1
# print("fibonacci series:",n1,n2,end=" ")
# for i in range(2,num):
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
#     print(n3,end=" ")
# print()

# def fibonacciSeries(i):


# if i <= 1:
# return i
# else:
# return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

# num = 10
# if num <= 0:
# print("Please enter a Positive Number")
# else:
# print("Fibonacci Series:", end=" ")
# for i in range(num):
# print(fibonacciSeries(i), end=" ")


# import math
# def fibonacci(phi,n):
#     for i in range(0,n):
#         result = round(pow(phi,i)/math.sqrt(5))
#         print(result,end=" ")
# n = 10
# phi = (1+math.sqrt(5))/2
# fibonacci(phi,n)
# r,c = map(int,input().split())
# a = [[input() for j in range(c)] for i in range(r)]
# print(a)
# for i in range(5):
#     for j in range(5):
# a = 1100101011 ^ 111011001 ^ 1110101110
# from ast import mod
# a  = mod(-1)
# print(a)
# a = 2%100
# print(a)
# a = 4
# b =1
# print(a&b)
# from itertools import combinations
# a = [0, 1, 2, 0, 2]
# c = list(combinations(a, 3))
# print(c)
# C = [0] + list(map(int, input().split()))
# print(C)
# a = ['b','u','n','n','y']
# print(a[:2][::-1])
# cook your dish here
# for _ in range(int(input())):
#     n = int(input())
#     s = list(input())
#     g = []
#     for i in range(n):
#         if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
#             g.append(s[:i])
#     print(g)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")


# # Creating and using the linked list
# ll = LinkedList()
# ll.append(3)
# ll.append(2)
# ll.append(4)
# ll.append(5)
# ll.display()
# n = 10
# t = [''] * n  # Initialize the output list;rp
# print(t)
# a = [1,2,3,4,5]
# print(sum(a[:3]))

# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     l = k
#     r = 0
#     b = []
#     while (l!=n+1):
#         c = sum(a[r:l])
#         b.append(c)
#         l += 1
#         r += 1
#     print(b)
# a = [1,2,3,4,5]
# print(sum(a[1:3])
# from itertools import combinations
# print(combinations([0 ,1 ,2 ,0]))
# a= [1,2,2,2,1]
# if 2 and 1 and 0 in a:
#     print("yes")
# def count_subarrays(arr):
#     # Write your code here
#     count = 0
#     count_0 = 0
#     count_1 = 0
#     count_2 = 0
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             count_0 += 1
#         elif arr[i] == 1:
#             count_1 += 1
#         else:
#             count_2 += 1
#     if count_2 == 0 or count_1 == 0 or count_0 == 0:
#         return 0
#     elif count_0 == 1 or count_1 == 1 or count_2 == 1:
#         return 1
#     else:
#         l = 0
#         n = len(arr) - 1
#         while (r != n):
#             r = n+l
#             while (r != n+1):
#                 if (1 and 2 and 0 in arr[l:r]):
#                     count += 1
#                 r += 1
#             l += 1
#         return count
# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(count_subarrays(arr))
# if __name__ == "__main__":
#     main()n = int(input())
# def main():
#     # Write your code here
#     count_1 = 0
#     n = int(input())
#     a = list(map(int, input().split()))
#     l = 0
#     while (a[l]!= 1):
#         if a[l] == 0:
#             a[l] = 1
#         l += 1
#     for i in range(len(a)):
#         if a[i] == 1:
#             count_1 += 1
#     print(count_1)
# if __name__ == "__main__":
#     main()
# from itertools import combinations


# def min_range_combinations(a, b):
#     n = len(a)  # Length of each original array
#     c = sorted(a + b)  # Merge and sort both arrays

#     # Generate all combinations of size n
#     min_range = float('inf')
#     for comb in combinations(c, n):
#         min_range = min(min_range, max(comb) - min(comb))  # Compute range

#     print(min_range)


# # Example input
# a = [2, 1, 3]
# b = [1, 4, 1]
# min_range_combinations(a, b)
# from collections import Counter
# so, st = map(int, input().split())
# s = input()
# t = input()
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = []
#     for i in range(n-1):
#         for j in range(i+2, n):  # Start j from i+2 to ensure non-adjacency
#             sum = a[i] + a[j]
#             b.append(sum)
#     print(max(b))N = 100002
# N =100002
# MOD = 10**9 + 7
# DP = [0] * N
# print(DP)
# t = int(input())

# N = 100002
# MOD = 10**9 + 7
# DP = [0] * N

# for _ in range(t):
#     n, l = map(int, input().split())
#     DP[0] = 1

#     for i in range(1, n + 1):
#         DP[i] = 0
#         for j in range(i - 1, 0, -2):
#             if i - j + 1 <= l:
#                 DP[i] = (DP[i] + DP[j - 1]) % MOD

#     print(DP[:7])
# import pyautogui as pg
# import datetime
# print("wait for 5 seconds")
# for i in range(10):
#     pg.press("Enter")
# a=[3,3,2,4,5,6,7]
# print(a)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")


# # Creating and printing the linked list
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.print_list()
# from collections
# from itertools import combinations

# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     min_sum = float('inf')  # Initialize with a large number
#     for triplet in combinations(a, k):
#         min_sum = min(min_sum, sum(triplet))
#     print(min_sum)
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# mi = []
# l = 0
# r = k

# while r <= n:
#     s = sum(a[l:r])
#     mi.append(s)
#     l += 1
#     r += 1

# print(min(mi))
# cook your dish here
# s = input()
# b = list(s)
# c = set(b)
# print(c)
# alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
# print(alphabet_dict)
# from collections import Counter
# data = ['a', 'b', 'a', 'c', 'b', 'a', 'd', 'c', 'c']
# freq_count = dict(Counter(data))
# print((freq_count))  # Converts Counter to a regular dictionary
