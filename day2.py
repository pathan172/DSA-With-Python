#print factors
#brute force method
num =20
result = []
for i in range(1,num+1):
    if num % i ==0:
        result.append(i)
print(result)


#better approach
num = 20
result = []
for i in range(1, num//2 + 1):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)        


#optimal approach
from math import sqrt
num = 20
result = []
for i in range(1, int(sqrt(num)) + 1):
    if num % i == 0:
        result.append(i)
        if i != num // i:
            result.append(num // i)
print(sorted(result))


#hashing in python
n=[5,4,33,2,1,5,4,3,2,1]
m=[4,5,6,7,8,9,10]
for num in m:
    count = 0
    for i in n:
        if i == num:
            count += 1
            print(count)