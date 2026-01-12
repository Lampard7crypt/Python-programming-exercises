# import sys
# lst1, lst2 = list(sys.argv[1:]), []
# def fact(num):
#     if num == 0:
#         return 1
#     return num * fact(num-1)

# for i in lst1:
#     lst2.append(str(fact(int(i))))
    
# print(', '.join(lst2))
# ===================================================================

# end = int(input())
# mydict = dict()

# for i in range(1, end+1):
#     mydict[i] = i*i
    
# print(mydict)
# ===================================================================
# Question 4

# numbers = list(input().split(', '))
# print(numbers, tuple(numbers))

# ===================================================================
# Question 5

# class MyClass:
#     def __init__(self):
#         self.string = ""
#     def getString(self):
#         self.string = input()
#     def printString(self):
#         print((self.string).upper())

# myclass = MyClass()
# myclass.getString()
# myclass.printString()

# ===================================================================
# Question 6
# from math import sqrt
# c, h, lst, d = 50, 30, [], input().split(", ")
# for i in d:
#     lst.append(round(sqrt((2*c*int(i))/h)))
    
# print(lst)

# ===================================================================
# Question 7, nested for loop ;(

# import numpy as np
# x, y = map(int, input().replace(' ', '').split(","))
# arr = np.zeros(shape=(x, y))
# for row in range(x):
#     for col in range(y):
#         arr[row][col] = row * col
# print(arr)
# ===================================================================
# Question 8

# words = list(input().split(", "))
# words.sort()
# print(", ".join(words))

# ===================================================================
# Question 9

# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;

# for sentence in lines:
#     print(sentence)

# ===================================================================
# Question 10

# words = [x for x in (input().split(' '))]
# words.sort()
# print(' '.join(words))

# ====================================================================
# Question 11


# def mysort(lst: list) -> list:
#     for j in range(1, len(lst)):
#         key = lst[j]
#         i = j -1
#         while i >= 0 and lst[i] > key:
#             lst[i+1] = lst[i]
#             i -= 1
#         lst[i + 1] = key
#     return lst

# print(mysort([5, 2, 4, 6, 1, 3]))

# Qiestion 13
# temp = {"Letters": 0, "Digits": 0}
# for letter in input("Enter alphanum str: "):
#     if letter.isdigit():
#         temp["Digits"] += 1
#     elif letter.isalpha():
#         temp["Letters"] += 1
#     else:
#         pass

# print("Letters", temp["Letters"], "Digits", temp["Digits"])

# ============================================================================================
# Question 14

# d = {"UPPERCASE": 0, "LOWERCASE": 0} 
# for char in input("Enter: "):
#     if char.isupper():
#         d["UPPERCASE"] += 1
#     elif char.islower():
#         d["LOWERCASE"] += 1

# print("UPPERCASE", d["UPPERCASE"], "LOWER", d["LOWERCASE"])

# ============================================================================================
# Question 15

# a = input("Enter: ")
# print(int(a) + int(a*2) + int(a*3) + int(a*4))

# ============================================================================================
# Question 16

# lst = [int(n)**2 for n in input("Enter: ").split(', ') if int(n)%2==1]
# print(lst)

# ============================================================================================
# Question 17


