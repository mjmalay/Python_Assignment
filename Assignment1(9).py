#9. Write a python program to find repeated numbers as well as frequency of 
#repetition of numbers in a list of 20 user defined values?

l=[1,2,3,1,2,4,3,6,4,2,3,2,6,4,7,2,4,2,5,3]
u=list(set(l))
f=[]
for i in u:
    a =l.count(i)
    f.append(a)
print("Given list",l)
print("Unique items :",u)
print("frequency of repetition of numbers:",f)
r=[]
for i in list(range(len(f))):
    if f[i]>1:
        a=f.index(f[i],i)
        n=u[a]
        r.append(n)
print("Repeated :",r)

# num_list = [int(i) for i in input().split()]

# unique_nums:dict = {}

# for i in num_list:
#     if i in unique_nums:
#         unique_nums[i] += 1
#     else:
#         unique_nums[i] = 1

# print((unique_nums.keys()))
# print(unique_nums)
