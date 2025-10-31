# import random
# def getRandomNumber():
#     return random.randrange(1,100)
# def give_hint(number,guess):
#     if guess >(number + 10) or guess < (number -10):
#         return "cold"
#     elif number == guess :
#         return "right"
#     else:
#         return "Hot"
# def runGuess():
#     secretNumber = getRandomNumber()
#     while True:
#         user_guess = int(input("Enter the number between 1 and 100:",))
#         hint = give_hint(secretNumber,user_guess)
#         if hint == "right":
#             print("you guessed it right")
#             break
#         else:
#             print(hint)

#     print("-----------game has ended---------")
# if __name__ == '__main__':
#     runGuess()

## project calculator##
# def calculatorDisplay():

#     display = """Welcome to Calculator

# Choose one operation:
# 1. Add
# 2. Subtract
# 3. Product
# """
#     return(display)


# def calculatorFunction(user_choice):
#     if user_choice == 1:
#         print("Let's perform addition")
#         a, b = user_input()
#         output = addition(a, b)
#         return f"The sum is: {output}"
#     elif user_choice == 2:
#         print("Let's perform subtraction")
#         a, b = user_input()
#         output = subtraction(a, b)
#         return f"The difference is: {output}"
#     elif user_choice ==3:
#         a,b = user_input()
#         output = prod(a,b)
#         return f"The product of {a} and {b} is :{output}"


# # Update the user_input(), addition() and subtraction() functions
# def user_input():
#     print("Give two numbers on two lines")
#     a = int(input("Number 1 is: "))
#     b = int(input("Number 2 is: "))
#     return a ,b

# def addition(a, b):
#     return a+b
# def subtraction(a, b):
#     return a-b
# def prod(a,b):
#     return a*b

# if __name__ == '__main__':
#     while True:
#         print(calculatorDisplay())
#         user_choice = int(input("Select the operation: "))
#         value = calculatorFunction(user_choice)
#         print(value)
#         print("do u want to calculate again write yes or no in small case:")
#         a = input()
#         if a =="yes":
#             print("continued")
#         else:
#             print("stopped ")
#             break
# import time
# import sys

# def userChoice(choice):
#     if choice == "1":
#         digital_clock()
#     elif choice == "2":
#         seconds = int(input("Enter the number of seconds to countdown: "))
#         countdown_timer(seconds)
#     else:
#         print("Invalid choice!")

# def digital_clock():
#     """Displays a digital clock."""
#     while True:
#         current_time = time.strftime("%H:%M:%S", time.localtime())
#         print("\rDigital Clock: " + current_time, end = '')
#         time.sleep(1)

# # Solution as follows
# def countdown_timer(seconds):
#     """Counts down from a given number of seconds."""
#     print("Countdown Timer started!")
#     while seconds > 0:
#         print("\rTime remaining: " + str(seconds) + " seconds", end = '')
#         time.sleep(1)
#         seconds -= 1
#     print("\nTime's up!")
# if __name__ == '__main__':
#     while True:
#         choice = input("Choose an option (1:Digital Clock, 2:Countdown Timer): ")
#         userChoice(choice)

# random password
# import random
# import string

# a =  string.ascii_lowercase + string.ascii_uppercase+string.digits+string.punctuation
# n = int(input("Enter  a n value to get how man digits of password:",))
# password = " "
# for i in range(n):
#     password+= random.choice(a)

# print("your random password is:",password)
# rock paper scissors
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

# """
# Function to play the game
# """
# print("Let's play Rock, Paper, Scissors!")
# print("\n")
# n = int(input("How many rounds do you want to play? "))
# count = 1

# # Solution as follows
# while n > 0:
#     print(f"Round: {count}")
#     user_choice = get_user_choice()
#     computer_choice = get_computer_choice()
#     print(f"You chose: {user_choice}")
#     print(f"Computer chose: {computer_choice}")
#     print(determine_winner(user_choice, computer_choice))
#     count = count + 1
#     n = n - 1
# if you_score > computer_score:
#     print("You won the overall match")
# elif you_score < computer_score:
#     print("Computer won the overall match")
# else:
#     print("The match is tied")

