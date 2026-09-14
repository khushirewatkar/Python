# # list
# fruits=["apple","mango","banana"]
# print(fruits)
# print(fruits[0])
# print(fruits[2])
# print(fruits[-1])

# fruits.append("orange")
# print(fruits)

# fruits.insert(1,"kiwi")
# print(fruits)

# fruits.remove("kiwi")
# print(fruits)

# fruits.pop(2)
# print(fruits)

# print(len(fruits))
# print(max(fruits))
# print(min(fruits))

# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)

# fruits.clear()
# print(fruits)


# Tuple
# marks=(90,83,76)
# print(marks)
# print(marks[1])


# #sets
# nums={1,2,3,4,5,6}
# print(nums)
# nums.add(7)
# print(nums)
# nums.remove(2)
# print(nums)

# a={2,4,6}
# b={1,3,5,2}
# print(a | b)
# print( a & b)
# print(a - b)

# # Dictonary
# s={
#     "name":"khushi",
#     "age":21,
#     "cgpa":8.88
# }
# print(s)
# print(s["name"])
# s["city"]="nagpur"
# print(s)
# del s["age"]
# print(s)

# print(s.items())

# for i,j in s.items():
#     print(i,j)

# Practice questions
# 1
# num=[2,3,1,4,5]
# print(min(num))
# print(sum(num))
# print(sum(num)//5)

# 2
# num=[10,11,15,20,30]
# evencount=0
# oddcount=0
# for i in num:
#     if i%2==0:
#         evencount=evencount+1
#     else:
#         oddcount=oddcount+1
# print(evencount)
# print(oddcount)

# 3.find second largest number
# num=[10,50,20,40]
# num.sort()
# print(num[-2])
        
# # 4. remove duplicate from list
# num=[1,2,2,3,4,4,5]
# new_l=[]
# for i in num:
#     if i not in new_l:
#         new_l.append(i)
# print(new_l)

# # 5.reverse a list
# num=[10,50,20,40]
# for i in range(len(num)-1,-1,-1):
#     print(num[i])

# # count frequency
# num=[1,2,2,3,3,3]
# visited=[]
# for i in num:
#     if i not in visited:
#         print(i,":",num.count(i))
#         visited.append(i)

# merge two list
# a=[1,2,3]
# b=[4,5,6]
# print(a + b)

# s={
#     "name":input("Enter a name: "),
#     "age":int(input("Enter age: ")),
#     "CGPA":float(input("Enter CGPA: "))
# }
# print(s)

# s={
#     "A":80,
#     "B":95,
#     "C":76
# }
# print(max(s.values()))

# a={1,2,3,4}
# b={3,4,5,6}
# print(a&b)

# Rotate a list by k positions.
# l1=[1,2,3,4,5]
# # k=2
# res=l1[-2: ]+l1[:-2]
# print(res)


# find missing number
# num=[1,2,3,5,6]
# print(num)
# n=max(num)
# for i in range(1,n+1):
#     if i not in num:
#         print("missing number: ",i)

# find all duplicates
list=[1,2,2,3,3,4,5,5]
seen=[]
dup=[]
for i in list:
    if i in seen and i not in dup:
        dup.append(i)
    else:
        seen.append(i)
print(dup)
