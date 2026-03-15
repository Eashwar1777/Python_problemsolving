print("Assignment 4")

print("Q1-For loops")
n = int(input("Enter a number: "))
for i in range(n):
    print("Hello")

print("Q2-For loops")
for i in range(1, n + 1):
    print(i)

print("Q3-For loops")
for i in range(n, 0, -1):
    print(i)

print("Q4-For loops")
for i in range(1, 11):
    print(n * i)

print("Q5-For loops")
n1 = int(input("Enter the number upto u want the sum: "))
n2 = 0
for i in range(n1 + 1):
    n2 = n2 + i

print(f"The sum of all the numbers is {n2}")

print("Q6-For loops")
fac = int(input("Enter a number obtain its factorial: "))
fac1 = 1
for i in range(1, fac + 1):
    fac1 = fac1 * i
print(f"The factorial of {fac}  is {fac1}")

num_sum = int(input("Enter the target number: "))
sum_even = 0
sum_odd = 0
for i in range(1, num_sum):
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i

print(f"The even and odd is {sum_even},{sum_odd}")

fact_num = int(input("Enter the number you want to find its factors: "))
print("The factors of the", fact_num, "are as follows: ")
for i in range(1, fact_num + 1):
    if fact_num % i == 0:
        print(i)

num = int(input("Enter a number to check whether it is a perfect number : "))
sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div = sum_div + i
if sum_div == num:
    print(f"The number {num} is a Perfect number")
else:
    print(f"The number {num} is not a perfect number")

org = input("Enter a string to reverse it : ")
rev = ""
for i in range(len(org) - 1, -1, -1):
    print(org[i])

org = input("Enter a string to check if it is a pallindrome: ")
rev = ""
for i in range(len(org) - 1, -1, -1):
    print(org[i])
    rev = rev + org[i]
if rev == org:
    print("The string is pallindrome")
else:
    print("The string is not pallindrome")

prime_num = int(input("Enter the number to check whether it is prime or not: "))
count = 0
for i in range(1, prime_num + 1):
    if prime_num % i == 0:
        count = count + 1

if count == 2:
    print(f"The number {prime_num} is a prime number")
else:
    print("The number is not a prime number")

str2 = input("Enter a string to find number of character,digits and secial characters: ")
char = 0
splchar = 0
dig = 0

for i in str2:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        splchar += 1

print(f"The number of digits are {dig} ")
print(f"The number of alphabets are {char}")
print(f"The number of special characters are {splchar}")
    
num = int(input("enter a number to get on new line: "))
while num > 0:
    print(num % 10)
    num //= 10
    

