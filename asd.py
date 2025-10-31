# a1 = 0
# a2 = 1
# print(a2)
# print(a1)
# for fib in range(18):
#     newFibo = a1 +a2
#     print(newFibo)
#     a2 = a1
#     a1 = newFibo
# print(0)
# print(1)
# count = 2
# def fibonacci(a1,a2):
#     global count
#     if count <= 18:
#         newFib = a1 + a2
#         print(newFib)
#         a2 = a1
#         a1 = a1+a2
#         count+=1
#         fibonacci(a1,a2)
#     else:
#         return
# fibonacci(1,0)
# def F(n):
#     if n<=1:
#         return n
#     else:
#         return F(n-1) + F(n-2)
# print(F(19))
# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for n in numbers:
#         squared_numbers.append(n*n)
#     print(squared_numbers)
#     return squared_numbers

# numbers = [2,5,8,9]
# get_squared_numbers(numbers)
# my_array = [64, 34, 25, 6, 22, 11, 90, 12]

# n = len(my_array)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1, n):
#         if my_array[j] < my_array[min_index]:
#             min_index = j
#     min_value = my_array.pop(min_index)
#     my_array.insert(i, min_value)

# print("Sorted array:", my_array)
# my_array = [7,3,9,12,11]
# n = len(my_array)
# for i in range(n-1):
#     swapped = False
#     for j in range(n-i-1):
#         if my_array[j]>my_array[j+1]:
#             my_array[j],my_array[j+1] = my_array[j+1],my_array[j]
#         swapped = True
#         if not swapped :
#             break
# print(my_array)
# print("Hello worlds")
# print("hello")
# def partition(array,low,high):
#     pivot = array[high]
# def quick_sort(array,low,high):
#     if low <high:
#         pivot = partition(array,low,high)
#         quick_sort(array,low,pivot-1)
#         quick_sort(array,pivot+1,high)
# def partition(array,low,high):
#     p = array[low]
#     i = low+1
#     j = high
#     while True:
#         while i<=j and array[i]<=p:
#             i+=1
#         while i<=j and array[j]>=p:
#             j-=1
#         if i<=j:
#             array[i],array[j] = array[j],array[i]
#         else:
#             break
#         array[low],array[j] = array[j],array[low]
#         return
# array =
# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1

#     for j in range(low, high):
#         if array[j] <= pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]

#     array[i+1], array[high] = array[high], array[i+1]
#     return i+1


# def quicksort(array, low=0, high=None):
#     if high is None:
#         high = len(array) - 1

#     if low < high:
#         pivot_index = partition(array, low, high)
#         quicksort(array, low, pivot_index-1)
#         quicksort(array, pivot_index+1, high)


# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# quicksort(my_array)
# print("Sorted array:", my_array)
# def countingSort(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)

#     while len(arr) > 0:
#         num = arr.pop(0)
#         count[num] += 1

#     for i in range(len(count)):
#         while count[i] > 0:
#             arr.append(i)
#             count[i] -= 1

#     return arr

# unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# sortedArr = countingSort(unsortedArr)
# print("Sorted array:", sortedArr)
# def countingSort(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)

#     while len(arr) > 0:
#         num = arr.pop(0)
#         count[num] += 1

#     for i in range(len(count)):
#         while count[i] > 0:
#             arr.append(i)
#             count[i] -= 1
#     return arr
# unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# sortedArr = countingSort(unsortedArr)
# print("Sorted array:", sortedArr)
# myArray= [170,45,75,90,802,24,2,66]
# print("ORIGINAL ARRAY:",myArray)
# radix_array = [[] for _ in range(10)]
# max_val = max(myArray)
# exp = 1
# while max_val // exp >0:
#     while len(myArray) >0:
#         val= myArray.pop()
#         radixIndex = (val//exp)%10
#         radix_array[radixIndex].append(val)
#     for bucket in radix_array:
#         while len(bucket)>0:
#             val = bucket.pop()
#             myArray.append(val)
#     exp*=10
# print("Sorted array:",myArray)
# import time
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]

#     sortedLeft = mergeSort(leftHalf)
#     sortedRight = mergeSort(rightHalf)

#     return merge(sortedLeft, sortedRight)


# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result


# unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
# sortedArr = mergeSort(unsortedArr)
# print("Sorted array:", sortedArr)
# # fruits = ['apple', 'banana', 'cherry']

# # for index , fruit in enumerate(fruits,start=1):
# #     print(index,fruit)

# start_time = time.time()

# # Your code here
# for i in range(1000000):
#     import time


# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]

#     sortedLeft = mergeSort(leftHalf)
#     sortedRight = mergeSort(rightHalf)

#     return merge(sortedLeft, sortedRight)


# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")


# start_time = time.time()

# # Your code here
# for i in range(1000000):
#     pass  # Example operation

# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")

# start_time = time.time()

# # Your code here
# for i in range(1000000):
#     array = [1,4,5,7,9,8,5,3]
#     array.sort()
#     print(array)

# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")
# from colorama import Fore
# print(Fore.YELLOW,"Hello world")
# print(Fore.RED,"Hello world")
# print(Fore.GREEN,"Hello world")
# print(Fore.BLUE,"Hello world")
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# head = Node(1)
# node1 = Node(2)
# node2 = Node(3)
# node3 = Node(4)
# node4 = Node(5)
# head.next = node2
# node2.next = node3
# node3.next = node4
# if head is not None:
#     head = head.next
# current = head
# while current is not None:
#     print(current.data, end=" ")
#     current.current.next
# class Node:
#     def __init__(self,data = None):
#         self.data = data
#         self.next = None
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = "NUll"
# print(node1.data,node1.next)
# print(node2.data,node2.next)
# print(node3.data,node3.next)
# print(node4.data,node4.next)
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node1.next= node2
# node2.next = node3
# node3.next = node4
# node4.next = None
# currentNode = node1
# while currentNode:
#     print(currentNode.data,end="-->")
#     currentNode = currentNode.next
# print("NULL")
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
# def traverse(self):
#     currentNode = self.head
#     while currentNode:
#         print(currentNode.data)
#         currentNode = currentNode.next
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# link = LinkedList()
# link.head = node1
# link.head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = None
# link.traverse()
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Linked_list:
#     def __init__(self):
#         self.head = None
#     def traverse(self):
#         currentNode = self.head
#         while currentNode:
#             print(currentNode.data)
#             currentNode = currentNode.next
#     def insert_at_the_beginning(self,data):
#         new_data= Node(data)
#         new_data.next = self.head
#         self.head = new_data
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# link = Linked_list()
# link.head = node1
# link.head.next = node2
# node2.next = node3
# node3.next = node4
# link.insert_at_the_beginning(5)
# link.traverse()
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Linked_list:
#     def __init__(self):
#         self.head = None
#     def traverse(self):
#         currentNode = self.head
#         while currentNode:
#             print(currentNode.data,end="->")
#             currentNode = currentNode.next
#         print("Null")
#     def insert_at_end(self,data):
#         new_data = Node(data)
#         currentNode = self.head
#         while currentNode.next!=None:
#             currentNode = currentNode.next
#         currentNode.next = new_data

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# link = Linked_list()
# link.head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4

# link.insert_at_end(5)
# link.insert_at_end(6)
# link.insert_at_end(7)
# link.traverse()
# class Node:
#     def __init__(self,data):
#         self.data =  data
#         self.next = None

# class Linked_list():
#     def __init__(self):
#         self.head = None

#     def traverse(self):
#         currentNode = self.head
#         while currentNode:
#             print(currentNode.data)
#             currentNode = currentNode.next

#     def insert_in_middle(self,insert_data,new_data):
#         new_node = Node(new_data)
#         new_node.next = insert_data.next
#         insert_data.next = new_node
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Linked_list:
#     def __init__(self):
#         self.head = None
#     def traverse(self):
#         currentNode = self.head
#         while currentNode:
#             print(currentNode.data,end="-->")
#             currentNode = currentNode.next
#     def insert_in_middle(self,insert_data,new_data):
#         new_node = Node(new_data)
#         new_node.next = insert_data.next
#         insert_data.next = new_node
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# link = Linked_list()
# link.head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# link.insert_in_middle(node3,8)
# link.traverse()
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Linked_list:
#     def __init__(self):
#         self.head = None
#     def traverse(self):
#         currentNode = self.head
#         while currentNode:
#             print(currentNode.data,end="-->")
#             currentNode = currentNode.next
#         print("NULL")
#     def remove(self,removeNode):
#         currentNode = self.head
#         while currentNode:
#             if(currentNode.next == removeNode):
#                 currentNode.next = removeNode.next
#             currentNode = currentNode.next
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# link = Linked_list()
# link.head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# link.remove(node2)
# link.traverse()


