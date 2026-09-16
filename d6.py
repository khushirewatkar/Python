# def khushi():
#     print("hello khushi")
# khushi()


# default argument
# def greet(name):
#     print("hello "+name)
# greet("khushi")
# greet("chinmay")

# def add(a,b):
#     c=a+b
#     print(c)
# num1=int(input("enter A: "))
# num2=int(input("enter B: "))
# add(num1,num2)

# def d1():
#     print("d1: hello")
# def d2():
#     return "d2: hello"
# print(d1())
# print(d2())
# //print() only displays the value.
# //return sends the value back to the caller, where it can be stored or used.


# keyword argument
# def s(name,age):
#     print(name,age)
# s(name="khushi",age=21)

# variable scope
# x=100
# def show():
#     y=50
#     print(x)
#     print(y)
# show()

# def sq(x):
#     print(x*x)
# sq(9)

# sq= lambda x:x*x
# print(sq(9))

# nums=[1,2,3,4]
# sq=list(map(lambda x:x*x,nums))
# print(sq)

# nums=[1,2,3,4,5,6]
# fil=list(filter(lambda x:x%2==0,nums))
# print(fil)

# name=["khushi","sani"]
# age=[20,21]
# res=list(zip(name,age))
# print(res)

# def countdown(n):
#     if n==0:
#         return
#     print(n)
#     countdown(n-1)
# countdown(5)


# 1
# def area():
#     a=3.14*r*r
#     print(a)
# r=int(input("enter radius: "))
# area()


# 2
# def check(n):
#     if (n%2==0):
#         print("Even")
#     else:
#         print("Odd")
# n=int(input("Enter n: "))
# check(n)

# 3
# def large(a,b,c):
#     if a>b and a>c:
#         print(a," is greatest..")
#     elif b>a and b>c:
#         print(b," is greater")
#     else:
#         print(c," is greater")
# a=int(input("enter value: "))
# b=int(input("enter value: "))
# c=int(input("enter value: "))
# large(a,b,c)

# 4
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n* fact(n-1)
# print(fact(3))


# text= "khushi"
# rev=""
# for i in text:
#     rev= i+ rev
# if text == rev:
#     print("Palindrome")
# else:
#     print("not a palindrome")

# 5
# def palindrome(word):
#     rev=""
#     for i in word:
#         rev= i+ rev
#     if word == rev:
#         print("Palindrome")
#     else:
#         print("not a palindrome")
# palindrome("khushi")

# # 6
# def count(word):
#     vowel=0
#     for i in word:
#         if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#             vowel=vowel+1
#     print(vowel)
# count("khushi")

# 7
# ab=lambda x:x**3
# print(ab(2))

# 8
# temp=[20,25,30]
# ab=list(map(lambda x:x/2,temp))
# print(ab)

# 9
# temp=[20,45,60,80,10]
# ab=list(filter(lambda x:x<50,temp))
# print(temp)

# 10
# def is_prime(num):
#     if num<=1:
#         print("not a prime number/false")
#     for i in range(2,num+1):
#         if num%i==0:
#             print("not a prime number/false")
#             break
#     else:
#             print("prime number/ true")
# is_prime(17)

