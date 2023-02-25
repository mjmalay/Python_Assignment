#2. Write a python program to find sum of product of corresponding digits of two any digit number 
#Such as n=1234 m=7896 output=6*4+9*3+8*2+7*1

n=1234
m=7896
sumOfProduct=0
while m>0 and n>0:
    rem1 = m % 10
    rem2 = n % 10
    sumOfProduct+=(rem1*rem2)
    m//=10
    n//=10
print("Sum of Product : ",sumOfProduct)