######################## PRINTING THE MIDDLE OR TWO MIDDLE NUMBERS###################################
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Linked_list:
#     def __init__(self):
#         self.head = None
#     def find_middle(self,list1):
#         counter = 0
#         currentNode = self.head
#         while currentNode:
#             currentNode = currentNode.next
#             counter +=1
#         print("Size of linked list:",counter)
#         currentNode = self.head
#         for i in range((counter-1)//2):
#             currentNode = currentNode.next
#         if counter%2 ==0:
#             nextNode = currentNode.next
#             print("Since the length of linked list is an even number the two middle elements are:")
#             print(currentNode.data,nextNode.data)
#         else:
#             print("since length of linked list is odd number, the middle element is :")
#             print(currentNode.data)
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# link = Linked_list()
# link.head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# link.find_middle(link)

############################ TRAVERSING THE DOUBLE LINKED LIST ##########################################
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
# class Linked_list:
#     def __init__(self):
#         self.head = None
#     def traverse(self):
#         currentNode = self.head
#         while currentNode:
#             print(currentNode.data,end = "-->")
#             currentNode = currentNode.next
#         print("NULL")
#     def reverse(self):
#         currentNode= selfcl
# def recursive_function():
#     return recursive_function()


# # Call the function to trigger the stack overflow
# recursive_function()
# class Stack:
#     def __init__(self,n):
#         self.stack = []
#         self.size = n
#     def push(self,element):
#         if len(self.stack)==self.size:
#             print("stack over flow error")
#         else:
#             self.stack.append(element)
#     def pop(self):
#         if(self.stack ==[]):
#             print("Stack is empty")
#         else:
#             self.stack.pop()
# s = Stack(3)
# s.push(6)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.stack)
# s.pop()
# print(s.stack)
# class Parenthesis_match:
#     openingBrackets = ["(","{","["]
#     closingBrackets = [")","}","]"]

#     def __init__(self,expression):
#         self.expression = expression
#         self.stack = []

#     def push(self,element):
#         self.stack.append(element)
#     def pop(self):
#         if self.stack ==[]:
#             print("unbalanced paranthesis")
#         else:
#             self.stack.pop()
#     def is_match(self):
#         print("Expression is =",self.expression)
#         if len(self.expression)%2 ==0:
#             for element in self.expression:
#                 print("Evaluating.... ",element)
#                 if element in self.openingBrackets:
#                     print("it is an opening bracket---",element,"pushing to stack")
#                     self.push(element)
#                 elif element in self.closingBrackets:
#                     x = self.stack.pop()
#                     print("time to pop element is",x)
#                     if self.openingBrackets.index(x) == self.closingBrackets.index(element):
#                         print("MATCH FOUND")
#                     else:
#                         print("match not found--check paranthesis")
#                         return
#                 else:
#                     print("unbalanced paranthesis")
# pm = Parenthesis_match("([{}])")
# pm.is_match()
# def peek():
#     global top
#     if top>= 0:
#         ele = a[top]
#         print(f"peeked:{ele}")
#         return ele
#     else:
#         print("Stack is empty.cannot peak")
#         return -1
# def is_empty():
#     return top ==-1
# def is_full():
#     return top>=MAX_SIZE
# class Stack:
#     def __init__(self):
#         self.STACK_CAPACITY = 101
#         self.stack_array = [""]*self.STACK_CAPACITY
#         self.top_index =-1
#     def push(self,character):
#         if self.is_full():
#             print(f"stack is full.cannot push:{character}")
#         else:
#             self.top_index+=1
#             self.stack_array[self.top_index] = character
#     def pop(self):
#         if self.is_empty():
#             print("stack is empty.cannot pop")
#             return None
#         else:
#             character = self.stack_array[self.top_index]
#             self.top_index -=1
#             return character
#     def is_empty(self):
#         return self.top_index ==-1
#     def is_full(self):
#         return self.top_index >=self.STACK_CAPACITY
# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, element):
#         self.stack.append(element)
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack.pop()
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack[-1]
#     def isEmpty(self):
#         return len(self.stack) == 0
#     def size(self):
#         return len(self.stack)
# # Create a stack
# myStack = Stack()
# myStack.push('A')
# myStack.push('B')
# myStack.push('C')
# print("Stack: ", myStack.stack)
# print("Pop: ", myStack.pop())
# print("Peek: ", myStack.peek())
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.size())
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def push(self, value):
#         new_node = Node(value)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#         self.size += 1

#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         popped_node = self.head
#         self.head = self.head.next
#         self.size -= 1
#         return popped_node.value

#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.head.value

#     def isEmpty(self):
#         return self.size == 0

#     def stackSize(self):
#         return self.size


# # Usage
# myStack = Stack()
# myStack.push('A')
# myStack.push('B')
# myStack.push('C')

# print("Pop: ", myStack.pop())
# print("Peek: ", myStack.peek())
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.stackSize())

# queue = []
# queue.append('A')
# queue.append('B')
# queue.append('C')
# print(queue)
# element = queue.pop(0)
# print("DeQUEUE",element)
# frontElement = queue[0]
# print("peek",frontElement)
# isEmpty = not bool(queue)
# print(isEmpty)
# print(len(queue))
# class Queue:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self,element):
#         self.queue.append(element)
#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.queue.pop(0)
#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty "
#         return self.queue[0]
#     def isEmpty(self):
#         return len(self.queue)==0
#     def size(self):
#         return len(self.queue)
# myQueue=Queue()
# myQueue.enqueue('A')
# myQueue.enqueue('B')
# myQueue.enqueue('C')
# print("Queue: ", myQueue.queue)
# print("Dequeue: ", myQueue.dequeue())
# print("Peek: ", myQueue.peek())
# print("isEmpty: ", myQueue.isEmpty())
# print("Size: ", myQueue.size())
# stack################################333
# max_size = 101
# a = [0]*max_size================
# top = -1
# def push(ele):
#     global top
#     if top <= max_size -1:
#         a[top] = ele
#         print(f"pushed:"{ele})
#     else:
#         print(f"stack is full. cannot push:{ele}")
# def pop():
#     global top
#     if top >=0:
############################## STACK############################################
# class Stack:
#     def __init__(self):
#         self.stack_capacity = 101
#         self.stack_array = ['']*self.stack_capacity
#         self.top_index =-1
#     def push(self,character):
#         if self.is_full():
#             print(f"stack is full .Cannot push:{character}")
#         else:
#             self.top_index+=1
#             self.stack_array[self.top_index] = character
#     def pop(self):
#         if self.is_empty():
#             print("Stack is empty.cannot pop")
#             return None
#         else:
#             character = self.stack_array[self.top_index]
#             self.top_index-=1
#             return character
#     def is_empty(self):
#         return self.top_index ==-1
#     def is_full(self):
#         return self.top_index>= self.stack_capacity-1
# if __name__ == "__main__":
#     input_string = "Hello,World!"
#     input_length = len(input_string)
#     char_stack = Stack()
#     for i in range(input_length):
#         current_char = input_string[i]
#         char_stack.push(current_char)
#     reversed_string = ""
#     while not char_stack.is_empty():
#         reversed_string+= char_stack.pop()
#     print(reversed_string)
# n = int(input("Enter the number to convert it into binary: ",))
# bin_num = 0
# place = 1

# while n > 0:
#     rem = n % 2
#     bin_num += rem * place
#     place *= 10
#     n //= 2  # Use floor division to avoid floating-point results
# print(bin_num)
# MAX_SIZE = 101
# a = [0] * MAX_SIZE
# top = -1


