#4. Write a Python program to print and store ‘n terms of Fibonacci series in list
n=int(input("Enter n number for print fibonacci series :"))
a,b=0,1
fibo=[a,b]
i=2
if n<=0:
    print("The fibonacci series is =: ",n)
else:
    while i<=n:
          f=a+b
          fibo.append(f)
          a=b
          b=f
          i+=1
print(fibo)
