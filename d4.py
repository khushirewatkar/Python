# name="khushi"
# city="nagpur"
# print(name)
# print(city)

# print(name[0])
# print(name[2])
# print(name[-2])

# text="PYTHON"
# print(text)
# print(text[0:3])
# print(text[2:])
# print(text[:4])
# print(text[0:6:2])

# text="PYTHON"
# print(text[::-1])

# text="PYTHON"
# print(text.lower())
# text="python"
# print(text.upper())
# text="hello python"
# print(text.title())
# text="hellow python"
# print(text.capitalize())

# text="  PYTHON  "
# print(text.strip())

# text=" I LIKE JAVA"
# print(text.replace("JAVA","PYTHON"))

# text="PYTHON"
# print(text.find("H"))
# print(text.count("T"))
# print(text.startswith("PY"))  

# text="PYTHON"
# print("Py" in text)
# print("PY" in text)

# text="Python"
# for i in text:
#     print(i)

# text="Python"
# count=0
# for i in text:
#     if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         print(i+" is a vowel")

# text="Python"
# count=0
# for i in text:
#     if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         count=count+1
# print("Count: "+str(count))

# text="Python"
# countUpper=0
# countLower=0
# for i in text:
#     if (i.isupper()):
#         print(i +" is upper")
#         countUpper=countUpper+1
#     else:
#         print(i + " is lower")
#         countLower=countLower+1
# print("Count of Upper string is "+str(countUpper))
# print("Count of Lower string is "+str(countLower))


# text="Python"
# rev=""
# for i in text:
#     rev= i +rev
# print(rev)

# text= "khushi"
# rev=""
# for i in text:
#     rev= i+ rev
# if text == rev:
#     print("Palindrome")
# else:
#     print("not a palindrome")

# text="python is awsome"
# words=text.split()
# count=0
# for i in words:
#     count=count+1
# print(count)

# text="python is awsome"
# print(text.replace(" ",""))

# text="python is awsome"
# print(text.replace(" ","_"))

# text="banana"
# for i in text:
#     print(f"{i}: {text.count(i)}")

# w1="listen"
# w2="silent"
# if sorted(w1)== sorted(w2):
#     print("anagram")
# else:
#     print("not anagram")

# text="aaabbcccc"
# count=1
# print(len(text))
# for i in range(len(text)-1):
#     if text[i]==text[i+1]:
#         count+=1
#     else:
#         print(text[i]+str(count),end="")
#         count=1
# print(text[-1]+str(count))


# text="aabbccddef"
# count=0
# for i in range(len(text)-1):
#     if text[i]==text[i+1]:
#         # print("")
#         pass
#     else:
#         print(text[i])