# def push(ele):
#     global top
#     if top <= MAX_SIZE - 1:
#         top += 1
#         a[top] = ele
#     else:
#         print(f"Stack is full. Cannot push: {ele}")


# def pop():
#     global top
#     if top >= 0:
#         ele = a[top]
#         top -= 1
#         return ele
#     else:
#         print("Stack is empty. Cannot pop.")
#         return -1


# def is_empty():
#     return top == -1


# def size():
#     return top + 1


# def decimal_to_binary(decimal):
#     # update the code below
#     return bin(decimal)[2:]

# if is_empty():
#     print("0")  # Special case for decimal = 0
#     return

#     while not is_empty():
#         print(pop(), end="")
#     print()


# if __name__ == "__main__":
#     t = int(input())

#     for _ in range(t):
#         decimal = int(input())
#         decimal_to_binary(decimal)
# class CircularQueue:
#     def __init__(self, max_size):
#         self.max_size = max_size
#         self.a = [0] * max_size
#         self.front = 0
#         self.rear = -1
#         self.current_size = 0
#     def is_empty(self):
#         if self.current_size == 0:
#             return True
#         else:
#             return False
#     def is_full(self):
#         if self.current_size == self.max_size:
#             return True
#         else:
#             return False

#     def size(self):
#         return self.max_size
#     def enqueue(self, item):
#         if self.is_full():
#             print("Queue is full. Cannot enqueue.")
#             return
#         self.rear = (self.rear + 1) % self.max_size  # Circular increment
#         self.a[self.rear] = item
#         self.current_size += 1

#     def dequeue(self):
#         if self.is_empty():
#             print("Queue is empty. Cannot dequeue.")
#             return -1  # Return a sentinel value or throw an exception
#         removed_item = self.a[self.front]
#         self.front = (self.front + 1) % self.max_size  # Circular increment
#         self.current_size -= 1
#         return removed_item


# # Enqueue elements from an integer array
# elements_to_add = [10, 20, 30, 40, 50]
# queue = CircularQueue(101)
# for element in elements_to_add:
#     queue.enqueue(element)
#     print("Enqueued:", element)

# # Check if the queue is empty
# print("Is the queue empty?", queue.is_empty())

# # Dequeue elements
# while not queue.is_empty():
#     removed_element = queue.dequeue()
#     print("Dequeued:", removed_element)

# # Check if the queue is empty again
# print("Is the queue empty?", queue.is_empty())
# print(CircularQueue.a[1])

# class CircularQueue:
#     def __init__(self,max_size):
#         self.max_size = max_size
#         self.a = [0]*max_size
#         self.front = 0
#         self.rear = -1
#         self.current_size = 0
#     def is_empty(self):
#         return self.current_size==0
#     def is_full(self):
#         return self.current_size==self.max_size
#     def size(self):
#         return self.current_size
#     def enqueue(self,item):
#         if self.is_full():
#             print("Queue is full.cannot enqueue")
#             return
#         self.rear= (self.rear+1)%self.max_size
#         self.a[self.rear] = item
#         self.current_size+=1
#     def dequeue(self):
#         if self.is_empty():
#             print("Queue is not empty.....cannot dequeue")
#             return -1
#         removed_item = self.a[self.front]
#         self.front = (self.front+1)%self.max_size
#         self.current_size -=1
#         return removed_item
# if __name__ == "__main__":
#     n = 10
#     queue = CircularQueue(101)
#     for i in range(1,n+1):
#         if i%2==1:
#             print(i,end=" ")
#         else:
#             queue.enqueue(i)
#     while not queue.is_empty():
#         print(queue.dequeue(),end=" ")
# class CircularQueue:
#     def __init__(self,max_size):
#         self.max_size =max_size
#         self.queue = [None]*self.max_size
#         self.front = 0
#         self.rear = -1
#         self.current_size = 0
#     def is_empty(self):
#         return self.current_size==0
#     def is_full(self):
#         return self.current_size==self.max_size
#     def size(self):
#         return self.current_size
#     def enqueue(self,item):
#         if self.is_full():
#             print("Queue is full.Cannot enqueue")
#             return
#         self.rear = (self.rear+1)% self.max_size
#         self.queue[self.rear] = item
#         self.current_size+=1
#     def dequeue(self):
#         if self.is_empty():
#             print("Queue is empty. Cannot dequeue")
#         removed_item = self.queue[self.front]
#         self.front = (self.front+1)%self.max_size
#         return removed_item
# import numpy as np
# x = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(x)
# import numpy as np
# x = [12,-28,-3,7]
# roots = np.roots(x)
# print(roots)
# from queue import Queue

# my_queue = Queue()

# my_queue.put(10)
# my_queue.put(20)
# my_queue.put(30)

# # Displaying the front element
# print("Front element:", my_queue.queue[0])

# # Displaying and removing elements
# print("Queue elements:", end=" ")
# while not my_queue.empty():
#     print(my_queue.get(), end=" ")
# print()

# # Checking if the queue is empty
# if my_queue.empty():
#     print("Queue is empty.")
# else:
#     print("Queue is not empty.")
# from queue import Queue
# my_queue = Queue()
# my_queue.put(10)
# my_queue.put(20)
# my_queue.put(30)

# temp_queue = Queue()
# while not my_queue.empty():
#     item = my_queue.get()
#     temp_queue.put(item)

#     if temp_queue.qsize()==1:
#         front_element = item
# while not temp_queue.empty():
#     my_queue.put(temp_queue.get())
# print(front_element)
# # Displaying and removing elements
# print("Queue elements:", end=" ")
# while not my_queue.empty():
#     print(my_queue.get(), end=" ")
# print()

# # Checking if the queue is empty
# if my_queue.empty():
#     print("Queue is empty.")
# else:
#     print("Queue is not empty.")
# max_size = 101
# a = ['']*max_size
# top = -1
# def push(ele):
#     global top
#     if top <= max_size-1:
#         top +=1
#         a[top] = ele
#     else:
#         print(f"stack is full.cannot push {ele}")
# def pop():
#     global top
#     if top >= 0:
#         ele = a[top]
#         top -=1
#         return ele
#     else:
#         print("stack is empty.cannot pop")
#         return -1
# def is_empty():
#     return top==-1
# def is_full():
#     return top>= max_size
# def is_matching_pair(open_char,close_char):
#     return (open_char == '')
# from sympy import primerange
# primes
# import pandas as pd
# s = pd.Series([1,3,5,7,9])
# df = pd.DataFrame({'A': [1,2,3],"B":[4,5,6]})
# print(s)
# print(df)
# class stack:
#     def __init__(self):
#         self.stack_capacity = 101
#         self.stack_array = ['']*self.stack_capacity
#         self.top_index = -1
#     def push(self,character):
#         if self.is_full():
#             print(f"Stack is full . Cannot push")
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next  = None
# def length(head):
#     length = 0
#     while head :
#         length+=1
#         head = head.next
#     return length
# def getMiddle(head):
#     length = length(head)
#     mid_index = length//2
#     while mid_index
########################### Nge or not#################################
#
# n = int(input())
# arr = list(map(int,input().split()))
# ngn = [-1]*n
# stack = []
# for i in range(n-1,-1,-1):
#     while stack and stack[-1] < arr[i]:
#         stack.pop()
#     if stack:
#         ngn[i] = stack[-1]
#     else:
#         ngn[i] = -1
#     stack.append(arr[i])
# print(*ngn)
# cook your dish here
# Read the number of tuples and some value k (not used in the code)
# cook your dish here
# n = int(input())
# pairs = []
# for _ in range(n):
#     pair = tuple(map(int, input().split()))
#     pairs.append(pair)
# print(pairs)
# def bubble_sort(arr,n):
# def bubble_sort(arr, n):
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]


