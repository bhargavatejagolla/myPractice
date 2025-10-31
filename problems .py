# from math import perm
# n= int(input("enter the number of students:",))
# r = int(input("enter the number of chairs:",))
# def facts(s):
#     if s==0:
#         return 1
#     else:
#         return s*(s-1)
# print(facts(n)/facts(n-r))

# list1 = [23,45,65,78]
# list1[0], list1[3] =list1[3], list1[0]
# print(list1)
###geeks for geeks ########
# def swapPositions(list ,pos1, pos2 ):
#     first_ele = list.pop(pos1)
#     second_ele = list.pop(pos2 -1)
#     list.insert(pos1,second_ele)
#     list.insert(pos2 ,first_ele)
    
#     return list
# list =[23 , 65 , 19, 90]
# pos1, pos2 = 1, 3
# print(swapPositions(list,pos1 -1 ,pos2-1))
# list = [ 23, 54, 67 ,82]
# print("the list is :", str(list))
# counter = 0
# for i in list:
#     counter+=1
# print("length of the list is :", str(counter)) 
# import numpy as np

# a = int(input("enter the first number:",))
# b = int(input("enter the second number:",))
# c = np.maximum(a ,b)
# print("The maximum number is :",c)
# txt = "iron man is the only super hero without powers and he is immortal"
# s =txt.split("")
# for i in s:
#     if len(i)%2 ==0:
# n = "hello world iam robo "
# s = n.split(' ')
# for i in s :
#     if len(i)%2 == 0:
#         print(i)
# word = "hello world iam robo"
# a = word.split(" ")[  : :-1]
# l = []
# for i in a:
#     l.append(i)
# print(" ".join(l))
# def rev_sentence(sentence):
#     words = sentence.split(" ")
#     reverse_sentence = ' '.join(reversed(words))
#     return reverse_sentence
# if __name__ == "__main__":
#     input = "hello this is bhargava teja "
#     print(rev_sentence(input))
# sentence = "hello world iam robo 2.0 and iam came to kill bird man"
# a = sentence.replace(' ',"")
# print(a)
# list = [ 2,5,4,6,7,89,90]
# i = int(input("enter the number wheather to check it is present in the list or not: ",))
# for i in list :
# list.clear()
# print(list)
# list.sort(reverse = True)
# print(list)

# a = sum(list)
# print(a)
# b = a/len(list)
# print(b
# import numpy as np
# list = [1,2,3,4,5,6]
# a = np.prod(list)
# print(a)
# from functools import reduce
# from operator import mul
# list = [2,3,4,5]
# result = reduce(mul,list)
# print(result)
# from operator import *
# list1 = [1,2,3,4,5]
# m = 1
# for i in list1:
#     m = mul(i ,m)
# print(m)
# from functools import reduce
# list1 = [1,2,3,4,5]
# rs = reduce((lambda x,y : x*y ), list1)
# print(rs)
# list = [23, 45,78,92,37,67]
# list.sort()
# print(list[-2])
# list1 =[ 10,20,4,45,99]
# new_list = set(list1)
# new_list.remove(max(new_list))
# print(max(new_list))
# list = [1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     if i%2 ==0:
#         a= print(i, end =' ')
# for i in range(1, 101):
#     if i %7 ==0 and i%5 !=0:
#         print(i, end =' ')

# print("the original list is ", str(list))
# res = [x for x in list if x!=[]]
# print("list after empty list removal:", str(res))
# list1 = [5,6,[],3, [],[],90]
# # res = list(filter(None,list1))
# # print(res)
# while [] in list1 :
#     list1.remove([])
# print(list1)
# n= int(input("enter the number to find its square :",))
# d =dict()
# for i in range(1,n+1):
#     d[i] = i*i
# print(d)    
# import numpy as np
# d = int(input("enter the number :",))
# Q = np.multiply(200,d) 
# c = np.divide(Q ,30)
# E = np.sqrt(c)
# 
# def generate_2d_array(X, Y):
#     # Initialize the 2D array
#     array = []
    
#     # Loop through rows (0 to X-1)
#     for i in range(X):
#         # Initialize a new row
#         row = []
        
#         # Loop through columns (0 to Y-1)
#         for j in range(Y):
#             # Calculate the value for this cell
#             row.append(i * j)
        
#         # Add the row to the array
#         array.append(row)
    
#     return array

# # Example usage
# X = 3
# Y = 5
# result = generate_2d_array(X, Y)
# print(result)item
# items =str(input().split(','))
# items.sort()
# print(','.join(items))


# items = str(input("enter the lines:",))
# words = [word for word in items.split(" ")]
# print("".join(sorted(list(set(words)))))
# def binary_to_decimal(binary_str):
#     return int(binary_str, 2)

# def is_divisible_by_5(binary_str):
#     decimal_number = binary_to_decimal(binary_str)
#     return decimal_number % 5 == 0

# def main():
#     binary_input = input("Enter a binary number: ")
#     if all(bit in '01' for bit in binary_input):  # Validate binary input
#         if is_divisible_by_5(binary_input):
#             print(f"The binary number {binary_input} is divisible by 5.")
#         else:
#             print(f"The binary number {binary_input} is not divisible by 5.")
#     else:
#         print("Please enter a valid binary number.")

# if __name__ == "__main__":
#     main()

