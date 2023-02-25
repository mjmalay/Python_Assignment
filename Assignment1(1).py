#1. Write a python program to create a list of prime numbers as per given range
num=int(input("Enter the second range :"))
PrimeNumbers=[]
for x in range(2,num):
    isPrime=True
    for n in range(2,x):
        if x%n==0:
            isPrime=False
    if isPrime:
        PrimeNumbers.append(x)
print("List of prime number : ",PrimeNumbers)