# n = int(input())
# arr = list(map(int, input().split()))
# bubble_sort(arr, n)
# print(arr)
# import numpy as np
# # Read input for the size of the matrix
# N = int(input())
# # Create the matrix with numbers from 1 to N^2
# matrix = np.arange(1, N**2 + 1).reshape(N, N)
# # Flatten the matrix and print the elements as space-separated integers
# print(*matrix.flatten())a
# a = [[ 0 for j in range(3)] for i in range(2)]
# for i in range(2):
#     for j in range(3):
#         print(f"enter element at {i}th row, {j}th column :")
#         a[i][j] = list(map(int,input().split()))
# for i in range(2):
#     for j in range(3):
#         print( a[i][j],end=" ")
#     print("")
# Initialize a 2x3 matrix with zeros
# a = [[0 for _ in range(2)] for _ in range(2)]
# print(a)
# b=  [[0 for _ in range(2)] for _ in range(2)]
# c = [[0 for _ in range(2)] for _ in range(2)]
# # Input elements into the matrix
# for i in range(2):
#     for j in range(2):
#         a[i][j] = int(input(f"Enter element at {i}th row, {j}th column: "))
# # Display the matrix (optional)
# print("The matrix1 is:")
# for row in a:
#     print(row)


# for i in range(2):
#     for j in range(2):
#         b[i][j] = int(input(f"Enter element at {i}th row, {j}th column: "))
# print("The matrix2 is:")
# for row in b:
#     print(row)

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             c[i][j] += a[i][k] * b[k][j]
# print("the multiplied matrix is ")
# for row in c:
#     print(row)
# r =  int(input("Enter the rows of the matrix:",))
# c = int(input("Enter the columns of the matrix:",))
# mat = [[input() for j in range(c)] for i in range(r)]
# for row in range(r):
#     if row%2 ==0 :
#         print(*mat[row])
#     else:
#         print(*reversed(mat[row]))
# cook your dish here
# cook your dish here
# cook your dish here
# n = int(input())
# mat = [list(map(int, input().split())) for _ in range(n)]
# sum_p = 0
# sum_s = 0
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             sum_p += mat[i][j]
#         if i+j == (n-1):
#             sum_s += mat[i][j]
# print(sum_s+sum_p)
# cook your dish here
# n,m = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(m)]
# r = []
# for i in range(n):
#     for j in range(m):
#         if i==j:
#             r.append(a[i][j])
# r.sort()
# for k in range(len(r)):
#     for i in range(n):
#         for j in range(m):
#             if i==j:
#                 a[i][j] = r[k]
# for row in range(n):
#     print(*a[i])
# cook your dish here
# n,m = map(int,input().split())
# mat = [[int(input()) for _ in range(m)] for _ in range(n)]
# print(mat)
# def generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# a = generator()
# for i in a:
#     print(i)
# class myIter:
#     def __init__(self,data):
#         self.data = data
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index <len(self.data):
#             result = self.data[self.index]
# def my_function(*args):
#     print("number of arguments are:",len(args))
#     for arg in args:
#         print("arguments",arg)
# my_function(1,2,3,4,5,6,7,8,9,10)
# my_function('a','b','c')
# my_function(True)
# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")


# print_details(name="bunny", age="30", city="newyork", game="sunnny", soup="34", pity="tity")
# n = int(input("Enter the dimension value of n:",))
# mat = [list(map(int, input().split())) for i in range(n)]
# mat_n = [[0 for j in range(n)] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         mat_n[i][j] = mat[j][i]
# for row in range(n):
#     print(*mat_n[row][::-1])
# cook your dish here
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# ith = set()
# jth = set()
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             ith.add(i)
#             jth.add(j)
# for i in ith:
#     for j in range(m):
#         a[i][j] = 0
# for i in range(n):
#     for j in jth:
#         a[i][j] = 0

# for row in range(n):
#     print(*a[row])
# print(ith)
# print(jth)
# matrix##################################3
# m = int(input())
# a = [list(map(int,input().split())) for i in range(m)]
# count_1 =0
# count_2 = 0
# count_3 = 0
# for i in range(m):
#     if i==0:
#         for k in range(m):
#             if a[i][k] ==1:
#                 count_1+=1
#     elif i==1:
#         for k in range(m):
#             if a[i][k] == 1:
#                 count_2+=1
#     else:
#         for k in range(m):
#             if a[i][k] ==1:
#                 count_3+=1
# if count_1 >= count_2 and count_1>=count_3:
#     print(1)
# elif count_2 > count_1 and count_2>=count_3:
#     print(2)
# else:
#     print(3)
# print(count_1)
# print(count_2)
# print(count_3)

##############################################################################################################################################################################################
# n = int(input("Enter the value:",))
# a = [list(map(int,input().split())) for i in range(n)]
# sum_r1 = 0
# sum_c1= 0
# sum_rl =0
# sum_cl =0
# for i in range(n):
#     if i==0:
#         for k in range(n):
#             sum_r1+=a[i][k]
#             sum_c1+=a[k][i]
#     if i==2:
#         for k in range(n):
#             sum_rl += a[i][k]
#             sum_c1 += a[k][i]
# cook your dish here
# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# for row in range(1):
#     print(*matrix[row])
# arr = [4, 5, 68, 29, 49]
# l = len(arr)
# a = int(l/2)
# a1 = arr[:a]
# a2 = arr[a:]
# b = len(a2)
# stack = []
# i = 0
# j = 0
# print(a,b)
# print(a1)
# print(a2)
# while (i != a and j != b):
#     if a1[i] < a2[j]:
#         stack.append(a1[i])
#         i += 1
#     else:
#         stack.append(a2[j])
#         j += 1
# while i < a:
#     stack.append(a1[i])
#     i += 1
# while i < b:
#     stack.append(a2[j])
#     j += 1
# print(*stack)
# a1 = [10, 26, 2]
# a2 = [94, 55, 93]
# n1 =3
# n2 = 3
# a3 = []
# i = 0
# j = 0
# while (i != n1 and j != n2):
#     if (a1[i] < a2[j]):
#         a3.append(a1[i])
#         i += 1
#     else:
#         a3.append(a2[j])
#         j += 1

# while i < n1:
#     a3.append(a1[i])
#     i += 1
# while j < n2:
#     a3.append(a2[j])
#     j += 1
# print(*a3)
# def partition(arr,low,high):
#     pivot = arr[high]
#     i = low-1
#     for j in range(low,high):
#         if arr[j] <= pivot:
#             i+=1
#             arr[i],arr[j] = arr[j],arr[i]
#     arr[i+1],arr[high]  = arr[high],arr[i+1]

# n= int(input())
# a = sorted([int(input()) for _ in range(n)])
# print(*a)
# cook your dish here
# for _ in range(int(input())):
#     s = input()
#     count_m =0
#     count_s = 0
#     for i in range(len(s)-1):
#         if i == 'sm' or 'ms':
#             count_m +=1
#         elif i== 's':
#             count_s+=1
#     print(count_s,count_m)# cook your dish here
# cook your dish here
# for _ in range(int(input())):
#     n = int(input())
#     a = []
#     count = 0
#     for i in range(n):
#         a.append(list(map(int, input().split())))
#     for row in range(n):
#         for j in range(n):
#             a[row].sort()
#             if j == n-1 and a[row][-1] > a[row][-2]:
#                 count += a[row][-1]
#     print(count)
# cook your dish here
# for _ in range(int(input())):
#     n, d = map(int, input().split())
#     a = list(map(int, input().split()))
#     s = 0
#     a.sort(reverse=True)
#     i = 0
#     while (i < n-1):
#         if a[i] - a[i+1] < d:
#            s += a[i]+a[i+1]
#            i += 2
#         else:
#             i += 1
#     print(s)
# cook your dish here
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     s = []
#     for i in range(n):
#         if a[i] == a[i+1]:

#             s.append(a[i])
#             a.pop(i)
#             i+=2
#         else:
#             s.append(a[i])
#             s.pop(i)
#             i+=1
#     for i in range(len(a)):
#         s.append(a)
# print(s)
# print(a)for for
# cook your dish here
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     g = list(map(int, input().split()))
#     g.sort()
#     print(g)
#     a = sorted(list(set(g)))
#     print(a)
#     print(a[-1])
# def count_pairs_less_than_x(arr, x):
#     count = 0
#     for i in range(n):
#         for k in range(i+1, n):
#             if arr[i]+arr[k] < x:
#                 count += 1
#     return count


# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#     x = int(input())
#     print(count_pairs_less_than_x(arr, x))

# def sortArrayByParity(nums):
#     result = [0] * len(nums)
#     left, right = 0, len(nums) - 1

