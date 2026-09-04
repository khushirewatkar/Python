# FOR LOOP
#  for i in range(5):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(10,1,-1):
#     print(i)


# WHILE LOOP
# i=1
# while i<=5:
#     print(i)
#     i+=1


# BREAK LOOP
# for i in range(5):
#     if i==5:
#         break
#     print(str(i)+ " khushi")


# for i in range(3):
#     for j in range(3):
#         print(i,j)

# Pattern printing
# for i in range(5):
#     print("*" * (i+1))
# for i in range(5,0,-1):
#     print("*" * (i+1))
# print("*")

# for i in range(1,10):
#     print(i)

# for i in range(2,31,2):
#     print(i)

# for i in range(1,31,2):
#     print(i)

# for i in range(1,11):
#     print(f"5 x {i} = {5*i}")


#  most imps
#Sum of all digits 
# sum=0
# for i in range(11):
#     sum=sum+i
# print(sum)


# Factorial
# fac=1
# for i in range(1,6):
#     fac=fac*i
# print(fac)

# reverse number
# num=input("enter the number: ")
# print(num[::-1])
    
# num=int(input("enter a number: "))
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print("Reverse: ",rev)

# count=0
# a= int(input("enter a number: "))
# while a>0:
#     count=count+1
#     a=a// 10
# print("count: "+str(count))

# a= (input("enter num: "))
# if a == a[::-1]:
#     print("Palindrome")
# else:
#     print("not a palindrome")

num=int(input("enter number: "))
if num <=1:
    print("not prime number")
else:
    for i in range(2,num):
        if num%i ==0:
            print("not a prime")
            break
    else:
        print("Prime")

# armstrong number

