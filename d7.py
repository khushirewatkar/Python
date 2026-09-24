# a = [1,2,3]
# print(type(a))

# print(bool(""))

# a=[1,2,3,4,5]
# # append single element add krta hai
# a.append(6)
# print(a)
# # extend multiple element ko add krta hai
# a.extend([7,8,9])
# print(a)

# positive,negative, zero
# ----
# multiplication table
# num=int(input("enter a number: "))
# for i in range(1,11):
#     print(num*i)


# # prime num
# num=int(input("enter a number: "))
# if num<=1:
#     print("not prime")
# for i in range(2,num+1):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#         print("prime")

# a=input("enter a string: ")
# print(a[::-1])

# palindrome
# a=input("enter a string: ")
# b=(a[::-1])
# if a==b:
#     print("palindrome")
# else:
#     print("not a palindrome")

# a=[90,654,23,76,34]
# large=a[0]
# for i in a:
#     if i>large:
#         large=i
# print(large)

def fact(num):
    if num==0:
        return 1
    
    return num * fact(num -1)
print(fact(3))