#     for num in nums:
#         if num % 2 != 0:
#             result[left] = num
#             left += 1
#         else:
#             result[right] = num
#             right -= 1
#     print(result)
#     # Reverse the even part to maintain relative order
#     result[left:] = result[left:][::-1]
#     print(result)
#     for i in range(len(nums)):
#         nums[i] = result[i]

# if __name__ == "__main__":
#     N = int(input())
#     nums = list(map(int, input().split()))
#     sortArrayByParity(nums)
#     print(" ".join(map(str, nums)))

# cook your dish here
# for _ in range(int(input())):
#     m, w = map(str, input().split())
#     a = set(list((m)))
#     b = set(list((w)))
#     if a.issubset(b):
#         print("Yes")
#     else:
#         print("no")
# cook your dish here
# from collections import defaultdict
# def longest_special_substring(s):
#     n = len(s)
#     left = 0
#     freq = defaultdict(int)  # Frequency dictionary
#     max_len = 0
#     # Function to find the alphabet index (f(β))
#     def f(char):
#         return ord(char) - ord('a') + 1
#     # Two-pointer approach (sliding window)
#     for right in range(n):
#         char = s[right]
#         freq[char] += 1
#         # Check if the current window is valid
#         while freq[char] > f(char):
#             freq[s[left]] -= 1
#             left += 1
#         # Update the maximum length of a valid substring
#         max_len = max(max_len, right - left + 1)
#     return max_len

# # Reading input
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     result = longest_special_substring(s)
#     print(result)
# import bisect
# a= list(map(int,input().split()))
# index = bisect.bisect_right(a, 9)
# if index < len(a) and a[index] == 9:
#     print("9 is present at index", index)
# else:
#       2,
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [1.0, 2.0, 3.0],
#     'C': ['a', 'b', 'c'],
#     'D': [True, False, True],
#     'E': pd.date_range('20230101', periods=3),
#     'F': [1, 2, None]
# })

# # Output datatypes of all columns
# print(df.dtypes)

# # Compehensive overview
# print(df.info())

# # Numeric columns
# numeric_columns = df.select_dtypes(include=[np.number]).columns
# print("Numeric columns:", numeric_columns)

# # String (object) columns
# string_columns = df.select_dtypes(include=['object']).columns
# print("String columns:", string_columns)

# # Boolean columns
# bool_columns = df.select_dtypes(include=['bool']).columns
# print("Boolean columns:", bool_columns)

# # Datetime columns
# date_columns = df.select_dtypes(include=['datetime']).columns
# print("Datetime columns:", date_columns)
# def max_sum_k_elements(a, k):
#     l = len(a)
#     le = 0
#     ri = l - 1
#     s = 0

#     if k >= l:
#         return sum(a)

#     for i in range(k):
#         if a[le] > a[ri]:
#             s += a[le]
#             le += 1
#         else:
#             s += a[ri]
#             ri -= 1

#     return s


# if __name__ == "__main__":
#     n, k = list(map(int, input().split()))
#     a = list(map(int, input().split()))

#     print(max_sum_k_elements(a, k))
# import sys

# data = sys.stdin.read()
# print("You entered:")
# print(data)
# def is_palindrome(s,left,right):
#     while left <right:
#         if s[left] != s[right]:
#             return False
#         left+=1
#         right-=1
# def valid_palindrome(s):
#     left = 0
#     right = len(s)-1
#     while left <right:
#         if s[left] != s[right]:
#             return is_palindrome(s,left+1,right) or is_palindrome(s,left,right-1)
#         left+=1
#         right-=1
#         return True
# if __name__=='__main__':
#     import sys
#     input = sys.stdin.read
# s = (input("Enter a string to check wether it is palindrome or not:",))
# if s[::-1] == s:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")
# s = (input("Enter a string to check wether it is palindrome or not:",))
# left = 0
# right = len(s)-1
# count = 0
# for i in range(len(s)):
#     if s[left] == s[right]:
#         count =0
#         left+=1
#         right-=1
#     else:
#         count = 1
#         break;

# # Print based on condition
# print("it is palindrome" if count == 0 else "it is not a palindrome")
# def min_max_difference(A, B, C):
#     i, j, k = 0, 0, 0
#     min_diff = float('inf')
#     while i < len(A) and j < len(B) and k < len(C):
#         max_diff = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(A[i] - C[k]))
#         min_diff = min(min_diff, max_diff)
#         # Move the pointer which points to the smallest element
#         if A[i] <= B[j] and A[i] <= C[k]:
#             i += 1
#         elif B[j] <= A[i] and B[j] <= C[k]:
#             j += 1
#         else:
#             k += 1
#     return min_diff


# T = int(input())
# for _ in range(T):
#     N_A, N_B, N_C = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     C = list(map(int, input().split()))
#     print(min_max_difference(A, B, C))
# cook your dish here
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
#     pg.write("hello akka iam coming")
#     time.sleep(0.5)
#     # Seding the messages by pressing enter
#     pg.press("Enter")
# import pyautogui as pg
# pg.moveTo(100,100,duration = 2)
# import pyautogui as pg
# import time
# pg.hotkey('ctrl','a')
# time.sleep(2)
# pg.press('delete')
# pg.sleep(5)
# pg.hotkey('ctrl','z')
# import pyautogui as pg
# import time
# pg.scroll(500)
# time.sleep(5)
# pg.scroll(-500)
# cook your dish here
# n,m = map(int,input().split())
# ma = [list(map(int,input().split())) for  _ in range(n) ]
# s = []
# t ,b ,l,r = 0,n-1,0,m-1
# for i in range(n-2):
#     for j in range(m):
#         s.append(ma[l][j])
#     for j in range(1,n):
#         s.append(ma[j][r])
#     for j in range(b,-1,-1):
#         s.append(ma[b][j])
#     for j in range(b+1):
#         s.append(ma[t+1][j])
# print(*s)
# n,m=map(int,input().split())
# matrix=[]
# for i in range(n):
#     matrix.append(list(map(int,input().split())))


# memo=[[0 for j in range(m)] for i in range(n)]


# for i in range(n):
#     for j in range(m):
#         if i==0 and j==0:
#             memo[i][j]=matrix[i][j]
#         elif i==0:
#             memo[i][j]=memo[i][j-1]+matrix[i][j]
#         elif j==0:
#             memo[i][j]=memo[i-1][j]+matrix[i][j]
#         else:
#             memo[i][j]=min(memo[i-1][j],memo[i][j-1])+matrix[i][j]

# # print(memo[n-1][m-1])
# n,k = map(int,input().split())
# a = [list(map(int,input().split())) for i in range(n)]
# m = [[0 for j in range(k)] for i in range(n)]
# for i in range(n):
#     for j in range(k):
#         if i==0 and j==0:
#             m[i][j] = a[i][j]
#         elif i==0:
#             m[i][j] = m[i][j-1]+a[i][j]
#         elif j==0:
#             m[i][j] = m[i-1][j] +a[i][j]
#         else:
#             m[i][j] = min(m[i-1][j],m[i][j-1])+a[i][j]
# print(m[n-1][k-1])
# cook your dish here
# s1, t1 = map(int, input().split())
# s = list(input())
# t = list(input())
# st = []
# l, r = 0, s1-1
# for i in range(r):
#     if s[i] == t[0]:
#         n = i
#     if s[i] == t[-1]:
#         k = i
# for i in range(n, k+1):
#     st.append(s[i])
# print(len(st))
# formatted = ''.join(map(str, st))  # Convert characters to strings and join them
# print(f"{formatted}")  # f-string with the formatted string
# cook your dish here
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     am = ''.join(map(str, a))
#     count = 0
#     l, r = 0, len(a)-1
#     while l <= r/2:
#         if a[l] != a[r]:
#             count += abs(a[l]-a[r])
#             l += 1
#             r -= 1
# print(count)
# from collections import deque
# for i in range(int(input())):
#     n = int(input())
#     dq = deque(map(int,input().split()))
#     ans = 0
#     while len(dq)>1:
#         x = dq.popleft()
#         y = dq.pop()
#         if x==y:
#             continue
#         ans+=1
#         if x>y:
#             dq.append(x-y)
#         else:
#             dq.append(y-x)
#     print(ans)
# cook your dish here
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     count= 0
#     for i in range(n):
#         if a[i]<=7:
#             count+=1
#         if count==7:
#             print(i+1)
# cook your dish here
# cook your dish here
# This line seems to be unnecessary, but you can leave it for the input format
# d = int(input())
# # Read input and split it into a list of strings
# g = list(map(str, input().split()))

