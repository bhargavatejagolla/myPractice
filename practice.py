# print("normal pyramid")
# n = int(input("Enter the range to print the pyramid:"))
# for i in range(n):
#     x = " *"
#     x = x*i
#     print(f"{x:^40}")
# n = int(input())
# for i in range(n):
#     x ="* "
#     x=x*(n-i)
#     print(f"{x:^20}")
# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# # Using the generator function
# gen = my_generator()

# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3
# import threading
# import time
# # Shared flag
# stop_flag = False
# def my_thread_function():
#     while not stop_flag:
#         # Thread's main task
#         time.sleep(1)  # Simulate some work
# # Create and start the thread
# my_thread = threading.Thread(target=my_thread_function)
# my_thread.start()
# # Interrupt the thread
# stop_flag = True
# import threading
# import time

# # Create an event object
# stop_event = threading.Event()

# def my_thread_function():
#     while not stop_event.is_set():
#         # Thread's main task
#         time.sleep(1)  # Simulate some work

# # Create and start the thread
# my_thread = threading.Thread(target=my_thread_function)
# my_thread.start()

# # Interrupt the thread
# stop_event.set()
# import threading
# import time
# def my_thread_function():
#     while True:
#         pass
# my_thread = threading.Thread(target = my_thread_function)
# my_thread.start()
# my_thread.join()
# import os

# def user_function():
#     # Define the directory path
#     directory_path = "/mnt/codechef"

#     # List the files and directories inside "/mnt/codechef"
#     files = os.listdir(directory_path)

#     # Check if there are any files or directories
#     if files:
#         # Iterate through each file or directory and print its name
#         for file_name in files:
#             print(file_name)


# def main():
#     directory_path = "/mnt/codechef"
#     file_path = "/mnt/codechef/input.txt"

#     # Create the directory if it doesn't exist
#     if not os.path.exists(directory_path):
#         try:
#             os.makedirs(directory_path)
#             print("Directory created successfully.")
#         except OSError:
#             print("Failed to create the directory.")
#             return

#     # Write numbers from 1 to 5 into the file
#     try:
#         with open(file_path, 'w') as file_writer:
#             for i in range(1, 6):
#                 file_writer.write(str(i) + "\n")
#     except IOError:
#         print("Failed to create the file.")
#         return

#     user_function()

# if __name__ == "__main__":
#     main()
# import threading
# import time
# stop_thread = threading.Event()
# def worker():
#     while not stop_thread.is_set():
#         print("Working")
#         time.sleep(1)
#     print("thread stopped")
# thread = threading.Thread(target = worker)
# thread.start()
# time.sleep(5)
# stop_thread.set()
# thread.join(timeout=3)
# if thread.is_alive():
#     print("thread is still running after time out")
# else:
#     print("thread has stopped")
# import threading
# import time

# # Shared flag
# stop_flag = False

# def my_thread_function():
#     print("Thread started.")
#     while not stop_flag:
#         print("Thread is doing some work...")
#         time.sleep(0.01)  # Simulate some work
#     print("Thread stopped.")

# # Create and start the thread
# my_thread = threading.Thread(target=my_thread_function)
# my_thread.start()

# # Simulate some other work in the main thread
# time.sleep(0.05)

# # Interrupt the thread by setting the stop flag
# print("Interrupting the thread.")
# stop_flag = True

# # Wait for the thread to complete
# my_thread.join()
# print("Main thread: Thread has completed.")
# import threading
# import time

# # Create an event object
# stop_event = threading.Event()

# def my_thread_function():
#     while not stop_event.is_set():
#         print("Thread is running...")
#         time.sleep(0.01)  # Simulate some work

# # Create and start the thread
# my_thread = threading.Thread(target=my_thread_function)
# my_thread.start()

# # Wait for 50 milliseconds
# time.sleep(0.05)

# # Set the event to interrupt the thread
# print("Interrupting the thread...")
# stop_event.set()

# # Wait for the thread to finish
# my_thread.join()

# print("Main thread: Done!")
# import threading
# import time
# def my_thread_function():
#     print("thread started..")
#     time.sleep(0.005)
#     print("thread finished")
# my_thread = threading.Thread(target = my_thread_function)
# my_thread.start()
# my_thread.join(timeout=0.003)
# print("main thread continued..........")
# my_thread.join()
# print("main thread:Done!!!")
# def fibonacci_generator():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b

# n = int(input())
# fib_gen = fibonacci_generator()
# for i in range(n):
#     print(next(fib_gen))/
# import threading
# import time

# # Global list to store integers
# integer_list = []

# # Flag to indicate whether the thread should stop
# stop_flag = False

# Thread function for inserting elements into the list
# def insert_thread():
#     global stop_flag
#     try:
#         while len(integer_list) < 5 and not stop_flag:
#             # Insert an element into the list
#             integer_list.append(len(integer_list) + 1)
#             print("Inserted:", len(integer_list))
#             # Simulate some work between insertions
#             time.sleep(0.005)  # 5 ms
#     except KeyboardInterrupt:
#         print("InsertThread interrupted.")
#     finally:
#         print("InsertThread stopped.")


# # Create and start the InsertThread
# insert_thread_instance = threading.Thread(target=insert_thread)
# insert_thread_instance.start()

# try:
#     # Monitor the size of the list
#     while len(integer_list) < 5:
#         time.sleep(1)  # Check every second
#     # Set the stop flag to True to interrupt the InsertThread
#     stop_flag = True
#     # Wait for the InsertThread to complete its execution
#     insert_thread_instance.join()

# except KeyboardInterrupt:
#     print("Main thread interrupted.")

# import threading
# import time
# variable = 0
# lock = threading.Lock()

# def increment():
#     global variable
#     for _ in range(5):
#         lock.acquire()
#         variable+=1
#         lock.release()
# threads = []
# for _ in range(6):
#     thread = threading.Thread(target= increment)
#     thread.start()
#     threads.append(thread)
# for thread in threads:
#     thread.join()
# print(variable
# import threading
# import time

# # Define a semaphore with a maximum of 2 resources
# semaphore = threading.Semaphore(2)

# # Function to access the shared resource
# def access_resource(thread_id):
#     print(f"Thread {thread_id} is trying to acquire the semaphore.")
#     # Acquire the semaphore
#     semaphore.acquire()
#     print(f"Thread {thread_id} has acquired the semaphore.")
#     try:
#         # Simulate accessing the shared resource
#         print(f"Thread {thread_id} is accessing the shared resource.")
#         time.sleep(0.002)
#     finally:
#         # Release the semaphore
#         semaphore.release()
#         print(f"Thread {thread_id} has released the semaphore.")

# # Create multiple threads to access the shared resource
# threads = []
# for i in range(5):
#     thread = threading.Thread(target=access_resource, args=(i,))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

