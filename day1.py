#we want to count of digits in a given string 
num = input("Enter a string: ")
n = int(num)
count = 0 
while n > 0:
    count += 1
    n = n // 10
print(count)



#check if number is palindrome or not
num = int(input("Enter a number: "))
num = int(num)
result = 0
while num > 0:
    ld = num %10
    result = result *10 +ld
    num = num //10
print(num == result)