# l, r = 0, len(g)
# h = r // 2  # Middle index

# # For even length, take the first half and reverse the second half
# # For odd length, exclude the center element in the comparison
# if r % 2 == 0:
#     b = g[h:]  # right half
#     left_part = g[:h]
# else:
#     b = g[h+1:]  # right half, excluding the center element
#     left_part = g[:h]

# # Now compare the left part to the reversed right part
# if left_part == b[::-1]:
#     print("Yes")
# else:
#     print("No")

# # Print the right half and the left half for debugging purposes
# print(b)
# print(left_part)
# cook your dish here
# for _ in range(int(input())):
#     n = int(input())
#     c = list(set(map(int, input().split())))
#     w = list(map(int, input().split()))
#     l = len(c)
#     count = 0
#     for i in range(l):
#         a = c[i]
#         count+=w[a]
#     print(count)
# def fib(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# n = int(input())
# print(fib(n))
# def Binary(n):
#     #Write your code here
#     return bin(n)[2:]

# n = int(input())
# print(Binary(n))
# a = int(input())
# b = 0
# place = 1
# while (a!=0):
#     rem = int(a%2)
#     b+= rem*place
#     place*=10
#     a = a/2
# print(b)
# cook your dish here
# for _ in range(int(input())):
#     m, x, y = map(int, input().split())
#     m1 = list(map(int, input().split()))
#     a = x*y
#     count = 0
#     for i in range(len(m1)):
#         c = m1[i]+ a
#         if c < 100:
#             count += 1
#         else:
#             count -= 1
#     print(count)
# cook your dish here
# cook your dish here
# def interleave(s1, s2, s3):
#     b = []
#     for i in range(len(s1)):
#         if i == len(s1)-1:


# s1 = input()
# s2 = input()
# s3 = input()
# interleave(s1, s2,s3)
# cook your dish here
# def interleave(s1, s2, s3):
#     b = []
#     for i in range(len(s1)):
#         if i == len(s1)-1:
#             b.append(s1[i-1:i+1])
#             b.append(s2[i-1:i+1])
#         if i == 0:
#             b.insert(i, s1[i])
#             b.insert(i+1, s2[i])
#     n = ''.join(b)
#     if s3==n:
#         print(True)
#     else:
#         print(False)


# s1 = input()
# s2 = input()
# s3 = input()
# interleave(s1, s2, s3)
# def is_interleave(s1,s2,s3):
#     if not s1 and not s2 and not s3:
#         return True
#     if s1 and s1[0] == s3[0]:
#         if is_interleave(s1[1:],s2,s3[1:]):
#             return True
#     if s2 and s2[0] == s3[0]:
#         if is_interleave(s1,s2[1:],s3[1:]):
#             return True
#     return False
# s1 = input()
# s2 = input()
# s3 = input()

# print(is_interleave(s1,s2,s3))
# from collections import Counter

# # Original Counter
# counter = Counter({'a': 2, 'b': 2, 'g': 1, 'd': 1})

# # Find and remove elements with a count of 1
# keys_to_remove = [key for key, count in counter.items() if count == 1]
# print(keys_to_remove)
# for key in keys_to_remove:
#     del counter[key]

# print(counter)  # Output: Counter({'a': 2, 'b': 2})
# print(len())
# cook your dish here
# from collections import Counter
# def longest_palin(s):
#     a = Counter(s)
#     g =0
#     key_to_remove = [key for key,count in a.items() if count==1]
#     for key in key_to_remove:
#         del a[key]
#     for key ,count in a.items():
#         g+=count

#     print(count-1)
# s = input()
# longest_palin(s)# cook your dish here

# def re_sum(n):
#     # If the number has only one digit, return it
#     if len(n) == 1:
#         return int(n)

#     s = sum(int(digit) for digit in n)
#     return re_sum(str(s))

# n = input()
# print(re_sum(n))
# cook your dish here
# def collatz_conjectrue(n, count=0):
#     while n!=1:
#         if n % 2 == 0:
#             count += 1
#             return collatz_conjectrue(int(n/2),count)
#         else:
#             count += 1
#             return collatz_conjectrue((n*3+1),count)
#     return count


# n = int(input())
# print(collatz_conjectrue(n))

# n = int(input())
# a = list(map(int,input().split()))
# b = []
# for i in range(1,n+1):
#     b.append(sum(a[:i]))
# print(b)
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int,input().strip().split()))
#     p =[]
#     s=[]
#     m = [0]*n
#     #prefix
#     for i in range(n):
#         p.append(sum(a[:i+1]))
#     #suffix
#     current_suffix = 0
#     for i in range(n - 1, -1, -1):
#         current_suffix += a[i]
#         s.append(current_suffix)
#     s.reverse()
# for i in range(n):
#     m[i] = p[i] +s[i]
# minium = min(m)
# for i in range(n):
#     if m[i] == minium:
#         print(i+1)
# cook your dish here
# import numpy as np
# n = int(input())
# a = list(map(int, input().split()))
# b = min(a)
# for i in range(len(a)):
#     if a[i] % b != 0:
#         a.pop(i)
# re = np.gcd.reduce(a)
# print(re)
# from itertools import combinations

# def all_possible_subsets():
#     # Read input
#     N = int(input())
#     arr = list(map(int, input().split()))

#     # Generate and sort all subsets
#     result = []
#     for r in range(0, N + 1):  # r is the size of the subset
#         for subset in combinations(arr, r):
#             result.append(list(subset))

#     # Sort the result lexicographically
#     result.sort()

#     # Print subsets in the required format
#     for subset in result:
#         print(" ".join(map(str, subset)))

# # Call the function
# # all_possible_subsets()
# from itertools import combinations
# def all_possible_subsets():
#     n = int(input())
#     arr = list(map(int,input().split()))
#     arr.sort()
#     result = set()
#     for r in range(n+1):
#         for subset in combinations(arr,r):
#             result.add(tuple(subset))
#     unique_subsets = sorted(result)
#     for subset in unique_subsets:
#         print(f"[{' '.join(map(str,subset))}]")
# all_possible_subsets()
# class CodeChef:
#     def __init__(self, n):
#         self.n = n
#         self.adjMat = [[0]*n for _ in range(n)]

#     def add_edge(self, u, v):
#         self.adjMat[u][v] = 1

#     def print_adj_matrix(self):
#         for row in self.adjMat:
#             print(" ".join(map(str, row)))


# def main():
#     n = int(input())
#     graph = CodeChef(n)
#     for _ in range(n-1):
#         u, v = map(int, input().split())
#         graph.add_edge(u, v)
#     graph.print_adj_matrix()


# if __name__ == "__main__":
#     main()
# def main():
#     n = int(input())

#     tree = [[] for _ in range(n)]

#     for _ in range(n - 1):
#         u, v = map(int, input().split())

#         tree[u].append(v)
#     for i in range(n):
#         for j in range(len(tree[i])):
#             print(f"element at {i, j}:", tree[i][j], end=" ")
#         print()


# if __name__ == "__main__":
#     main()
# a = [[]]*5
# print(a)
# for i in range(5):
#     b = int(input())
#     a[i].append(b)
#     print(a)
# print(a)
# n = int(input())
# a = [[]]*n
# for i in range(n):
#     a[i].append(int(input()))
# print(a)
# class Tree:
#     def __init__(self,n):
#         self.n = n
#         self.tree = [[] for _ in range(n+1)]
#     def add_edge(self,u,v):
#         self.tree[u].append(v)
#     def dfs(self,node):
#         print(node,end="")
#         for _ in self.tree[node]:
#             self.dfs(_)