# print("All threads have completed their execution.")
# import matplotlib.pyplot as plt
# import numpy as np
# # Generate random data
# np.random.seed(0)
# x = np.random.uniform(0, 10, 100)
# y = x + np.random.normal(0, 1, 100)
# plt.figure(figsize=(6, 4))
# plt.scatter(x, y, color='blue', alpha=0.5)
# plt.title('Random Scatter Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.show()
# import matplotlib.pyplot as plt
# categories = ['A','B','C','D','E']
# values = [23,35,17,29,12]
# colors = ['grey','gold','orange','green','blue']
# plt.figure(figsize=(6,4))
# plt.bar(categories, values, color = colors)
# plt.title('Simple Bar Chart')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.grid(True, axis='y')
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(0)
# scores = np.random.normal(10,30,1000)
# plt.figure(figsize=(6,4))
# plt.hist(scores,bins=5,edgecolor= 'red')
# plt.title("distribution of exam scores")
# plt.xlabel('score')
# plt.ylabel("number of students")
# plt.grid(axis="y",alpha =0.75)
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0,10,100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x,y1,color ='red')
# plt.plot(x,y2,color ='#00FF00')
# plt.plot(x,y1+2,linestyle = "--",color = (0,0,1))
# plt.plot(x,y2+2,linestyle ="-",color= (1,0,1,0.5))
# plt.title("different color specification")
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# np.random.seed(0)
# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.scatter(x,y,color = (0,1,0),alpha = 1)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("scatter graph")
# plt.grid(True)
# plt.show()
# import matplotlib.pyplot as plt
# categories = ['bunny','sunny','bheem','iron man']
# values = [10,20,30,40]
# colors = ['grey','gold','orange','red']
# plt.figure(figsize=(6,4))
# plt.bar(categories, values, color = colors)
# plt.title('Simple Bar Chart')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.grid(True, axis='y')
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(0)
# scores = np.random.normal(50,20,1000)
# plt.figure(figsize=(6,4))
# plt.hist(scores,bins =10,edgecolor = (0,1,0))
# plt.title("distribution of scores")
# plt.xlabel("score")
# plt.ylabel("number of students")
# plt.grid(True,axis= "y",alpha = 1)
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# import threading
# import time

# # Define a semaphore with a maximum of 2 resources
# semaphore = threading.Semaphore(2)

# # Function to access the shared resource
# def access_resource(thread_id):
#     print(f"Thread {thread_id} is trying to acquire the semaphore.")
#     # Acquire the semaphore
#     semaphore.acquire()
#     print(f"Thread {thread_id} has acquired the semaphore.")
#     try:
#         # Simulate accessing the shared resource
#         print(f"Thread {thread_id} is accessing the shared resource.")
#         time.sleep(0.002)
#     finally:
#         # Release the semaphore
#         semaphore.release()
#         print(f"Thread {thread_id} has released the semaphore.")

# # Create multiple threads to access the shared resource
# threads = []
# for i in range(5):
#     thread = threading.Thread(target=access_resource, args=(i,))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

# print("All threads have completed their execution.")
# import threading
# class Counter:
#     def __init__(self):
#         # Initialize the counter and a lock
#         self.count = 0
#         self.lock = threading.Lock()
#     def increment(self):
#         # Acquire the lock before modifying the counter
#         with self.lock:
#             self.count += 1
#     def decrement(self):
#         # Acquire the lock before modifying the counter
#         with self.lock:
#             self.count -= 1
#     def get_count(self):
#         # Acquire the lock before reading the counter
#         with self.lock:
#             return self.count
# counter = Counter()
# # Function to increment the counter
# def increment_counter():
#     for _ in range(1000):
#         counter.increment()
# # Function to decrement the counter
# def decrement_counter():
#     for _ in range(100):
#         counter.decrement()
# # Create two threads to increment and decrement the counter concurrently
# thread1 = threading.Thread(target=increment_counter)
# thread2 = threading.Thread(target=decrement_counter)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Final count:", counter.get_count())

# from threading import Semaphore, Thread

# class SharedResource:
#     def __init__(self):
#         self.isProduced = False
#         self.mutex = Semaphore(1)
#         self.producerSemaphore = Semaphore(1)
#         self.consumerSemaphore = Semaphore(0)

#     def produce(self):
#         self.producerSemaphore.acquire()
#         self.mutex.acquire()

#         if self.isProduced:
#             self.mutex.release()
#             self.consumerSemaphore.release()
#             self.producerSemaphore.acquire()
#         print("Producer produced")
#         self.isProduced = True
#         self.mutex.release()
#         self.consumerSemaphore.release()

#     def consume(self):
#         self.consumerSemaphore.acquire()
#         self.mutex.acquire()
#         if not self.isProduced:
#             self.mutex.release()
#             self.producerSemaphore.release()
#             self.consumerSemaphore.acquire()
#         print("Consumer consumed")
#         self.isProduced = False
#         self.mutex.release()
#         self.producerSemaphore.release()
# sharedResource = SharedResource()
# producerThread = Thread(target=sharedResource.produce)
# consumerThread = Thread(target=sharedResource.consume)
# producerThread.start()
# consumerThread.start()

# def user_function():
#     file_name = "/mnt/codechef/input.txt"
#     try:
#         with open(file_name,'r') as my_file:
#             for line in my_file:
#                 number = int(line.strip())
#                 print(number)
#     except FileNotFoundError as e:
#         print(e)
# user_function()
# def user_function():
#     # Open files in respective modes
#     input_filename = r"C:\Users\bharg\OneDrive\Documents\coding\bunnyin.txt"
#     output_filename = r"C:\Users\bharg\OneDrive\Documents\coding\bunnyou.txt"
#     try:
#         # Open files in respective modes
#         with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
#             # Read and write the numbers from the file
#             for line in input_file:
#                 output_file.write(line)

#         # Display the contents of output file
#         with open(output_filename, 'r') as output_file:
#             for line in output_file:
#                 print(line.strip())
#     except IOError as e:
#         print("I/O error:", e)

# user_function()


# import os

# # yE5pCbJVBszYx6E7jDhrymM3jhd1BPoMAlaJJ0KLzY8opDcPxjvraHBuERFGSg01Jv0iZbowCZxGP6QQ-prefix
# def user_function():
#     # Open files in respective modes
#     input_filename = "/mnt/codechef/input.txt"
#     output_filename = "/mnt/codechef/output.txt"
#     try:
#         with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
#             # Read and write the numbers from the file
#             for line in input_file:
#                 output_file.write(line)

#         # Display the contents of output.txt
#         with open(output_filename, 'r') as output_file:
#             for line in output_file:
#                 print(line.strip())
#     except IOError as e:
#         print("I/O error:", e)

# # yE5pCbJVBszYx6E7jDhrymM3jhd1BPoMAlaJJ0KLzY8opDcPxjvraHBuERFGSg01Jv0iZbowCZxGP6QQ-suffix
# directory = "/mnt/codechef"
# filename = "/mnt/codechef/input.txt"

# # Create the directory if it doesn't exist
# try:
#     os.makedirs(directory, exist_ok=True)
# except OSError as e:
#     print("Failed to create the directory:", e)


# # Write numbers from 1 to 5 into the file
# try:
#     with open(filename, 'w') as my_file:
#         for i in range(1, 6):
#             my_file.write(str(i) + "\n")
# except IOError as e:
#     print("I/O error:", e)

