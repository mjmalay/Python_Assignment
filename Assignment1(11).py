
#11. WAP to do following using string
#a) Check whether a string is palindrome or not
str=input("Enter a string wheather the strin is palindrome or not : ")
str=str.casefold()
str1=reversed(str)
if list(str)==list(str1):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#b) capitalize first and last character of each word in string
s=input("Enter a string :")
str1=list(s)
str1+='\0'
for i in range(len(str1)):
    if i==0 or str1[i-1]==' ':
       str1[i]=str1[i].upper()
    else: 
        if str1[i]==' ' or str1[i]=='\0':
           str1[i-1]=str1[i-1].upper()
print("Your string is : ","".join(str1))

#c)categories the password as low,medium and high
#        low – only numbers or alphabets and length less than 8
#        medium - number and alphabets and length more than 8
#        string - number, alphabet and special character should present  and length should be greater than 8
# str=input("Enter a password :")
# if (str==isalnum() or str==isalpha()) and len(str)<8:
#     print("The password is low")
# elif (str==isalnum() and str==isalpha()) and len(str)>8:
#     print("The password is medium")
# else:
#     if (str==isalnum() and str==isalpha() and str==str.index("#$@*&^/<,.")) and len(str)>8:
#         print("The pasword is high")

#d)Find the letter used maximum and minimum time in a string
str=input("Enter the string to find the letter used maximum and minimum time :")
maxChar=' '
maxCount=0
minCount=0
minChar=' '
for i in set(str):
     count=str.count(i)
     if count > maxCount:
         maxCount=count
         maxChar=i
     else:
         minChar=i
         
print("Letter maximum time used : ",maxChar)
print("Letter minimum time used : ",minChar)

#e) create a list to store unique character in string and another list  
#   to store frequency of repeatation of unique character available in first list in the string