# import time
# import random
# def choose_word():
#     words = ['python', 'programming', 'treasure', 'creative', 'medium', 'horror']
#     return random.choice(words)
# def wordDisplay(word, guesses):
#     display_word = ''
#     for char in word:
#         if char in guesses:
#             display_word += char + ' '
#         else:
#             display_word += '_ '
#     return display_word

# def winningCondition(updated_word, turns):
#     # Solution as follows
#     if '_' not in updated_word:
#         result = 1
#         return result
#     if turns == 0:
#         result = 0
#         return result

# if __name__ == '__main__':
#     name = input("What is your name? ")
#     print("Hello, " + name + ", time to play hangman!")
#     time.sleep(1)
#     print("Start guessing...\n")
#     time.sleep(0.5)

#     word = choose_word()
#     turns = len(word)   # number of turns = length of the word to be guessed
#     guesses = ''

#     while turns > 0:
#         print("\nYou have", turns, 'guesses remaining')
#         print(wordDisplay(word, guesses))
#         guess = input("\nguess a character: ").lower()

#         if guess in guesses:
#             print("\nYou have already tried this letter")
#             continue
#         else:
#             guesses += guess

#         if guess not in word:
#             print("\nWrong, Try again")

#         updated_word = wordDisplay(word, guesses)
#         turns -= 1
#         flag = winningCondition(updated_word, turns)

#         if flag == 0:
#             print("\nYou Lose")
#             print("The word was", word)
#         elif flag == 1:
#             print("\nYou won!")
#             print("You guessed", word, "correctly")
#             break
# class Name:
#     def __init__(self):
#         self.name = None
#     @staticmethod
#     def concatenate_names(obj1,obj2):
#         result = Name()
#         result.name = obj1.name +" " "&" " "  +obj2.name
#         return result
# name1 = Name()
# name1.name = "TOM"
# name2 = Name()
# name2.name = "JERRY"
# concatenated_name = Name.concatenate_names(name1,name2)
# print(concatenated_name.name)

#######  image screenshot ############
# import pyscreenshot
# image = pyscreenshot.grab()
# image.show()
# image.save("bunny.png")

# import pyscreenshot
# image = pyscreenshot.grab(bbox=(10,10,500,500))
# image.show()
# image.save("bunny.png")
# import requests
# import xml.etree.ElementTree as ET

# # url of news rss feed
# RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"


# def loadRSS():
#     '''
#     utility function to load RSS feed
#     '''
#     # create HTTP request response object
#     resp = requests.get(RSS_FEED_URL)

#     # return response content
#     return resp.content


# def parseXML(rss):
#     '''
#     utility function to parse XML format rss feed
#     '''
#     # create element tree root object
#     root = ET.fromstring(rss)

#     # create empty list for news items
#     newsitems = []

#     # iterate news items
#     for item in root.findall('./channel/item'):
#         news = {}

#         # iterate child elements of item
#         for child in item:

#             # special checking for namespace object content:media
#             if child.tag == '{http://search.yahoo.com/mrss/}content':
#                 news['media'] = child.attrib['url']
#             else:
#                 news[child.tag] = child.text.encode('utf8')
#         newsitems.append(news)

#     # return news items list
#     return newsitems


# def topStories():
#     '''
#     main function to generate and return news items
#     '''
#     # load rss feed
#     rss = loadRSS()

#     # parse XML
#     newsitems = parseXML(rss)
#     return newsitems

# import demoji

# demoji.download_codes()
# #################################### WEATHER APP ################################################
# from tkinter import *
# import tkinter as tk
# from geopy.geocoders import Nominatim
# from tkinter import ttk,messagebox
# from timezonefinder import TimezoneFinder
# from datetime import datetime
# import requests
# import pytz
# root= Tk()
# root.title("weather App")
# root.geometry("900x500+300+200")
# root.resizable(False,False)
# root.mainloop()
# ######################### GUI##################################
# from tkinter import Tk,Entry,Button,StringVar