# if __name__=='__main__':
#     n = int(input())
#     t = Tree(n)
#     for _ in range(n-1):
#         u,v = map(int,input().split())
#         t.add_edge(u,v)
#     t.dfs(1)
# from collections import deque ,defaultdict
# tree = defaultdict(list)
# print(tree)
# c= map(int,input().split())
# c = list(sum)
# count = 0
# for i in range(len(c)):
#     if int(c[i]) == 0:
#         count+=6
#     elif int(c[i]) ==1:
#         count+=2
#     elif int(c[i]) == 2:
#         count+=5
#     elif int(c[i]) == 3:
#         count+=5
#     elif int(c[i]) == 4:
#         count+=4
#     elif int(c[i]) == 5:
#         count +=5
#     elif int(c[i]) == 6:
#         count+=6
#     elif int(c[i]) == 7:
#         count+=3
#     elif int(c[i]) == 8:
#         count+=7
#     else:
#         count+=6
# print(count)
# from statistics import mode
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     m = mode(a)
#     print(m)
#     print(len(a)-(a.count(m)))
# cook your dish here
# cook your dish here
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     for i in range(len(a)):
#         if a[i] < 0:
#             a[i] = a[i]*-1
#     a.sort(reverse=True)
# #     print(sum(a[:k]))
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     for i in range(len(a)):
#         if a[i] < 0:
#             a[i] = a[i]*-1
#     a.sort(reverse=True)
#     print(sum(a[:k]))
# from collections import deque,defaultdict
# def main():
#     n = int(input())
#     tree = defaultdict(list)
#     for _ in range(1,n):
#         u,v = map(int,input().split())
#         tree[u].append(v)
#     q = deque()
#     vis = set()
#     q.append(1)
#     while q:
#         u = q.popleft()
#         print(u,end=" ")
#         vis.add(u)
#         for v in tree[u]:
#             if v not in vis:
#                 q.append(v)
#                 print(v)
# main()
# code here
# code here
# n = int(input())
# tree = [[] for _ in range(n-1)]
# for _ in range(0, n-1):
#     a, b = map(int, input().split())
#     tree[a].append[b]
# print(tree)
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.right_child = None
#         self.left_child = None

#     c
# n1 = Node("rootNode")
# n2 = Node("LeftChildNode")
# n3 = Node("rightChildNode")
# n4 = Node("left grandChildren")

# n1.left_child = n2
# n1.right_child = n3
# n2.left_child = n4
# name = " jhon"
# print(name.rstrip())
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# node1 = Node(int(input("Enter node1",)))
# node2 = Node(int(input("Enter node2",)))
# node3 = Node(int(input("Enter node3",)))
# node4 = Node(int(input("Enter node4",)))
# node1.next = node2
# node2.next = node3
# node3.next = node4
# currentNode= node1
# while currentNode:
#     print(currentNode.data,end="-->")
#     currentNode  = currentNode.next
# print("NULL")
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next= None
#         self.prev = None
# node1 = Node(int(input("Enter node1:",)))
# node2 = Node(int(input("Enter node2:",)))
# node3 = Node(int(input("Enter node3:",)))
# node4 = Node(int(input("Enter node4:",)))

# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# node3.next = node4
# node4.prev = node3

# print("traversing forward")
# currentNode = node1
# while currentNode:
#     print(currentNode.data,end="-->")
#     currentNode = currentNode.next
# print("Null")
# print("backward traversing")
# currentNode = node4
# while currentNode:
#     print(currentNode.data, end="-->")
#     currentNode = currentNode.prev
# print("Null")
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None


# node1 = Node(int(input("Enter node1:",)))
# node2 = Node(int(input("Enter node2:",)))
# node3 = Node(int(input("Enter node3:",)))
# node4 = Node(int(input("Enter node4:",)))
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node1
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


# node1 = Node(int(input("Enter node1:",)))
# node2 = Node(int(input("Enter node2:",)))
# node3 = Node(int(input("Enter node3:",)))
# node4 = Node(int(input("Enter node4:",)))
# node1.next  = node2
# node2.next = node3
# node3.next = node4
# node4.next = node1
# currentNode = node1
# startNode = node1
# print(node1.next.data)
# from collections import Counter


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# node1 = Node(int(input("Enter node1:",)))
# node2 = Node(int(input("Enter node2:",)))
# node3 = Node(int(input("Enter node3:",)))
# node4 = Node(int(input("Enter node4:",)))
# node1.next = node2
# node1.prev = node4
# node2.next = node3
# node2.prev = node1
# node3.next = node4
# node3.prev = node2
# node4.next = node1
# node4.prev = node3
# print("Traversing forward")
# currentNode = node1
# startNode = node1
# print(currentNode.data,end="-->")
# currentNode = currentNode.prev
# while currentNode!=startNode:
#     print(currentNode.data,end="-->")
#     currentNode = currentNode.next
# print("...")

# code here
# n = int(input())
# tree = [[] for _ in range(n-1)]
# for i in range(n-1):
#     u,v = map(int,input().split())
#     tree[u].append(v)
# print(tree)
# def quicksort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quicksort(arr, low, pi - 1)
#         quicksort(arr, pi + 1, high)

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low,high-1):
#         if arr[j] < pivot:
#             i = i + 1
#             arr[i] = arr[j]
#             arr[i + 1] =arr[high]
#     return (i + 1)
# arr = [4,8,9,10,23,54,78]
# print(quicksort(arr))# cook your dish here
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int,input().split()))
#     m = min(a)
#     ma =max(a)
#     for i in range(len(a)):
#         if a[i] == ma:
#             a[i] = 1
#         else:
#             a[i] = m
#     print(a)
# import sys
# input = sys.stdin.read
# data = input().splitlines()
# N = int(data[0])  # Size of the matrix
# matrix = []

# for i in range(1, N + 1):
#     row = list(map(int, data[i].split()))
#     matrix.append(row)

# print("Matrix\n:", matrix)
# print(data)for i in range(len(s)):
# s = list(input())
# for i in range(len(s)):
#         if s[i] =='0':
#             s[i] = '1'
#         else:
#             s[i] = '0'
# print(*s)
# cook your dish here
# for _ in range(int(input())):
#     s = list(input())
#     n = []
#     l = 0
#     r = len(s)-1
#     for i in range(len(s)):
#         if s[i] == '0':
#             n.append('1')
#         else:
#             n.append('0')
#     print(*n)
# cook your dish here
# for _ in range(int(input())):
#     s = input()
#     if s.find('010') or s.find('101'):
#         print("Good")
#     else:
#         print("Bad")
# s = input().lower()
# print(s)
# cook your dish here
# s = list(input().lower())
# n = int(input())
# count = 0
# for i in range(n):
#     a = list(input())
#     if a[i] in s:
#         count += 1
#     if len(s) == len(a):
#         print("Yes")
# cook your dish here
# Read the number of test cases
# for _ in range(int(input())):
#     # Read n (rows) and m (columns) for the matrix
#     n, m = map(int, input().split())

#     # Read x (number of rows with conditions) and y (another threshold value)
#     x, y = map(int, input().split())

#     c_f = 0  # Counter for 'F'
#     c_p = 0  # Counter for 'P'
#     c_u = 0  # Counter for others

#     c = []  # List to store results for each test case

#     # Process each row
#     for i in range(x):
#         # Read the row as a list of characters
#         row = list(map(str, input().split()))

#         # Reset the counters for this row
#         row_f = 0
#         row_p = 0

#         for char in row:
#             if char == 'F':
#                 row_f += 1
#             elif char == 'P':
#                 row_p += 1
#             # No need to count 'U' since it isn't being used directly

#         # Check the condition
#         if row_f >= x and row_p >= y:
#             c.append(1)
#         else:
#             c.append(0)

#     # Print the result as a space-separated string for the current test case
#     print(*c)
# cook your dish here
# import itertools
# for _ in range(int(input())):
#     n = int(input())
#     s = list(input())
#     a = []
#     for r in range(len(s) + 1):
#         subsets = itertools.combinations(s, r)
#         a.append(list(subsets))
#     print(a)    de
# def find_pascal_value(n,m):
#     if m==0 or m==n:
#         return 1
#     return print(find_pascal_value(n-1,m-1))
# n,m = map(int,input().split())
# find_pascal_value(n-1,m)
# print(bin(5)[2:])
# a = input()
# print(a[::-1])
# class Tree:
#     def __init__(self, n):
#         self.tree = [[] for _ in range(n + 1)]

