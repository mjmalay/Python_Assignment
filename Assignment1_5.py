#5. Write a python program compute following series and take a numbers num as input
#x-x3/3! + x5/5!-x7/7!+------+xn/n!
#where x=sum of all even digits except 2 and 8 and n= sum of all odd digits except 1 and 3
num=int(input("Enter a number : "))
fact=1
x,n,count=0,0,0
while num>0:
    rem=num%10
    if rem%2==0 and rem!=2 and rem!=8:
        x+=rem
    else :
         if rem%2!=0 and rem!=1 and rem!=3:
             n+=rem
    num=num//10
sum=x
i,j=n,1
while i>=3:
    while j<=i: 
        fact*=1
    count+=1
    if count%2==0:
        sum+=(x**i)//fact
    else:
        if count%2!=0:
            sum-=(x**i)//fact
print("Sum: ",sum)