# class Calculator:
#     def __init__(self,master):
#         master.title("Calculator")
#         master.geometry("357x420+0+0")
#         master.config(bg="grey")
#         master.resizable(False,False)
#         self.equation = StringVar()
#         self.entry_value = ""
#         Entry(width =17,bg = "#fff",font=("Arial Bold",28),textvariable = self.equation).place(x=0,y=0)

#         Button(width = 11,height = 4,text= "(",relief ="flat",bg = "white",command = lambda:self.show("(")).place(x=0,y=50)
#         Button(width = 11,height = 4,text= ")",relief ="flat",bg = "white",command = lambda:self.show(")")).place(x=90,y=50)
#         Button(width = 11,height = 4,text= "%",relief ="flat",bg = "white",command = lambda:self.show("%")).place(x=180,y=50)
#         Button(width = 11,height = 4,text= "1",relief ="flat",bg = "white",command = lambda:self.show("1")).place(x=0,y=125)
#         Button(width = 11,height = 4,text= "2",relief ="flat",bg = "white",command = lambda:self.show("2")).place(x=90,y=125)
#         Button(width = 11,height = 4,text= "3",relief ="flat",bg = "white",command = lambda:self.show("3")).place(x=180,y=125)
#         Button(width = 11,height = 4,text= "4",relief ="flat",bg = "white",command = lambda:self.show("4")).place(x=0,y=200)
#         Button(width = 11,height = 4,text= "5",relief ="flat",bg = "white",command = lambda:self.show("5")).place(x=90,y=200)
#         Button(width = 11,height = 4,text= "6",relief ="flat",bg = "white",command = lambda:self.show("6")).place(x=180,y=200)
#         Button(width = 11,height = 4,text= "7",relief ="flat",bg = "white",command = lambda:self.show("7")).place(x=0,y=275)
#         Button(width = 11,height = 4,text= "8",relief ="flat",bg = "white",command = lambda:self.show("8")).place(x=180,y=275)
#         Button(width = 11,height = 4,text= "9",relief ="flat",bg = "white",command = lambda:self.show("9")).place(x=90,y=275)
#         Button(width = 11,height = 4,text= "0",relief ="flat",bg = "white",command = lambda:self.show("0")).place(x=90,y=350)
#         Button(width = 11,height = 4,text= ".",relief ="flat",bg = "white",command = lambda:self.show(".")).place(x=180,y=350)
#         Button(width = 11,height = 4,text= "+",relief ="flat",bg = "white",command = lambda:self.show("+")).place(x=270,y=275)
#         Button(width = 11,height = 4,text= "-",relief ="flat",bg = "white",command = lambda:self.show("-")).place(x=270,y=200)
#         Button(width = 11,height = 4,text= "/",relief ="flat",bg = "white",command = lambda:self.show("/")).place(x=270,y=50)
#         Button(width = 11,height = 4,text= "x",relief ="flat",bg = "white",command = lambda:self.show("*")).place(x=270,y=125)
#         Button(width = 11,height = 4,text= "=",relief ="flat",bg = "white",command = self.solve).place(x=270,y=350)
#         Button(width = 11,height = 4,text= "C",relief ="flat",command =self.clear).place(x=0,y=350)

#     def show(self,value):
#         self.entry_value+=str(value)
#         self.equation.set(self.entry_value)

#     def clear(self):
#         self.entry_value= ""
#         self.equation.set(self.entry_value)

#     def solve(self):
#         result = eval(self.entry_value)
#         self.equation.set(result)

# root = Tk()
# calculator = Calculator(root)
# root.mainloop()
################################ drawing rose##############################################
# import turtle


# def draw_flower():
#     turtle.penup()
#     turtle.left(90)
#     turtle.fd(200)
#     turtle.pendown()
#     turtle.right(90)

