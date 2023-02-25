#9. Write a python program to find repeated numbers as well as frequency of repetition of numbers in a list of 20 user defined values?
num=[1,2,3,4,2,3,4,5,3,4,5,2,4,2,4,6,5,3,43,2]
for i in num:
    if i in num:
        a=num.count(i)
print(a)