#8. Write a python program to find 1st,2nd and 3rd largest and smallest numbers in a list 20 user defined values.
list=[4,3,6,3,5,34,8,6,9,6,45,4,35,23]
#num.sort()
num=[]
for i in list: 
    if i not in num: 
        num.append(i) 
num.sort()
firstlarge=num[-1]
secondLarge=num[-2]
thirdLarge=num[-3]
firstSmall=num[0]
secondSmall=num[1]
thirdSmall=num[2]

print("First Largest = ",firstlarge,"Second Largest = ",secondLarge,"Third Largest = ",thirdLarge)
print("First Small = ",firstSmall,"Second Smallest = ",secondSmall,"Third Smallest = ",thirdSmall)
