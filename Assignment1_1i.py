#1. Write a python program to find following using looping and decision making without function
#I. Sum of all digits of any numbers

num=1234
sum=0
while num>0:
     i=num%10
     sum=sum+i
     num=num//10
print("Sum of all digits of any number is = %d"%(sum))

#II. Sum of all even digits of any number
num=4321
sum=0
while num>0:
    i=num%10
    if i%2==0:
         sum=sum+i
    num=num//10
print("Sum of all even digits number :",sum)

#III. Sum of all odd digits of any number
num=1234
sum=0
while num>0:
    i=num%10
    if i%2!=0:
         sum=sum+i
    num=num//10
print("Sum of all odd digits number :",sum)

#IV. Sum of all prime digits
num=int(input("Enter any digits number : "))
sum=0
while num>0:
     r=num%10
     if (r==2 or r==3 or  r==5 or r==7):
         sum+=r
     num//=10
print("Sum of all prime digits : ",sum)

#V. Difference between average of all even digits except divisible by 4 and avearge of all odd digits except divisble by 3
num=56789
sumOfeven=0
sumOfOdd=0
eCount=0
oCount=0
eAvg=0
oAvg=0
while num>0:
     i=num%10
     if i%2==0: 
        if i%4!=0:
          eCount+=1
          sumOfeven+=i
     else :
          if i%3!=0:
             oCount+=1
             sumOfOdd+=i
     num=num//10

eAvg=sumOfeven//eCount
oAvg=sumOfOdd//oCount
print("Average of all even number : ",eAvg)
print("Average of all odd digits number :",oAvg)

#VI. Find kth digit from frontside or back side of any digits number and find its poistional value
digit=int(input("Enter any digits : "))


#VII. Sum of product of consecutive digits of any digit number
num=1234
sum=0
while num>0:
      i=num%10
      j=(num//10)%10
      sum+=(i*j)
      num=num//10
print("Sum of product of consecutive digits of any digit number: ",sum)
#VIII. Sum of product of consecutive even digits of any digit number
num=2467
sum=0
while num>0:
      i=num%10
      j=(num//10)%10
      if i%2==0:
         if j%2==0:
             sum+=(i*j)
      num=num//10
print("Sum of product of consecutive even digits of any digit number : ",sum)
#IX. Sum of product of consecutive odd digits of any digit number
num=2357
sum=0
while num>0:
      i=num%10
      j=(num//10)%10
      if i%2!=0:
         if j%2!=0:
             sum+=(i*j)
      num=num//10
print("Sum of product of consecutive odd digits of any digit number : ",sum)
#X. Sum of product of consecutive prime digits of any digit number
num=int(input("Enter any digis number : "))
sum=0
while num>0:
     r1=num%10
     r2=(num//10)%10
     if (r1==2 or r1==3 or  r1==5 or r1==7) and (r2==2 or r2==3 or r2==5 or r2==7):
         sum+=r1*r2
     num=num//10
print("Sum of product of digits : ",sum) 
#XI. Difference between Sum of product of consecutive even digits except 2 and 6 and Sum of product of consecutive odd digits except 3 and 7 of any digit number
num=4891
SumOfEven=0
SumOfOdd=0
while num>0:
      rem1=num%10
      rem2=(num//10)%10
      if rem1%2==0 and rem2%2==0:
         if(rem1!=2 and rem1!=6 ) and (rem2!=2 and rem2!=6):
               SumOfEven+=(rem1*rem2)
      else:
         if(rem1%2!=0 and rem2%2!=0):
            if(rem1!=3 and rem1!=7) and (rem2!=3 and rem2!=7):
                      SumOfOdd+=(rem1*rem2)
      num=num//10
difference=SumOfEven-SumOfOdd
print("Difference between Sum of product of consecutive even digits except 2 and 6 and Sum of product of consecutive odd digits except 3 and 7 of any digit number: ",difference)