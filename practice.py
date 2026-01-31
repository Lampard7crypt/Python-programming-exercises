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
# Question 18

# import re
# passwords, value = [x for x in input("Enter: ").split(', ')], list()
# for password in passwords:
#     if len(password)<6 or len(password)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]", password):
#         continue
#     elif not re.search("[A-Z]", password):
#         continue
#     elif not re.search("[0-9]", password):
#         continue
#     elif not re.search("[$#@]", password):
#         continue
#     elif not re.search("\s", password):
#         continue
#     else:
#         pass
#     value.append(password)
    
# print(", ".join(value))

# ============================================================================================
# Question 19

# from operator import itemgetter
# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))

# print(sorted(l, key=itemgetter(0,1,2)))

# ============================================================================================
# Question 20

# class Numbers:
#     def __init__(self, n):
#         self.n = n
#     def putNumbers(self):
#         i = 0
#         while i<self.n:
#             j=i
#             i=i+1
#             if j%7==0:
#                 yield j

# i = Numbers(100).putNumbers()
# print(list(i))

# ============================================================================================
# Question 21 <--- A real nice one frrr!!!

# import math
# origin = [0, 0]
# for _ in range(4):
#     line = input("").split(" ")
#     if not line:
#         break
#     if line[0] == "LEFT":
#         origin[0] -= int(line[1])
#     elif line[0] == "RIGHT":
#         origin[0] += int(line[1])
#     if line[0] == "UP":
#         origin[1] -= int(line[1])
#     elif line[0] == "DOWN":
#         origin[1] += int(line[1])
#     else:
#         pass

# distance = round(math.sqrt((int(line[1]))**2 + (int(line[1]))**2))
# print(distance)

# ============================================================================================
# Question 22

# from collections import Counter
# words = [x for x in input().split(' ')]
# words.sort()
# print(dict(Counter(words))) # can also usedefaultdict or get()

# ============================================================================================
# Question 23 Hell NO!!

# ============================================================================================
# Question 24

# print(dict.get.__doc__) # Docstrings in the methods


# ============================================================================================
# Question 25

# class Question:
#     name = "Joe Goldberg" # Class param ie Question.name
#     def __init__(self, name=None):
#         self.name = name # instance param ie int.name
#     def __str__(self):
#         return "This is a class with name class var and instance var"
    
# person = Question("Tyler")
# print(person)
# print(person.name) # Tyler - instance var
# print(Question.name) # Joe Goldberg - Class var

# ============================================================================================
# Question 26

def sumoftwo(a: int, b: int)-> int:
    return a + b

# ============================================================================================
# Question 27, 28, 29, 30, 31, 32 <---- Too easy
# Question 34, 35, 36

# squares = dict()
# for i in range(0, 21):
#     squares[i] = i**2
    
# print(squares, "\n", list(squares.values()), "\n", list(squares.keys()))

# ============================================================================================
# Question 41

# lst = [(i, i**2) for i in range(1, 21)]
# print(lst)

# ============================================================================================
# Question 42

# mytup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(mytup[:5], "\n", mytup[5:])

# ============================================================================================
# Question 44

# boolean = input("Enter: ")
# if boolean.lower() == "yes":
#     print("Yes")
# else:
#     print("No")

# ============================================================================================
# Question 45

# print(list(filter(lambda x: x%2==0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# ============================================================================================
# Question 46

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10]
# print(list(map(lambda x: x*x, lst)))

# ============================================================================================
# Question 47

# sqe = map(lambda x: x*x, filter(lambda x: x%2==0, lst))
# print(list(sqe))

# ============================================================================================
# Question 50

class American:
    def __init__(self):
        pass
    @staticmethod # Methods in python not particular to classes or objects. 
    def printNationality():
        print("American")
    
# ============================================================================================
# Question 51

class NewYorker(American):
    def __init__(self):
        super().__init__()
    
# ============================================================================================
# Question 52

import math
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    def calculateArea(self):
        return round(math.pi * self.radius**2)
    
# ============================================================================================
# Question 53

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
# ============================================================================================
# Question 54

class Shape:
    def __init__(self) -> None:
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

# ============================================================================================
# Question 56

try:
    print(5/0)
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("I am atomic")
    
# ============================================================================================
# Question 57

class MyError:
    def __init__(self, msg) -> None:
        self.msg = msg

error = MyError("Something went wrong")

# ============================================================================================
# Question 58

import re