# user_function()
# def user_function():
#     # Open files in respective modes
#     input_filename =  r"C:\Users\bharg\OneDrive\Documents\coding\bunnyin.txt"
#     output_filename =  r"C:\Users\bharg\OneDrive\Documents\coding\bunnyou.txt"
#     try:
#         with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
#             # Read and write the numbers from the file
#             for line in input_file:
#                 number = int(line.strip())
#                 output_file.write(f"{number} : {number * number}\n")
#         # Display the contents of output.txt
#         with open(output_filename, "r") as output_file:
#             for line in output_file:
#                 print(line.strip())
#     except IOError as e:
#         print("An error occurred:", e)
# Writing binary data to a file
# with open('example.bin', 'wb') as file:
#     # Binary data to write (e.g., a sequence of bytes)
#     binary_data = bytearray([0, 1, 2, 3, 4, 255])
#     file.write(binary_data)
#     print("Binary data written to 'example.bin'")
# def user_function():
#     input_filename = "/mnt/codechef/input.txt"
#     output_filename = "/mnt/codechef/output.txt"
#     try:
#         with open(input_filename,'r') as input_file, open(output_filename,'w') as output_file:
#             for line in input_file:
#                 number = int(line.strip())
#                 output_file.write(str(2*number)+'\n')
#         with open(output_file,'r') as output_reader:
#             for line in output_file:
#                 print(line.strip())
#     except IOError as e:
#         print(e)
# user_function()
# import os
# file_path = "example.txt"
# if os.path.exists(file_path):
#     print("file exists")
# else:
#     print("file doesn't exist")
#     try:
#         with open(file_path,'w'):

#             pass
#         print("file created")
#     except IOError as e:
#         print('an error occurred')
#         print(e)
# try:
#     with open(file_path,'w') as writer:
#         writer.write("hello, world!")
#     print("data written to the data")
# except IOError as e:
#     print("an occurred while writing data")
#     print(e)
# try:
#     with open(file_path,'r') as reader:
#         for line in reader:
#             print("read from file:",line.strip())
# except IOError as e:
#     print("An error occurred while reading from th file.")
#     print(e)
# def user_function():
#     file_path = "/mnt/codechef/numbers.txt"
#     sum_val = 0
#     try:
#         with open(file_path,'r') as reader:
#             for line in reader:
#                 num = int(line.strip())
#                 sum_val+= num
#         print("sum:",sum_val)
#     except IOError as e:
#         print(e)
# user_function()
# import os
# def user_function():
#     file = "/mnt/codechef/input.txt"
#     try:
#         with open(file,'r') as my_file:
#             cnt = 0
#             for line in my_file:
#                 cnt+=len(line.split())
#             print("number of words:",cnt)
#     except FileNotFoundError as e:
#         print(e)
# try:

#     with open(file,'w')
# import os
# def user_function():
#     file_path = "/mnt/codechef/input.txt"
#     try:
#         with open(file_path,'r') as file:
#             search = 'codechef'
#             count = 0
#             for line in file:
#                 words = line.split()
#                 for word in words:
#                     if word == search:
#                         count+=1
#         print("number of occurrences of 'codechef':",count)
#     except IOError as e:
#         print("Error reading th file :",e)
# def main():
#     directory = "/mnt/codechef"
#     filename = "/mnt/codechef/input.txt"
#     if not os.path.exists(directory):
#         try:
#             os.makedirs(directory)
#         except OSError:
#             print("failed to create the directory")
#             return
# def print_info(obj):
#     print("Type:", type(obj))
#     print("Info:", obj.info())
# class Dog:
#     def info(self):
#         return "I am a dog."
# class Cat:
#     def info(self):
#         return "I am a cat."
# dog = Dog()
# cat = Cat()
# print_info(dog)
# print_info(cat)
# from typing import TypeVar, List

# T = TypeVar('T')  # Declare type variable

# def process_items(items: List[T]) -> List[T]:
#     processed_items = []  # Initialize an empty list for processed items
#     for item in items:
#         # Process each item here
#         processed_item = item * 2  # Example processing, just doubling the value
#         processed_items.append(processed_item)
#     return processed_items
# # Usage
# integer_list = [1, 2, 3, 4, 5]
# processed_integer_list = process_items(integer_list)
# print(processed_integer_list)  # Output: [2, 4, 6, 8, 10]
# string_list = ['a', 'b', 'c']
# processed_string_list = process_items(string_list)
# print(processed_string_list)  # Output: ['aa', 'bb', 'cc']
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.figure(figsize=(6, 4))
# plt.plot(x[::10], y1[::10], marker='o', label='Circle')
# plt.plot(x[::10], y1[::10] + 1, marker='s', label='Square')
# plt.plot(x[::10], y1[::10] + 2, marker='^', label='Triangle')
# plt.legend()
# plt.title('Different Markers')
# plt.show()
# import turtle

# cursor = turtle.Turtle()
# screen = turtle.Screen()
# screen.title("Follow @Pycode.Hubb")

# def pause():
#     cursor.speed(0)
#     for _ in range(100):
#         cursor.left(90)

# def draw_upper_dot():
#     cursor.penup()
#     cursor.right(90)
#     cursor.forward(160)
#     cursor.left(90)
#     cursor.forward(70)
#     cursor.pencolor("white")
#     cursor.dot(35)

# def move_to_lower_section():
#     cursor.penup()
#     cursor.forward(20)
#     cursor.right(90)
#     cursor.forward(10)
#     cursor.right(90)
#     cursor.pendown()

# def draw_half_logo():
#     cursor.forward(50)
#     draw_side_curve()
#     cursor.forward(90)
#     draw_first_left_curve()
#     cursor.forward(40)
#     cursor.left(90)
#     cursor.forward(80)
#     cursor.right(90)
#     cursor.forward(10)
#     cursor.right(90)
#     cursor.forward(120)
#     draw_second_left_curve()
#     cursor.forward(30)
#     cursor.left(90)
#     cursor.forward(50)
#     draw_right_curve()
#     cursor.forward(40)
#     cursor.end_fill()

# def draw_lower_dot():
#     cursor.left(90)
#     cursor.penup()
#     cursor.forward(310)
#     cursor.left(90)
#     cursor.forward(120)
#     cursor.pendown()
#     cursor.dot(35)

# def draw_first_left_curve():
#     draw_side_curve()
#     cursor.forward(80)
#     draw_side_curve()

# def draw_second_left_curve():
#     draw_side_curve()
#     cursor.forward(90)
#     draw_side_curve()

# def draw_side_curve():
#     for _ in range(90):
#         cursor.left(1)
#         cursor.forward(1)

# def draw_right_curve():
#     for _ in range(90):
#         cursor.right(1)
#         cursor.forward(1)

# cursor.pensize(2)
# cursor.speed(10)
# cursor.pencolor("white")
# screen.bgcolor("black")

# cursor.fillcolor("#306998")
# cursor.begin_fill()
# draw_half_logo()
# cursor.end_fill()

# move_to_lower_section()

# cursor.fillcolor("#FFD43B")
# cursor.begin_fill()
# draw_half_logo()
# cursor.end_fill()

# draw_upper_dot()
# draw_lower_dot()
# pause()

