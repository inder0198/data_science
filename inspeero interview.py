# 1) Write a program to print below series upto 'N' number.
# Note: 'N' is taken from user
# o/p : 0 1 2 6 12 25 48 91 ....... N
# n = int(input("enter n:"))
#
#
# def fib(n):
#     a = [0, 1]
#     if n < 2:
#         return a[n]
#     while len(a) <= n:
#         b = a[-1] + a[-2]
#         a.append(b)
#     return a[n]
#
#
# for i in range(n):
#     print(i * fib(i))


#nnn

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
#
#
# for i in range(1,11):
#     print(i*fib(i))


# Given an array numbers,write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# If the total sum of the array elements is greater than 20 then remove all 0's from array .
# For example, given numbers = [0, 1, 0, 3, 12], after calling your function, numbers should be [1, 3, 12, 0, 0]. Another example given numbers = [0, 1, 0, 3, 17],
# after calling your function, numbers should be [1, 3, 17].
# a = [0, 1, 0, 3, 12]
# b = [0, 1, 0, 3, 17]
#
# def x(a):
#     if sum(a) > 20:
#         for i in a:
#             if i == 0:
#                 a.remove(i)
#     else:
#         for i in a:
#             if i == 0:
#                 a.append(i)
#                 a.remove(i)
#     print(a)
#
# x(a)
# x(b)


# 3) Given a string containing just the characters '(' and ')', find the maximum number of occurrences of longest valid (well-formed) parentheses substring.
# For Ex"(()", the longest valid parentheses substring is "()", which has max occurrence = 1.
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has maximum occurrence = 1.
# Another example is ")()()))()())", where the longest valid parentheses substring is "()()", which has maximum occurrence = 2.

# a="(()"
# b=")()())"
# c1=")()()))()())"
# d="))))()()((((()()))()()"
# import re
# c=0
# l=list(d)
# for i in range(len(l)):
#     if l[i]=="(":
#         if l[i+1]==")":
#             c=c+1
#
# if c==1:
#     print(c)
# else:
#     print(c//2)

#
# 2. write a program to to take an input integer array from user and separate all even numbers and odd numbers
# from given array and arrange in sequence of first even number then odd number then again even number
# and odd number. example : input : {5 ,7 ,2 ,3 ,8 ,99 ,102,6} even numbers 2,8,102,6 odd numbers 5,7,3,99
# output: {2,5,8,7,102,3,6,99}
#
# n=int(input("enter how may numbers u want to enter:"))
# b=[]
# c=[]
# for j in range(n):
# 	i=int(input("enter numbers:"))
# 	if i%2==0:
# 		b.append(i)
# 	else:
# 		c.append(i)
# print("even numbers:",b,"\nodd numbers:",c)
# x=1
# for i in c:
# 	b.insert(x,i)
# 	x+=2
# print("result:",b)

#
# 3. write a program to print following pattern take n input from user
# 0
# 2 4
# 6 8 10
# 12 14 16
# 18 20 22 24
# 26 28 30 32 34
# 36 38 40 42 44 46


# n=int(input("enter number of rows:"))
#
# f=0
# for i in range(1,n+1):
# 	f+=i
#
# a=[]
# for i in range(f):
# 	a.append(i*2)
#
# x=0
# for i in range(1,n+1):
# 	for j in range(i):
# 		print(a[x],end="  ")
# 		x+=1
# 	print()