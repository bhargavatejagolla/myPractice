# import random
# you_score = 0
# computer_score = 0
# def get_user_choice():
#     """
#     Function to get user's choice (rock, paper, or scissors)
#     """
#     while True:
#         user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
#         if user_choice in ['rock', 'paper', 'scissors']:
#             return user_choice
#         else:
#             print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

# def get_computer_choice():
#     """
#     Function to randomly generate computer's choice
#     """
#     return random.choice(['rock', 'paper', 'scissors'])

# def determine_winner(user_choice, computer_choice):
#     """
#     Function to determine the winner of the game
#     """
#     global you_score, computer_score
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#          (user_choice == 'paper' and computer_choice == 'rock') or \
#          (user_choice == 'scissors' and computer_choice == 'paper'):

#         you_score = you_score + 1
#         return "Congratulations! You win this round!"
#     else:
#         computer_score = computer_score + 1
#         return "Computer wins this round!"

# def overall_winner(you_score, computer_score):
#     # Solution as follows
#     if you_score > computer_score:
#         return("You won the overall match")
#     elif you_score < computer_score:
#         return("Computer won the overall match")
#     else:
#         return("The match is tied")
# """
# Main code
# """
# if __name__ == '__main__':
#     print("Let's play Rock, Paper, Scissors!")
#     print("This game is the best of 3!")
#     print("\n")

#     n = 0
#     while n < 3:
#         print(f"Round: {n+1}")
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()
#         print(f"You chose: {user_choice}")
#         print(f"Computer chose: {computer_choice}")
#         print(determine_winner(user_choice, computer_choice))
#         n = n + 1

#     print("\n")
#     print(overall_winner(you_score, computer_score))
# s_m = ['a','b','c','d','e','f']
# for index, value in enumerate(s_m):
#     print(index,value)
# arr = [1,5,3,2,4,67,3]
# for i in range(len(arr)):
#     if arr[i-1] > arr[i+1]:
#         arr[i+1],arr[i] = arr[i],arr[i+1]


# print(arr)
# import time
# import pyautogui as pg

# # Giving Dealy to run program
# print("program will run after 5 second")
# time.sleep(5)
# print("running")


# for i in range(100):
#     # writing the messages
#     pg.write("hello Ash")
#     time.sleep(0.5)
#     # Seding the messages by pressing enter
#     pg.press("Enter")
# import re
# text = 'The quick brown fox jumps over the lazy dog'
# pattern = r'\b\w{5}\b'
# matches = re.findall(pattern, text)
# print(len(matches))
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.pop('b', 0) + my_dict.get('d', 4))
# numbers = [1,2,3,4,5]
# result = list(map(lambda x : x*x,numbers))
# print(result)
# import datetime
# print(datetime.now(tz = timezone('America/New_York')))
# print("hello world")
# n = int(input("Enter the number to generate prime numebrs:",))
# flag = 1
# j=2
# for i in range(2,n):
#     while(i>j*j):
#         if(i%j==0):
#             flag = 0
#         j += 1
#     if(flag==1 ):
#         print(i)
# n =  int(input())
# a  =[]
# i = 2
# while(i<=n):
#     if(n%i==0):
#         a.append(i)
#         n//=i
#     i+=1
# print(*a)
# def factor(n):
#     ret = []
#     i = 2
#     while i * i <= n:
#         while n % i == 0:
#             ret.append(i)
#             n //= i
#         i += 1
#     if n > 1:
#         ret.append(n)
#     return ret
# print(factor(12))
# cook your dish here
# for _ in range(int(input())):
#     r, s = map(int, input().split())
#     a = set()
#     b = set()
#     for i in range(1, r+1):
#         if r % i == 0:
#             a.add(i)
#     for i in range(1, s+1):
#         if s % i == 0:
#             b.add(i)
#     if len(a)>len(b):
#         print(len(a))
#     else:
import math
#         print(len(b))         
# print(int(math.sqrt(2)+1))