# turtle.done()
# from typing import TypeVar,List
# T = TypeVar('T')
# def process_items(items:List[T]) -> List[T]:
#     processed_items = []
#     for item in items:
#         processed_item = item*2
#         processed_items.append(processed_item)
#     return processed_items
# # Usage
# integer_list = [1, 2, 3, 4, 5]
# processed_integer_list = process_items(integer_list)
# print(processed_integer_list)  # Output: [2, 4, 6, 8, 10]
# string_list = ['a', 'b', 'c']
# processed_string_list = process_items(string_list)
# print(processed_string_list)  # Output: ['aa', 'bb', 'cc']
# from typing import TypeVar
# T = TypeVar('T')
# def find_max(a:T,b:T) -> T:
#     return a if a > b else b
# max_int = find_max(10,5)
# print("max Integer:",max_int)
# max_string = find_max('apple',"banana")
# print("max string:",max_string)

# max_double = find_max(3.14,2.71)
# print("max Double:",max_double)
# from typing import TypeVar
# T = TypeVar("T")
# class Box:
#     def __init__(self,item:T):
#         self.item = item
#     def get_item(self) -> T:
#         return self.item
# string_box = Box("hello")
# print(string_box.get_item())
# from typing import TypeVar,List
# T = TypeVar("T")
# def find_max(arr:List[T]) -> T:
#     max_element = arr[0]