#     # Flower base
#     turtle.fillcolor("red")
#     turtle.begin_fill()
#     turtle.circle(10, 180)
#     turtle.circle(25, 110)
#     turtle.left(50)
#     turtle.circle(60, 45)
#     turtle.circle(20, 170)
#     turtle.right(24)
#     turtle.fd(30)
#     turtle.left(10)
#     turtle.circle(30, 110)
#     turtle.fd(20)
#     turtle.left(40)
#     turtle.circle(90, 70)
#     turtle.circle(30, 150)
#     turtle.right(30)
#     turtle.fd(15)
#     turtle.circle(80, 90)
#     turtle.left(15)
#     turtle.fd(45)
#     turtle.right(165)
#     turtle.fd(20)
#     turtle.left(155)
#     turtle.circle(150, 80)
#     turtle.left(50)
#     turtle.circle(150, 90)
#     turtle.end_fill()

#     # Petal 1
#     turtle.left(150)
#     turtle.circle(-90, 70)
#     turtle.left(20)
#     turtle.circle(75, 105)
#     turtle.setheading(60)
#     turtle.circle(80, 98)
#     turtle.circle(-90, 40)

#     # Petal 2
#     turtle.left(180)
#     turtle.circle(90, 40)
#     turtle.circle(-80, 98)
#     turtle.setheading(-83)

#     # Leaves 1
#     turtle.fd(30)
#     turtle.left(90)
#     turtle.fd(25)
#     turtle.left(45)
#     turtle.fillcolor("green")
#     turtle.begin_fill()
#     turtle.circle(-80, 90)
#     turtle.right(90)
#     turtle.circle(-80, 90)
#     turtle.end_fill()
#     turtle.right(135)
#     turtle.fd(60)
#     turtle.left(180)
#     turtle.fd(85)
#     turtle.left(90)
#     turtle.fd(80)

#     # Leaves 2
#     turtle.right(90)
#     turtle.right(45)
#     turtle.fillcolor("green")
#     turtle.begin_fill()
#     turtle.circle(80, 90)
#     turtle.left(90)
#     turtle.circle(80, 90)
#     turtle.end_fill()
#     turtle.left(135)
#     turtle.fd(60)
#     turtle.left(180)
#     turtle.fd(60)
#     turtle.right(90)
#     turtle.circle(200, 60)
#     turtle.done()
# draw_flower()

# binary to decimal and decimal to binary###########################################33
# import tkinter as tk


# def convert():
#     if conversion_mode.get() == "decimal_to_binary":
#         decimal_to_binary()
#     else:
#         binary_to_decimal()


# def decimal_to_binary():
#     try:
#         decimal_num = int(input_field.get())
#         binary_num = bin(decimal_num).replace("0b", "")
#         output_label.config(text=f"Binary: {binary_num}")
#     except ValueError:
#         output_label.config(
#             text="Invalid input. Please enter a decimal number.")


# def binary_to_decimal():
#     try:
#         binary_num = input_field.get()
#         decimal_num = int(binary_num, 2)
#         output_label.config(text=f"Decimal: {decimal_num}")
#     except ValueError:
#         output_label.config(
#             text="Invalid input. Please enter a valid binary number.")


# def clear_output():
#     output_label.config(text="")
#     input_field.delete(0, tk.END)


# root = tk.Tk()
# root.title("Binary-Decimal Converter")

# # Variable to store the selected conversion mode
# conversion_mode = tk.StringVar(value="decimal_to_binary")

# # Menu frame for conversion options
# menu_frame = tk.Frame(root)
# menu_frame.pack()

# decimal_to_binary_button = tk.Radiobutton(
#     menu_frame, text="Decimal to Binary", variable=conversion_mode, value="decimal_to_binary")
# decimal_to_binary_button.pack(side=tk.LEFT)

# binary_to_decimal_button = tk.Radiobutton(
#     menu_frame, text="Binary to Decimal", variable=conversion_mode, value="binary_to_decimal")
# binary_to_decimal_button.pack(side=tk.LEFT)

# # Input field
# input_field = tk.Entry(root)
# input_field.pack()

# # Convert button
# convert_button = tk.Button(root, text="Convert", command=convert)
# convert_button.pack()

