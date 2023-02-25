#4. Write a python program to compute following series and take input x and n
#I. 1-x2/2!+x3/3!-x4/4!+------+xn/n!
x=int(input("Enter the value of x :"))
n=int(input("Enter the value of n :"))
check=False
fact,sum=1,1
i,j=2,1
while i<=n:
    while j<=i:
        fact*=j
        j+=1
    if(check):
        sum+=(x**i)//fact
        check=False
    else:
        sum-=(x**i)//fact
        check=True
    fact=1
    i+=1
print("Sum : ",sum)
    
#II. x-x3/3! + x5/5!-x7/7!+------+xn/n!
x=int(input("Enter the value of x :"))
n=int(input("Enter the value of n :"))
check=False
fact,sum=1,x
i,j=3,1
while i<=n:
    while j<=i:
        fact*=j
        j+=1
    if(check):
        sum+=(x**i)//fact
        check=False
    else:
        sum-=(x**i)//fact
        check=True
    fact=1
    i+=2
print("Sum : ",sum)

#III. 1+x2/2! + x4/4!+x6/6!+------+xn/n!
x=int(input("Enter the value of x :"))
n=int(input("Enter the value of n :"))
fact,sum=1,1
i,j=2,1
while i<=n:
    while j<=i:
        fact*=i
        j+=1
    sum+=(x**i)//fact
    fact=1
    i+=2
print("Sum : ",sum)

#IV. x-x3/3! + x5/5!-x7/7!+x11/11!------+xn/n!
x=int(input("Enter the value of x :"))
n=int(input("Enter the value of n :"))
check=False
count=0
fact,sum=1,x
i,j=3,1
k=1
while i<=n:
    while j<=i:
        if i%j==0:
           count+=1
    if count==2:
        while k<=i: 
            fact*=k
            k+=1
        if(check):
            sum+=(x**i)//fact
            fact=1
            check=False
        else:
            sum-=(x**i)//fact
            fact=1
            check=True
    i-=1
print("Sum : ",sum)