#     for element in arr[1:]:
#         if element > max_element:
#             max_element = element
#     return max_element
# int_array = [5,12,3,8,9]
# double_array = [2.4,6.7,1.8,9.2,4.5]
# print(find_max(int_array))
# print(find_max(double_array))
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.figure(figsize=(6, 4))
# plt.plot(x[::5], y1[::5], marker='o', label='Circle')
# plt.plot(x[::5], y1[::5] + 1, marker='s', label='Square')
# plt.plot(x[::10], y1[::10] + 2, marker='^', label='Triangle')
# plt.legend()
# plt.title('Different Markers')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use('seaborn')
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# plt.figure(figsize=(6, 4))
# plt.plot(x, y)
# plt.title('Sine Wave')
# plt.show()
# class Node:
#     def __init__(self,value):
#         self.value = value
# head = Node(1)
# print("The value at head is", head.value)
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_front(self,value):
#         print("inserting:",value)
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#     def get_head_value(self):
#         if self.head  is None:
#             return -1
#         else:
#             return self.head.value
# list = LinkedList()
# list.insert_front(3)
# print("The value at the head is:",list.get_head_value())
# list.insert_front(2)
# print("The value at the head is:",list.get_head_value())
# cook your dish here
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_at_end(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#     def get_last_value(self):
#         if self.head is None:
#             return -1
#         current = self.head
#         while current.next:
#             current = current.next
#         return current.value
# if __name__ == "__main__":
#     n = int(input())
#     linked_list = LinkedList()
#     vals = list(map(int, input().split()))
#     for x in vals:
#         linked_list.insert_at_end(x)
#         print(linked_list.get_last_value(), end=" ")
# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use(['bmh'])

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.figure(figsize=(6, 4))
# plt.plot(x, y)
# plt.title('Sine Wave')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.title("Sine Wave", fontsize=50, fontweight='heavy', color='green')
# plt.xlabel("X-axis", fontsize=20, fontstyle='oblique', labelpad=10)
# plt.ylabel("Y-axis", fontsize=14, fontweight='heavy', labelpad=-20)
# plt.show()
# cook your dish here
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_at_end(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#     def get_last_value(self):
#         if self.head is None:
#             return -1
#         current = self.head
#         while current.next:
#             current = current.next
#         return current.value
# if __name__ == "__main__":
#     n = int(input())
#     linked_list = LinkedList()
#     vals = list(map(int, input().split()))
#     for x in vals:
#         linked_list.insert_at_end(x)
#         print(linked_list.get_last_value(), end=" ")
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_after_k(self,value,k):
#         new_node = Node(value)
#         current = self.head
#         if current is None:
#             self.head = new_node
#             return
#         for _ in range(k-1):
#             current = current.next
#         new_node.next = new_node
#     def print_values(self);
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0,10,100)
# y = np.sin(x)
# plt.plot(x,y)
# plt.xlim(-5,5)
# plt.ylim(-5,5)
# plt.title("sine wave with adjusted axes")
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# fig,axs = plt.subplots(1,2,figsize = (6,4))
# x = np.linspace(0,10,100)
# axs[0].plot(x,np.sin(x))
# axs[0].set_title("sine wave")
# axs[1].plot(x, np.tan(x))
# axs[1].set_title('tan wave')
# plt.tight_layout()
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# fig,axs = plt.subplots(2,2,figsize = (6,6))
# x = np.linspace(0,2*np.pi,100)
# axs[0,0].plot(x,np.sin(x))
# axs[0,0].set_title("sine wave")
# axs[0,1].plot(x,np.cos(x))
# axs[0,1].set_title("cos wave")
# random_data1 = np.random.randn(100)
# random_data2 = np.random.randn(100)
# axs[1,0].scatter(random_data1,random_data2)
# axs[1,0].set_title("scatter plot")
# random_data3 = np.random.randn(1000)
# axs[1,1].hist(random_data3,bins = 30)
# axs[1,1].set_title("histogram")
# fig.suptitle("Multiple Plots Example",fontsize = 20)
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# # Define the x values for different ranges
# x_full = np.linspace(-np.pi, np.pi)
# x_arcs = np.linspace(-1, 1, 400)  # For arc functions

# # Create subplots
# fig, axs = plt.subplots(2, 3, figsize=(15, 8))

# # Plot sine
# axs[0, 0].plot(x_full, np.sin(x_full))
# axs[0, 0].set_title('Sine')
# axs[0, 0].grid(True)

# # Plot cosine
# axs[0, 1].plot(x_full, np.cos(x_full))
# axs[0, 1].set_title('Cosine')
# axs[0, 1].grid(True)

# # Plot tangent
# axs[0, 2].plot(x_full, np.tan(x_full))
# axs[0, 2].set_title('Tangent')
# axs[0, 2].set_ylim(-10, 10)  # Limit y-axis to avoid extreme values
# axs[0, 2].grid(True)

# # Plot arcsine
# axs[1, 0].plot(x_arcs, np.arcsin(x_arcs))
# axs[1, 0].set_title('Arcsin')
# axs[1, 0].grid(True)

# # Plot arccosine
# axs[1, 1].plot(x_arcs, np.arccos(x_arcs))
# axs[1, 1].set_title('Arccos')
# axs[1, 1].grid(True)

# # Plot arctangent
# axs[1, 2].plot(x_full, np.arctan(x_full))
# axs[1, 2].set_title('Arctan')
# axs[1, 2].grid(True)

# # Adjust layout
# plt.tight_layout()
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# # Define the range of x values
# x = np.linspace(-10, 10, 100)

# # Create a figure with 3 subplots arranged vertically
# fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# # Plot y = x
# axs[0].plot(x, x, label='y = x', color='blue')
# axs[0].set_title('Linear Function')
# axs[0].set_xlabel('x')
# axs[0].set_ylabel('y')
# axs[0].legend()
# axs[0].grid(True)

# # Plot y = x^2
# axs[1].plot(x, x**2, label='y = x^2', color='green')
# axs[1].set_title('Quadratic Function')
# axs[1].set_xlabel('x')
# axs[1].set_ylabel('y')
# axs[1].legend()
# axs[1].grid(True)

# # Plot y = x^3
# axs[2].plot(x, x**3, label='y = x^3', color='red')
# axs[2].set_title('Cubic Function')
# axs[2].set_xlabel('x')
# axs[2].set_ylabel('y')
# axs[2].legend()
# axs[2].grid(True)

# # Adjust layout to avoid overlap
# plt.tight_layout()

# # Display the plot
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Create a 2x2 grid of subplots
# fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# # Define x
# x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# # Plot sine
# axs[0, 0].plot(x, np.sin(x))
# axs[0, 0].set_title('Sine')

# # Plot cosine
# axs[0, 1].plot(x, np.cos(x))
# axs[0, 1].set_title('Cosine')

# # Plot tangent
# axs[1, 0].plot(x, np.tan(x))
# axs[1, 0].set_title('Tangent')
# axs[1, 0].set_ylim(-10, 10)  # Limit y-axis to avoid extreme values

# # Plot arctangent
# axs[1, 1].plot(x, np.arctan(x))
# axs[1, 1].set_title('Arc Tangent')

# # Adjust layout
# plt.tight_layout()
# plt.show()
# import matplotlib.pyplot as plt

# expenses = ['Rent', 'Food', 'Utilities', 'Entertainment']
# amounts = [1200, 400, 200, 200]
# colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
# plt.pie(amounts, labels=expenses, colors=colors, autopct='%1.1f%%', startangle=90)
# plt.axis('equal')
# plt.title('Monthly Expense Distribution')
# plt.legend(title="Expense Categories")
# plt.show()
# import matplotlib.pyplot as plt
# expenses = ['Rent', 'Food', 'Utilities', 'Entertainment']
# amounts = [1200, 400, 200, 200]

# colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# plt.pie(amounts, labels=expenses, colors=colors, autopct='%1.1f%%', startangle=90)

# plt.axis('equal')

# plt.title("Monthly Expense Distribution")

# plt.legend(title="Expense Categories")

# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt

# # Generate some sample data
# np.random.seed(42)
# data = np.random.normal(100, 20, 200)

# # Calculate the five-number summary
# minimum = np.min(data)
# q1 = np.percentile(data, 25)
# median = np.median(data)
# q3 = np.percentile(data, 75)
# maximum = np.max(data)

# # Create the box plot
# fig, ax = plt.subplots(figsize=(6, 4))
# bp = ax.boxplot([data], whis=[0, 100], showfliers=False)
# # Add labels and title
# ax.set_xlabel('Dataset')
# ax.set_ylabel('Values')
# ax.set_title('Simple Box Plot (Five-Number Summary)')
# # Add annotations for each part of the box plot
# ax.annotate('Maximum', xy=(1, maximum), xytext=(1.1, maximum),arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('Third Quartile', xy=(1, q3), xytext=(1.1, q3),arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('Median', xy=(1, median), xytext=(1.1, median),arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('First Quartile', xy=(1, q1), xytext=(1.1, q1),arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('Minimum', xy=(1, minimum), xytext=(1.1, minimum),arrowprops=dict(facecolor='black', shrink=0.05))
# # Remove x-axis ticks
# ax.set_xticks([])
# plt.tight_layout()
# plt.show()
# import numpy as np

# # Generate some sample data
# data = np.random.normal(100, 20, 200)

# # Compute the 25th and 75th percentiles
# percentiles_25_75 = np.percentile(data, [25, 75])

# print(f"25th Percentile: {percentiles_25_75[0]}")
# print(f"75th Percentile: {percentiles_25_75[1]}")
# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 600

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (135, 206, 250)
# BROWN = (139, 69, 19)  # For the ground
# YELLOW = (255, 255, 0)  # For the bird

# # Set up the display
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Flappy Bird")

# # Load images
# bird_image = pygame.Surface((34, 24))
# bird_image.fill(YELLOW)
# pipe_image = pygame.Surface((70, 500))
# pipe_image.fill(GREEN)
# ground_image = pygame.Surface((SCREEN_WIDTH, 100))
# ground_image.fill(BROWN)

# # Game variables
# bird_x = 50
# bird_y = SCREEN_HEIGHT // 2
# bird_velocity = 0
# gravity = 0.5
# jump_strength = -10

# pipe_width = 70
# pipe_gap = 150
# pipe_velocity = 5
# pipe_frequency = 1500  # milliseconds
# last_pipe = pygame.time.get_ticks() - pipe_frequency

# ground_y = SCREEN_HEIGHT - 100


# def draw_bird(y):
#     screen.blit(bird_image, (bird_x, y))


# def draw_pipe(x, y):
#     screen.blit(pipe_image, (x, y))
#     screen.blit(pipe_image, (x, y - pipe_image.get_height() - pipe_gap))


# def draw_ground():
#     screen.blit(ground_image, (0, ground_y))


# def game_loop():
#     global bird_y, bird_velocity, last_pipe
#     running = True
#     clock = pygame.time.Clock()

#     pipes = []
#     score = 0

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     bird_velocity = jump_strength

#         # Bird mechanics
#         bird_velocity += gravity
#         bird_y += bird_velocity

#         # Pipe mechanics
#         current_time = pygame.time.get_ticks()
#         if current_time - last_pipe > pipe_frequency:
#             pipe_height = random.randint(150, SCREEN_HEIGHT - 150 - pipe_gap)
#             pipes.append([SCREEN_WIDTH, pipe_height])
#             last_pipe = current_time

#         pipes = [[x - pipe_velocity, y] for x, y in pipes if x > -pipe_width]

#         # Check for collisions
#         bird_rect = pygame.Rect(bird_x, bird_y, 34, 24)
#         for pipe_x, pipe_y in pipes:
#             top_pipe_rect = pygame.Rect(
#                 pipe_x, pipe_y - pipe_image.get_height(), pipe_width, pipe_image.get_height())
#             bottom_pipe_rect = pygame.Rect(
#                 pipe_x, pipe_y + pipe_gap, pipe_width, SCREEN_HEIGHT)
#             if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
#                 pygame.quit()
#                 return

#         if bird_y + 24 >= ground_y:
#             pygame.quit()
#             return

#         # Drawing
#         screen.fill(BLUE)
#         draw_ground()
#         draw_bird(bird_y)
#         for pipe_x, pipe_y in pipes:
#             draw_pipe(pipe_x, pipe_y)

#         pygame.display.flip()
#         clock.tick(30)


# if __name__ == "__main__":
# #     game_loop()
# import matplotlib.pyplot as plt
# import numpy as np
# np.random.seed(0)
# class1 = np.random.normal(70,10,30)
# class2 = np.random.normal(80,5,30)
# class3 = np.random.normal(75,8,30)
# plt.boxplot([class1,class2,class3],labels = ["class1","class2","class3"])
# plt.title("Distribution of Test Scores by Class")
# plt.ylabel("scores")
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(10)
# group1 = np.random.normal(100,10,200)
# group2 = np.random.normal(80,30,200)
# group3 = np.random.normal(5,10,200)
# fig,ax = plt.subplots(figsize =(6,4))
# violin_parts = ax.violinplot([group1,group2,group3])
# plt.title("graph violin")
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# data = np.array([[1,2,3],[4,5,6],[7,8,9]])
# plt.figure(figsize =(6,4))
# plt.imshow(data,cmap ="coolwarm")
# plt.colorbar()
# plt.title("simple heatmap")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Generate sample temperature data for a year
# dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
# # Mean of 15°C, std dev of 10°C
# temperatures = np.random.normal(loc=15, scale=10, size=len(dates))
# temperatures = temperatures + 15 * \
#     np.sin(np.arange(len(dates)) * 2 * np.pi / 365)  # Add seasonal trend

# # Create DataFrame
# df = pd.DataFrame({'Date': dates, 'Temperature': temperatures})
# df.set_index('Date', inplace=True)

# # Calculate moving average
# df['Moving_Avg'] = df['Temperature'].rolling(window=30).mean()
# # Plotting
# plt.figure(figsize=(12, 6))
# plt.plot(df.index, df['Temperature'], label='Daily Temperature', alpha=0.5)
# plt.plot(df.index, df['Moving_Avg'],
#          label='30-day Moving Average', color='red')
# plt.title('Daily Temperatures in City X (2023)')
# plt.xlabel('Date')
# plt.ylabel('Temperature (°C)')
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()
# import pandas as pd
# data = {
#     'Date': ['2024-09-17', '2024-09-18', '2024-09-19', '2024-09-20'],
#     'Value': [10, 15, 20, 25]
# }
# df = pd.DataFrame(data)
# df["Date"] =pd.to_datetime(df['Date'])
# df.set_index("Data",inplace = True)
# import pandas as pd

# # Create the DataFrame
# data = {
#     "Date": ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
#     'Sales': [100, 120, 110, 140, 130]
# }
# df = pd.DataFrame(data)

# # Print the DataFrame
# print(df.head())

# # Convert the 'Date' column to datetime
# df["Date"] = pd.to_datetime(df["Date"])

# # Set the 'Date' column as the index
# df.set_index("Date", inplace=True)

# # Print the modified DataFrame
# print(df)
# import pandas as pd
# import matplotlib.pyplot as plt
# data ={
#     'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
#     'Sales': [100, 120, 110, 140, 130]
# }
# df =pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df.set_index("Date",inplace= True)
# plt.figure(figsize=(6,4))
# plt.plot(df.index,df["Sales"])
# plt.title
# import pandas as pd
# import matplotlib.pyplot as plt
# data = {
#     'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
#     'Sales': [100, 120, 110, 140, 130]
# }
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df.set_index("Date", inplace=True)
# plt.figure(figsize=(6, 4))
# plt.plot(df.index, df["Sales"])
# plt.title("Time series data")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt

# # Create sample data
# data = {
#     'Date': pd.date_range(start='2023-01-01', end='2023-01-10'),
#     'Electronics': [100, 120, 110, 140, 130, 160, 150, 180, 190, 210],
#     'Clothing': [80, 90, 85, 100, 95, 110, 105, 120, 125, 130],
#     'Books': [50, 60, 55, 65, 70, 75, 80, 85, 90, 95]
# }

# # Create the DataFrame
# df = pd.DataFrame(data)
# df.set_index('Date', inplace=True)

# # Create the plot
# plt.figure(figsize=(6, 4))

# # Plot each time series
# plt.plot(df.index, df['Electronics'], marker='o')
# plt.plot(df.index, df['Clothing'], marker='s')
# plt.plot(df.index, df['Books'], marker='^')

# # Rotate and align the tick labels so they look better
# plt.gcf().autofmt_xdate()

# # Use tight layout to prevent clipping of labels
# plt.tight_layout()

# # Display the plot
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt

# # Create sample data
# data = {
#     'Date': pd.date_range(start='2023-01-01', end='2023-01-10'),
#     'Electronics': [100, 120, 110, 140, 130, 160, 150, 180, 190, 210],
#     'Clothing': [80, 90, 85, 100, 95, 110, 105, 120, 125, 130],
#     'Books': [50, 60, 55, 65, 70, 75, 80, 85, 90, 95]
# }

# # Create the DataFrame
# df = pd.DataFrame(data)
# df.set_index('Date', inplace=True)

# # Create the plot
# plt.figure(figsize=(6, 4))

# # Plot each time series
# plt.plot(df.index, df['Electronics'], marker='o')
# plt.plot(df.index, df['Clothing'], marker='s')
# plt.plot(df.index, df['Books'], marker='^')

# # Rotate and align the tick labels so they look better
# plt.gcf()

# # Use tight layout to prevent clipping of labels
# plt.tight_layout()

# # Display the plot
# plt.show()
# import matplotlib.pyplot as plt
# import  pandas as pd
# data = {
#     'Date': pd.date_range(start='2023-01-01', end='2023-01-10'),
#     'Electronics': [100, 120, 110, 140, 130, 160, 150, 180, 190, 210],
#     'Clothing': [80, 90, 85, 100, 95, 110, 105, 120, 125, 130],
#     'Books': [50, 60, 55, 65, 70, 75, 80, 85, 90, 95]
# }
# df = pd.DataFrame(data)
# df.set_index("Date",inplace = True)
# plt.figure(figsize=(6,4))
# plt.plot(df.index,df["Electronics"],marker ='o')
# plt.plot(df.index,df["Clothing"],marker ='s')
# plt.plot(df.index,df["Books"],marker ='^')
# plt.gcf().autofmt_xdate()
# plt.tight_layout()
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# # Create sample data with missing values
# dates = pd.date_range(start='2023-01-01', periods=10)
# values = [100, 120, np.nan, 140, 130, np.nan, 160, 150, 180, 170]
# df = pd.DataFrame({'Value': values}, index=dates)
# # Plot with dropped NaN values - update the code below
# plt.figure(figsize=(6, 4))
# plt.subplot(2, 1, 1)
# plt.gcf().autofmt_xdate()
# plt.title('Time Series with Dropped Missing Values')
# # Plot with filled NaN values - update the code below
# plt.subplot(2, 1, 2)
# plt.gcf().autofmt_xdate()
# plt.title('Time Series with Filled Missing Values')
# plt.tight_layout()
# plt.show()
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# np.random.seed(42)
# num_customers = 100
# age = np.random.randint(20,70,num_customers)
# income = np.random.randint(20000,100000,num_customers)
# purchase_freq = np.random.randint(1,20,num_customers)
# fig = plt.figure(figsize=(6,5))
# ax = fig.add_subplot(111,projection ='3d')
# ax.scatter(age,income,purchase_freq)
# ax.set_title("Customer Data: Age,Income and Purchase Frequency")
# ax.set_xlabel("Age")
# ax.set_ylabel("Income($)")
# ax.set_zlabel("Purchase Frequency (per year)")
# plt.show()
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np

# # Generate sample data
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# x, y = np.meshgrid(x, y)

# # Calculate Z values for the sine and cosine functions
# z1 = np.sin(np.sqrt(x**2 + y**2))
# z2 = np.cos(np.sqrt(x**2 + y**2))

# # Create a figure
# fig = plt.figure(figsize=(8, 10))

# # First subplot (top)
# ax1 = fig.add_subplot(211, projection='3d')  # 2 rows, 1 column, first subplot
# ax1.plot_surface(x, y, z1, cmap='viridis')
# ax1.set_title('3D Surface Plot of Sine Function')
# ax1.set_xlabel('X axis')
# ax1.set_ylabel('Y axis')
# ax1.set_zlabel('Z = sin(sqrt(x^2 + y^2))')

# # Second subplot (bottom)
# ax2 = fig.add_subplot(212, projection='3d')  # 2 rows, 1 column, second subplot
# ax2.plot_surface(x, y, z2, cmap='plasma')
# ax2.set_title('3D Surface Plot of Cosine Function')
# ax2.set_xlabel('X axis')
# ax2.set_ylabel('Y axis')
# ax2.set_zlabel('Z = cos(sqrt(x^2 + y^2))')

# # Adjust layout
# plt.tight_layout()

# # Sh the plot
# plt.show()
# import matplotlib .pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure(figsize= (6,4))
# ax = fig.add_subplot(111,projection = '3d')
# ax.set_xlabel("X-axis",fontsize= 12)
# ax.set_ylabel("z-axis",fontsize= 12)
# ax.set_zlabel("y-axis",fontsize= 12)
# ax.view_init(elev =20,azim = 45)
# ax.set_title("My first 3d plot",fontsize = 14)
# X = np.random.rand(10)
# y = np.random.rand(10)
# z = np.random.rand(10)
# ax.scatter(X,y,z,c=i',marker="^")
# plt.show()
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# n = 10000
# x = np.random.normal(0,1,n)
# y = np.random.normal(0,1,n)
# z = np.random.normal(0,1,n)

# fig = plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111,projection='3d')
# scatter = ax.scatter(x,y,z,c=z,cmap = 'viridis',alpha = 1)
# ax.view_init(elev = 20,azim = 45)
# plt.show()
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     b = 0
#     c = n
#     while (c):
#         a = c % 10
#         b = b*10+a
#         c = c//10
#     if (b == n):
#         print("wins")
#     else:
#         print("loses")
# class Solution(object):
#     def removeElement(self, nums, val):
#         for i in range(len(nums)):
#             if i == val:
#                 val.replace(val, '_')
#                 break


# nums = list(map(int, input().split()))
# val = int(input())
# Solution()
# removeElement()
# def stutter(word):
#     # Get the first two letters of the word
#     first_two = word[:2]
#     # Create the stuttered version
#     stuttered = f"{first_two}... {first_two}... {word}?"
#     return stuttered

# # Test cases
# print(stutter("incredible"))  # "in... in... incredible?"
# print(stutter("enthusiastic")) # "en... en... enthusiastic?"
# print(stutter("outstanding"))  # "ou... ou... outstanding?"

# def discount(price,discount1):

#     calc = (price*discount1)/100
#     print("the discount amount was:",calc)


# price = int(input())
# discount1 = int(input())
# discount(price,discount1)
# import numpy as np
# a = np.rad2deg(1)
# print(a)
# import numpy as np
# # radians_to_degrees(1) ➞ 57.3
# print(np.rad2deg(1))
# # radians_to_degrees(20) ➞ 1145.9
# print(np.rad2deg(20))
# # radians_to_degrees(50) ➞ 2864.8
# print(np.rad2deg(50))
# a = [50,20,50,30,11,12]
# print(a.count(50))
# import ctypes

# # Define the integer variable
# my_val = 13

# # Print the value of the integer
# print(f"Value of integer 'myVal': {my_val}")

# # Print the size of the integer (in bytes)
# print(f"Size of integer 'myVal': {ctypes.sizeof(ctypes.c_int)} bytes")

# # Print the address of the variable
# address = id(my_val)
# print(f"Address to 'myVal': {hex(address)}")

# # Print the size of the address (in bytes)
# print(f"Size of the address to myVal: {ctypes.sizeof(ctypes.c_void_p)} bytes")
# import ctypes
# class MyStruct(ctypes.Structure):
#     _fields_ = [("field1", ctypes.c_int),
#                 ("field2", ctypes.c_float)]


# my_struct = MyStruct(field1=10, field2=3.14)
# print(f"Field 1: {my_struct.field1}, Field 2: {my_struct.field2}")
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# currentNode = node1
# while currentNode:
#     print(currentNode.data,end="->"  )
#     currentNode = currentNode.next
# print("null")
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# node1 = Node(1)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# currentNode = node1
# while currentNode:
#     print(currentNode.data,end="-->")
#     currentNode = currentNode.next
# print("Null")
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.next = node2
# node3.next = node4
# node4.prev = node3

# print("\nTransvering forward")
# currentNode = node1
# while currentNode:
#     print(currentNode.data,end="-->")
#     currentNode= currentNode.next
# print("Null")
# print("\nTransvering backward")
# currentNode = node4
# while currentNode:
#     print(currentNode.data,end="-->")
#     currentNode = currentNode.prev
# print("Null")
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node1
# currentNode = node1
# startNode = node1
# print(currentNode.data,end="-->")
# currentNode = currentNode.next
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)