#     def add_edge(self, u, v):
#         self.tree[u].append(v)

#     def dfs(self, node):
#         print(node, end=" ")
#         for child in self.tree[node]:
#             self.dfs(child)


# if __name__ == "__main__":
#     n = int(input())
#     tree = Tree(n)

#     for _ in range(n - 1):
#         u, v = map(int, input().split())
#         tree.add_edge(u, v)

#     # Start DFS from the root node
#     tree.dfs(1)
# from collections import deque,defaultdict
# tree = defaultdict(list)
# print(tree)
# from collections import defaultdict
# tree = defaultdict(list)
# tree[1].append(2)
# tree[1].append(5)
# tree[2].append(5)
# print((dict(tree)))
# n = int(input())
# tree = [[] for _ in range(n)]
# for i in range(n):
#     u, v = map(int, input().split())
#     tree[u].append(v)
# print(tree)
# class c:
#     def __init__(self):

#     def pop(self):
#         t =[]
#         return 1
# print(c.pop())
# class Tree:
#     def __init__(self, n):
#         self.tree = [[] for _ in range(n + 1)]  # 1-based index
#         self.n = n

#     def add_edge(self, u, v):
#         self.tree[u].append(v) # Since it's an undirected tree

#     def dfs(self, node):
#         print(node)
#         for child in self.tree[node]:
#             self.dfs(child)


# if __name__ == '__main__':
#     n = int(input())  # Number of nodes
#     tree = Tree(n)

#     for _ in range(n - 1):
#         u, v = map(int, input().split())
#         tree.add_edge(u, v)

#     tree.dfs(1)  # Print the nodes directly connected to node 1
# from collections import defaultdict
# def dfs(node,parent,level,adj,level_nodes):
#     if level ==k:
#         level_nodes.append(node)
#     for neighbor in adj[node]:
#         if neighbor != parent:
#             dfs(neighbor,node,level+1,adj,level_nodes)
# n,k = map(int,input().split())
# adj = defaultdict(list)
# for _ in range(n-1):
#     u,v = map(int,input().split())
#     adj[u].append(v)
#     adj[v].append(u)
# level_nodes = []
# dfs(1,-1,0,adj,level_nodes)
# print(*sorted(level_nodes))
# dist = [-1, 0, 1, 2, 1, 2, 2, 2]
# dist.pop(3)
# print(dist)
# cook your dish here
# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     b = list(s)
#     c = set(b)
#     new = []

#         for i in range(n):
#             if b[i] == '0':
#                 new.append(b[i])
#                 b.pop(i)
#         new.extend(b)
#         result = " ".join(new)
#         print(result)
# cook your dish here
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     d = list(map(int, input().split()))
#     n = []
#     for i in range(len(a)):
#         n.append(abs(a[i]-d[i]))
#     c = Counter(a)
#     print(c)
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4

# current = node1
# while(current != None):
#     print(current.data,end="->")
#     current = current.next
# print("None")
# Step 1: Define a Node class
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
#         else:
#             last = self.head
#             while last.next:
#                 last = last.next
#             last.next = new_node

#     # Method to print the linked list
#     def print_list(self):
#         current = self.head
#         while current:  # Traverse the list and print each node's data
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")  # Indicate the end of the list

# # Step 3: Create the LinkedList and take input


# def take_input():
#     linked_list = LinkedList()  # Create a new linked list
#     # Take number of nodes as input
#     n = int(input("Enter the number of elements in the linked list: "))
#     for _ in range(n):
#         # Input the value for each node
#         data = int(input("Enter the value for the node: "))
#         linked_list.append(data)  # Append the value to the linked list

#     print("\nThe linked list is:")
#     linked_list.print_list()  # Print the entire linked list


# # Run the input and create the linked list
# take_input()
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
# class Linked_list:
#     def __init__(self):
#         self.head = None

#     def insert_at_end(self,val):
#         new_node = Node(val)
#         if self.head is None:
#             self.head = new_node
#             return
#         Current = self.head
#         while Current.next:
#             Current = Current.next
#         Current.next = new_node
#     def last_value(self):
#         if self.head is None:
#             return -1
#         current = self.head
#         while current.next :
#             current = current.next
#         return current.value
# class Node:
#     def __init__(self,value):
#         self.val = value
#         self.next= None
# class Linked_list:
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
#         new_node.next = current.next
# class Node:
#     def __init__(self, val):
#         self.value = val
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insertAtEnd(self, value):
#         new_node = Node(value)

#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return

#         self.tail.next = new_node
#         self.tail = new_node

# def deleteNode(self, value):
#     # Case 1: If the head node needs to be deleted
#     if self.head is None:
#         return  # The list is empty, nothing to delete
#     if self.head.value == value:
#         self.head = self.head.next  # Move the head to the next node
#         return

# Case 2: Search for the node and delete it (node is in the middle or end)
# current = self.head
# while current.next:
#     if current.next.value == value:
#         current.next = current.next.next  # Remove the node from the list
#         if current.next is None:  # If the node was the tail, update the tail
#             self.tail = current
#         return
#     current = current.next

#     def printValues(self):
#         current = self.head
#         while current:
#             print(current.value, end=' ')
#             current = current.next
#         print()


# if __name__ == "__main__":
#     # Take input for n (number of elements) and x (value to delete)
#     n, x = map(int, input("Enter n and x: ").split())

#     # Create a new linked list
#     linked_list = LinkedList()

#     # Take input for the list of values to insert
#     vals = list(map(int, input("Enter the values: ").split()))
#     for a in vals:
#         linked_list.insertAtEnd(a)

#     # Delete the node with value x
#     linked_list.deleteNode(x)

#     # Print the linked list after deletion
#     linked_list.printValues()
# from collections
# import sys
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

# mp = {}

# for i, val in enumerate(arr):
#     mp[val] = i

# for val in arr:
#     print(mp[val], end=" ")
# print()
# import sys
# input = sys.stdin.read
# data = input().split()
# print(data)
# from collections import Counter


# def main():
#     import sys
#     input = sys.stdin.read
#     data = input().split()

#     n = int(data[0])
#     k = int(data[1])
#     s = data[2]
#     li = list(s)
#     freq = Counter(li)

#     for char, count in freq.items():
#         if (count >= k) and (65 <= ord(char) <= 90):  # Uppercase letters
#             print(char, end="")
#         if (count >= k) and (97 <= ord(char) <= 122):  # Lowercase letters
#             print(char, end="")


# # if __name__ == "__main__":
# #     main()
# a=[1,1,1]
# sum =0
# for char in a:
#     sum+=char
# print(sum)    
# cook your dish here
# Loop through the number of test cases
# for _ in range(int(input())):
#     # Read the number of elements in the current test case
#     n = int(input())
    
#     # Read the list of integers and store it in variable 'a'
#     a = list(map(int, input().split()))
    
#     # Initialize a dictionary to count the frequency of each element
#     freq = {}
    
#     # Iterate over each element in the list 'a'
#     for x in a:
#         # If the element 'x' is already in the frequency dictionary, increment its count
#         if x in freq:
#             freq[x] += 1
#         else:
#             # If 'x' is not in the dictionary, initialize its count to 1
#             freq[x] = 1
#     print(freq)
#     # Calculate the maximum frequency of any element in the list
#     # Then, print the result: total elements minus the maximum frequency
#     print(n - max(freq.values()))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def node_new(val):
    return Node(val)


def insert(root, element):
    if root is None:
        # Assigning first element of array as root
        root = element
        return node_new(element)

    current = root

    # We start traversal to insertion position from root
    while True:
        if element < current.val:
            # If the value is lesser, we find in left subtree where to insert
            if current.left is None:
                print(f"Inserting {element} in left of {current.val}")
                current.left = node_new(element)
                break
            else:
                # Repeat the process for left subtree which is also a BST
                current = current.left
        else:
            if current.right is None:
                print(f"Inserting {element} in right of {current.val}")
                current.right = node_new(element)
                break
            else:
                current = current.right

    return root


if __name__ == "__main__":
    arr = [8, 3, 10, 1, 6, 14]
    root = None

    for element in arr:
        root = insert(root, element)

    print("The BST is created!")
