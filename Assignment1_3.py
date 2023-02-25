#3. Write a python program to find sum of product of corresponding even digits of first any digit number 
#and corresponding odd digit of any digit number
#Such as n=1234 m=4567 output=4*7+2*5
m=4567
n=1234
sumOfProduct=0
while (m > 0 and n > 0):
    rem1 = n % 10
    rem2 = m % 10
    if ((rem1%2== 0) and (rem2 % 2!=0)): 
        sumOfProduct += (rem1*rem2)
    m//= 10
    n//= 10
print("Sum of product of corresponding even and odd digits number : ",sumOfProduct)