# node1.next = node2
# node1.prev = node4

# node2.prev = node1
# node2.next = node3

# node3.prev = node2
# node3.next = node4

# node4.prev = node3
# node4.next = node1

# print("\nTraversing forward:")
# currentNode = node1
# startNode = node1
# print(currentNode.data, end=" -> ")
# currentNode = currentNode.next

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
# print("...")

# print("\nTraversing backward:")
# currentNode = node4
# startNode = node4
# print(currentNode.data, end=" -> ")
# currentNode = currentNode.prev

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.prev
# print("...")
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# def traverseAndPRint(head):
#     currentNode = head
#     while currentNode:
#         print(currentNode.data,end="-->")
#         currentNode = currentNode.next
#     print("NUll")
# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# traverseAndPRint(node1)
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# def findLowestValue(head):
#     minValue = head.data
#     currentNode = head.next
#     while currentNode:
#         if currentNode.data <minValue :
#             minValue = currentNode.data
#         currentNode = currentNode.next
#     return minValue
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# def traverseAndPrint(head):
#     currentNode = head
#     while currentNode:
#         print(currentNode.data,end="-->")
#         currentNode = currentNode.next
#     print("NULL")
# def deleteSpecificNode(head,nodeToDelete):
#     if head == nodeToDelete:
#         return head.next
#     currentNode = head
#     while currentNode.next and currentNode.next != odeToDelete:
#            currentNode = currentNode.next
#     if currentNode.next is None:
#         return head
#     currentNode.next = currentNode.next.next
#     return head
# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# print("Before deletion:")
# traverseAndPrint(node1)

