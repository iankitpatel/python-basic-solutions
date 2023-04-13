#printing hello world
#print("hello world!")
# printing first natural numbers
#using while loop
# num=int(input("enter a number:"))
# i=1
# while i<=num:
#     print(i, end=" ,")
#     i+=1
#using for loop
# num=int(input("enter a number:"))
# i=1
# for i in range(1,num+1):
#     print(i, end=" ")
#voting system
# age=int(input("enter your age:"))
# if age<=17:
#     print(" you cannot vote")
# elif age<=10:
#     print("you are a kid you cant vote:")
# else:
#     print("you are adult now you can vote")

#positive and negative number
#method 1
# num=int(input("enter a number:"))
# if num>0:
#     print("number is positive ")
# elif num<0:
#     print("number is negative")
# else:
#     print("number is zero")
#method 2
# num=int(input("enter a number"))
# if num>=0:
#     if num>0:
#         print("number is positive")
#     else:
#         print("number is zero")
# else:
#     print("number is negative")
#method 3
# num=int(input("enter a number:"))
# if num==0:
#     print("nuber is zero")
# else:
#     result="number is positive" if num>0 else "num is negative"
#     print(result)
#printing all operations
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
#
# sum = a + b
# sub = a - b
# product = a * b
# quo = a / b
# flr_quo = a // b
# mod = a % b
# power = pow(a,b)
# print("sum:", sum)
# print("subtraction:", sub)
# print("product:", product)
# print("quotient:", quo)
# print("Floor quotient:", flr_quo)
# print("remainder:", mod)
# print("power:", power)
#checking if the number is even or odd
# num=int(input("enter a number :"))
# if num%2==0:
#     print("number is a even:")
# else:
#     print("number is odd")
#method 2
# num=int(input("enter a number :"))
# result= "number is even " if num%2==0 else "number is odd"
# print(result)

#grading system
# marks=int(input("enter your marks:"))
# if marks<0 or marks>100:
#     print("invalid")
# elif marks<50:
#     print("grade F")
# elif marks>=50 and marks<60:
#     print("grade D")
# elif marks>=60 and marks<70:
#     print("grade C")
# elif marks>=70 and marks<80:
#     print("grade B")
# elif marks>=80 and marks<90:
#     print("grade A")
# else:
#     print("grade A+")
# round of the numbers:-

# import math
# n=float(input("enter a number:"))
# print(math.ceil(n))
# print(math.floor(n))
# print(round(n))

# sqare root and cube root of a numbers:-

# import math
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# c=int(input("enter a number: "))
#
# sqroot=math.sqrt(a)
# square=b**2
# cube=c**(1/6)
#
# print("square root is :", sqroot)
# print("square  is :", square)
# print("cube root is :", cube)

# multiples/table of a number

# num=int(input("enter a number: "))
# print("mulltiplication of a table is: ")
# for i in range (1,11):
#      print(num,'x',i,'=',num*i)

# greatest of two numbers:-
# a=int(input("enter a first number:"))
# b=int(input("enter a second number:"))
#
# if a==b:
#     print("both numbers are equal!")
# elif a>b:
#     print(str(a) + "is greater" )
# else:
#     print(str(b) + "is greater")

# method 2:
# first=int(input("enter first number: "))
# second=int(input("enter second number: "))
# if first==second:
#     print("both numbers are equal:)")
# else:
#     result=first if first>second else second
#     print(str(result)+ "is greatest")

# greatest of three numbers

# first=int(input("enter first number: "))
# second=int(input("enter second number: "))
# third=int(input("enter third number: "))
# if first>second and first>third:
#     print(str(first) +"is greatest")
# elif second>first and second>third:
# #     print(str(second) + "is greatest")
# # else:
# #     print(str(third) + "is greatest")
#
# # method 2:
#
# first=int(input("enter first number: "))
# second=int(input("enter second number: "))
# third=int(input("enter third number: "))
#
# result=max(first,max(second,third))
# print(str(result) + "is greatest")

# N power of number: (using builtin function)
# base=int(input("enter base number :"))
# expo=int(input("enter expo number :"))
# temp=pow(base,expo)
# print(temp)

# without using inbuilt function:
# base=int(input("enter base number :"))
# expo=int(input("enter expo number :"))
# result=1
# while expo!=0:
#     result*=base
#     expo-=1
# print(result)
# print(expo)

# break statement :
# question1- Write a program to print all numbers between two intervals, namely low and high. But, with a special condition that if any number in the range while getting printed becomes divisible by 13 then you must not print anything further and stop. (Do this using the Break Statement)
#
#
# Example -
#
# Input -
#
# 1 10
#
# Output
#
# 1 2 3 4 5 6 7 8 9 10
#
#
#
# Input
#
# 10 20
#
# Output
#
# 10 11 12 13
#
#
#
# Input
#
# -18 0
#
# Output
#
# -18 -17 -16 -15 -14 -13

# solution using for loop;

# low,high=input("enter numbers: ").split(" ")
# for i in range(int(low),int(high)12+1):
#     print(i,end=" ")
#     if i%13==0:
#         break

# using while loop:
# list1=list(map(int,input("enter numbers: ").split()))
# low=list1[0]
# high=list1[1]
# while low<=high:
#     print(low,end=" ")
#     if low%13==0:
#         break
#     low+=1

# continue statement:

# Write a program to print all numbers between two intervals, namely low and high. But, with a special condition that numbers divisible by 5 must not be printed and skipped. (Do this using continue Statement)

# using for loop

# low,high=input("enter two numbers : ").split(" ")
# for i in range (int(low),int(high)+1):
#     if i%5 == 0:
#         continue
#     print(i,end=" ")

# implenting 2D array or list:
# method 1

# R=int(input("enter the number of rows: "))
# C=int(input("enter the number of columns: "))
#
# # initialize matrix
#
# matrix=[]
# print("enter th entries row wise: ")
#
# # For user input
# for i in range(R):  # A for loop for row entries
#     a=[]
#     for j in range (C):  # A for loop for column entries
#         a.append(int(input()))
#     matrix.append(a)
#
# # For printing the matrix
# for i in range(R):
#     for j in range(C):
#         print(matrix[i][j],end=" ")
#     print()

# method2

R=int(input("enter the number of rows: "))
C=int(input("enter the number of columns: "))

# initialize matrix

matrix=[]
print("enter th entries row wise: ")

# For user input

matrix=[[int(input())for x in range (C)]for y in range (R)]
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j],end=" ")
    print()