# # Clear button
# clear_button = tk.Button(root, text="Clear", command=clear_output)
# clear_button.pack()

# # Output label
# output_label = tk.Label(root, text=""imp, pady=10)
# output_label.pack()

# root.mainloop()
# alarm clock####################################################################33
# Import Required Library
# from tkinter import *
# import datetime
# import time
# import winsound
# from threading import *

# # Create Object
# root = Tk()

# # Set geometry
# root.geometry("400x200")

# # Use Threading


# def Threading():
#     t1 = Thread(target=alarm)
#     t1.start()


# def alarm():
#     # Infinite Loop
#     while True:
#         # Set Alarm
#         set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

#         # Wait for one seconds
#         time.sleep(1)

#         # Get current time
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time, set_alarm_time)

#         # Check whether set alarm is equal to current time or not
#         if current_time == set_alarm_time:
#             print("Time to Wake up")
#             # Playing sound
#             winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


# # Add Labels, Frame, Button, Optionmenus
# Label(root, text="Alarm Clock", font=(
#     "Helvetica 20 bold"), fg="red").pack(pady=10)
# Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

# frame = Frame(root)
# frame.pack()

# hour = StringVar(root)
# hours = ('00', '01', '02', '03', '04', '05', '06', '07',
#          '08', '09', '10', '11', '12', '13', '14', '15',
#          '16', '17', '18', '19', '20', '21', '22', '23', '24'
#          )
# hour.set(hours[0])

# hrs = OptionMenu(frame, hour, *hours)
# hrs.pack(side=LEFT)

# minute = StringVar(root)
# minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
#            '08', '09', '10', '11', '12', '13', '14', '15',
#            '16', '17', '18', '19', '20', '21', '22', '23',
#            '24', '25', '26', '27', '28', '29', '30', '31',
#            '32', '33', '34', '35', '36', '37', '38', '39',
#            '40', '41', '42', '43', '44', '45', '46', '47',
#            '48', '49', '50', '51', '52', '53', '54', '55',
#            '56', '57', '58', '59', '60')
# minute.set(minutes[0])

# mins = OptionMenu(frame, minute, *minutes)
# mins.pack(side=LEFT)

# second = StringVar(root)
# seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
#            '08', '09', '10', '11', '12', '13', '14', '15',
#            '16', '17', '18', '19', '20', '21', '22', '23',
#            '24', '25', '26', '27', '28', '29', '30', '31',
#            '32', '33', '34', '35', '36', '37', '38', '39',
#            '40', '41', '42', '43', '44', '45', '46', '47',
#            '48', '49', '50', '51', '52', '53', '54', '55',
#            '56', '57', '58', '59', '60')
# second.set(seconds[0])

# secs = OptionMenu(frame, second, *seconds)
# secs.pack(side=LEFT)

# Button(root, text="Set Alarm", font=(
#     "Helvetica 15"), command=Threading).pack(pady=20)

# # Execute Tkinter
# root.mainloop()
# Import the necessary modules
# import json
# import requests
# from pywebio.input import *
# from pywebio.output import *
# from pywebio.session import *


# def get_fun_fact(_):
#     # Clear the screen
#     clear()

#     # Put HTML content for the fun fact generator header
#     put_html(
#         '<p align="left">'
#         '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
#         '</p>'
#     )

#     # URL from where we will fetch the data
#     url = "https://uselessfacts.jsph.pl/random.json?language=en"

#     # Use GET request
#     response = requests.get(url)

#     # Load the request in json file
#     data = json.loads(response.text)

#     # We will need 'text' from the data
#     useless_fact = data['text']

#     # Put the fact in blue color and increase the font size
#     style(put_text(useless_fact), 'color:blue; font-size: 30px')

#     # Put the "Click me" button
#     put_buttons(
#         [dict(label='Click me', value='outline-success', color='outline-success')],
#         onclick=get_fun_fact
#     )


# # Driver Function
# if __name__ == '__main__':
#     # Put a heading "Fun Fact Generator"
#     put_html(
#         '<p align="left">'
#         '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
#         '</p>'
#     )