# # Delete node4
# node1 = deleteSpecificNode(node1, node4)

# print("\nAfter deletion:")
# traverseAndPrint(node1)

# for i in range(7):
#     for  j in range(5):
#         if(j==0) or ((i==0 or i==6) and (j>0)):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()
# for i in range(7):
#     for j in range(5):
#         if ((i == 0 or i == 6) and (j != 4)) or (j == 0) or (j == 4 and (i > 0 and i < 6)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# for i in range(7):
#     for j in range(5):
#         if (i == 0 or i == 3 or i == 6) or (j == 0 and (i > 0 and i < 3)) or(j==0 and ( i>3 and i<6)):
#             print("*", end=" ")
#         else:
#             print(end=" ")
#     print()
# for i in range(7):
#     for j in range(5):
#         if (i==0 or i==3) or (j==0):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()
# for i in range(8):
#     for j in range(6):
#         if (j == 0) or ((i == 0 or i == 7) and (j < 5)) or (j == 4 and (i > 2 and i < 7) or (i==3 and j==3) or(i==3 and j==5)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# for i in range(7):
#     for j in range(5):
#         if (j == 0 or j == 4) or (i == 3 and (j > 0 and j < 4)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# for i in range(7):
#     for j in range(6):
#         if (i == 0 or i == 6) or (j == 3 and (i > 0 and i < 6)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# for i in range(7):
#     for j in range(5):
#         if (i==0) or (j==2) or (i==6 and (j<2)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# for i in range(7):
#     for j in range(5):
#         if (j==0) or (i <=3 and j==4-i) or (i>3 and j == (i-2)):
#         print("*",end=" ")
#     else:
#         print(end="  ")
# print()
# for i in range(7):
#     for j in range(7):
#         if (j==0 or j==6) or (i==j and j==i and (j<4)) or (j==5 and i==1) or(j==4 and i==2):
#         print("*", end=" ")
#     else:
#         print(end="  ")
# print(
# k = 0
# h = 6
# for i in range(5):
#     for j in range(7):
#         if ((i == j) and (j < 4)):
#             print("*", end=" ")
#         elif (i == k) and (j == h):
#             print("*", end=" ")
#             i += 1
#             j -= 1
#         else:
#             print(end="  ")
#     print()
# for i in range(4):
#     for j in range(7):
#         if (j == 0 or j == 6) or (i+j ==3) or (j-i ==3):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# for i in range(5):
#     for j in range(5):
#         if (i == j) or (i+j == 4):
#             print("* ", end=" ")
#         else:
#             print(end="  ")
#     print()
# for i in range(6):
#     for j in range(5):
#         if (i == j and (j < 3)) or ((i+j==4) and (j>2)) or (j==2 and(i>2)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# ########################### Hollow pyramid######################
# for i in range(6):
#     for j in range(6):
#         if (i == 0 or j == 5) or (i == j):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# n = int(input("Enter the n value:",))
# num = 0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num+1,end=" ")
#         num+=1
#     print()
# n = input()
# for i in range(1, len(n)+1):
#     print(n[:i])
# n = int(input())
# for i in range(n, 0, -1):
#     for j in range(1, i):
#         print(j, end=" ")
#     print()
# n = int(input())
# for i in range(n):
#     for j in range(n+1):
#         if (i == n-2) or (i+j == 2):
#             print(" * ", end=" ")
#         else:
#             print(end=" ")
#     print()
# n = int(input("Enter the side of a triangle:",))
# for i in range(1, n):
#     for j in range(1, n+3):
#         if ((i == n-1) and (j < 6)) or (i+j == 5) or (j-i == 3):
#             print("*", end=" ")
#         else:
#             print(end=" ")
#     print()
# for i in range(4):
#     for j in range(8):
#         if (i == 3 and (j % 2 == 0)) or (i+j == 3) or (j-i == 3):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# from scipy import stats
# import numpy as np

