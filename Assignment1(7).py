#7. Write a python program to find difference between average of all even
#numbers except divisible by 4 and average of all odd numbers except
#divisible by 5 in a list of user defined 20 values?
even,odd=0,0
num=[23,34,56,45,12,56,98,43,46,17,52,3,2,12,43,55,86,90,4,21]
e,o=0,0
for i in range(0,len(num)):
    if i%2==0 and i%4!=0:
         e+=1
         even+=i
    else:
        if i%2!=0 and i%5!=0:
            o=o+1
            odd+=i
    i+=1
EvenAvg=even//e
OddAvg=odd//o
diff=EvenAvg-OddAvg
print("Difference : ",diff)