#     # Hold the session for a long time and put the "Click me" button
#     put_buttons(
#         [dict(label='Click me', value='outline-success', color='outline-success')],
#         onclick=get_fun_fact
#     )
#     hold()
# import tkinter
# from PIL import Image ,ImageTk
# import random

# root = tkinter.Tk()
# root.geometry('400x400')
# root.title("DataFlair Roll the Dice")
# root.mainloop()
# BlankLine = tkinter.Label(root,text = "")
# BlankLine.pack()

# HeadingLabel = tkinter.Label(root,text="Hello from DataFlair",
#                              fg = "light green",
#                              bg = "dark green",
#                              font = "Helvetica 16 bold italic")
# HeadingLabel.pack()
# dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']

# DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
# ImageLabel = tkinter.Label(root,image= DiceImage)
# ImageLabel.image = DiceImage
# ImageLabel.pack(expand = True)
##########################################################################################################################################################

# import tkinter as tk
# import openai


# # Apply the API Key
# openai.api_key = "YOUR_API_KEY"

# # Generate a response using OpenAI GPT-3


# def generate_response(prompt):
#     completions = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     message = completions.choices[0].text
#     return message

# # GUI interface


# def display_response():
#     input_text = input_field.get()
#     response = generate_response(input_text)
#     output_field.config(state='normal')
#     output_field.delete(1.0, tk.END)
#     output_field.insert(tk.END, response)
#     output_field.config(state='disabled')


# # Create the main window
# root = tk.Tk()
# root.title("OpenAI Chatbot")
# root.geometry("600x700")

# # Create the input field
# input_field = tk.Entry(root, font=("Arial", 14))
# input_field.pack(pady=10)

# # Create the submit button
# submit_button = tk.Button(root, text="Submit", font=(
#     "Arial", 14), command=display_response)
# submit_button.pack(pady=10)

# # Create the output field
# output_field = tk.Text(root, font=("Arial", 14), state='disabled')
# output_field.pack(pady=10)

# # Start the GUI event loop
# root.mainloop()
######################################################################################################
# import pyautogui as pg
# import time

# # Giving Dealy to run program
# print("program will run after 5 second")
# time.sleep(5)
# print("running")

# # Note : after running the program immediately open whatsapp web then open the persons chat you want to send messages

# # For loop
# for i in range(100):
#     # writing the messages
#     pg.write("pilla papalu ala unnaru")


#     time.sleep(0.5)
#     # Seding the messages by pressing enter
#     pg.press("Enter")
##########################################################################################################################################
# Importing the Required Moduel

# import cv2 as cv

# # Reading the image
# image = cv.imread("bunny.jpeg")

# if image is None:
#     print("Error: Image not found. Please check the file path.")
# else:
#     # Converting the Image into grayscale
#     gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#     # Inverting the Image
#     invert_image = cv.bitwise_not(gray_image)

#     # Blur the Image
#     blur_image = cv.GaussianBlur(invert_image, (21, 21), 0)

#     # Invert the Blurred Image
#     invert_blur = cv.bitwise_not(blur_image)

#     # Convert Image into Sketch
#     sketch = cv.divide(gray_image, invert_blur, scale=256.0)

#     # Generating the Sketch Image Named as Sketch4.png
#     cv.imwrite("Sketch4.png", sketch)
#     print("Sketch saved as 'Sketch4.png'.")
# 33######################################################################################################################################3
# import random
# operators = ["+", "-", "/", "*"]
# min_operand = 1
# max_operand = 100
# total_problems = 10


# def generator_problem():
#     left = random.randint(min_operand, max_operand)
#     right = random.randint(min_operand, max_operand)
#     operator = random.choice(operators)
#     exp = str(left)+""+operator+""+str(right)
#     ans = eval(exp)
#     return exp, ans


# exp, ans = generator_problem()
# for i in range(total_problems):
#     exp, ans = generator_problem()
#     while True:
#         guess = input("problem #"+str(i*1)+":"+exp+"=")
#         if guess == str(round(ans)):
#             break