# data = np.array([1, 2, 2, 3, 4, 4, 4, 5])
# mode_value = stats.mode(data)
# print(mode_value[0])  # Output: 4

# from collections import defaultdict

# freq = defaultdict(int)
# print(freq)

# for i in range(6):
#     for j in range(7):
#         if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i-j == 2) or(i+j)==8:
#             print("*", end=" ")
#         else:
#             print(end="  ")

#     print()
# n = int(input("enter the number:",))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     for j in range(2,i+1):
#         print(j,end=" ")
#     print()

# num = int(input("Enter the number:",))
# for i in range(num):
#     val = i+1
#     dec = num+2
#     for j in range(i+1):
#         print(format(val, '<5'), end=" ")
#         val = val + dec
#         dec = dec-1
#     print()
# cook your dish here
# for i in range(int(input())):
#     x = int(input())
#     if (x % 10 == 0):
#         print(x//10)
#     elif (x % 10 != 0 and x % 5 == 0):
#         print((x//10)+1)
#     else:
#         print("-1")
# def PigLatin(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     if string[0].lower() in vowels:
#         return string + "yay"
#     else:
#         for i in range(len(string)):
#             if string[i].lower() in vowels:
#                 return string[i:].lower() + string[:i].lower() + "ay"


# sentence = str(input("Enter a string: ")).split(" ")
# answer = ""

# for word in sentence:
#     answer+=PigLatin(word)+" "

# print(answer.strip().lower())
# from string import PascalCase
# n = input()
# print(PascalCase(n))
# def pugunc(r):
#     for x in range(r):
#         print(" "*(r-x-1)+"*"*(2*x+1))
# r = int(input())
# pugunc(r)
# class Car():
#     sound = "beep"
#     def __init__(self,color):
#         self.color = "Blue"
# ford = Car("blue")
# print(ford.sound,ford.color)
# class Dog():
#     def makeSound(self):
#         print("bark")
# a= Dog()
# a.makeSound()
# class Dog():
#     name = ''
#     def SetName(self,new_name):
#         self.name = new_name
#     def getName(self):
#         return self.name
# s = Dog()
# s.SetName("rocky")
# print(s.getName())
# class Dog():
#     age =5
#     def happyBirthday(self):
#         self.age+=1
# s = Dog()
# s.happyBirthday()
# print(s.age)
# class Dog():
#     age = 6
#     def getAge(self):
#         return self.age
#     def printInfo(self):
#         if self.getAge()<10:
#             print("puppy")
# a = Dog()
# a.printInfo()
# class Dog():
#     def __str__(self):
#         return "hello"
# sam = Dog()
# print(sam)
# class Animal( ):
#     def __init__(self, species):
#             self.species = species
# class Dog(Animal):
#     def __init__(self, species, name):
#         self.name = name

#         super( ).__init__(species)   #  using super to declare the species

#  sam = Dog("Canine", "Sammi")
#  print(sam.species)import pprint
# import pprint
# data = {'key1': [1, 2, 3], 'key2': {'subkey': 'value'}}
# pprint.pprint(data)
# from pprint import pprint
# import requests

# response = requests.get('https://api.github.com/users/octocat')
# pprint(response.json())
# from pprint import PrettyPrinter
# data = {"key1": list(range(50)), "key2": {"inner": list(range(10))}}
# printer = PrettyPrinter(width=40, depth=2)
# printer.pprint(data)
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--name', help='Your name')
# args = parser.parse_args()
# print(f'Hello, {args.name}')
# a = list(map(str,input().split()))
# for  i in range(1,len(a)):
#     for j in range(len(a)-1):
#         if ord(a[i][0])< ord(a[j][0]):
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp 
# print(a)

# cook your dish herefr
# Cook your dish here
# for _ in range(int(input("Enter the number of test cases: "))):
#     n = int(input("Enter the value of n: "))
#     found = False  # To check if we found at least one solution
#     for i in range(1, 10):
#         for j in range(1, 10):
#             a = i | j  # Bitwise OR
#             b = i ^ j  # Bitwise XOR
#             if (a * b) == n:
#                 print(i, j)
#                 found = True
#     if not found:
#         print(-1)  # Print -1 if no solution is found
# # cook your dish here
# for _ in range(int(input())):
#     n, y = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = []
#     result = 0
#     for num in a:
#         result |= num 
#     for i in range(0,1)
# a = [7,2,31,0,8,99]
# b = [7,2,31,0,8]
# if a==b:
#     print("they are equal")
# else:
#     print("not equal")    

