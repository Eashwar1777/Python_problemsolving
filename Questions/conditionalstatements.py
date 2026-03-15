print("Assignment 3")
as31 = int(input("Enter the first number: "))
as32 = int(input("Enter the second number: "))
if as31 > as32:
    print(f"{as31} is larger than {as32}")
elif as32 > as31:
    print(f"{as32} is larger than {as31}")
else:
    print("Both the numbers are same")

as34 = input("Enter your gender(M or F): ")
if as34 == "M" or as34 == "m":
    print("Good afternoon sir")
elif as34 == "F" or as34 == "f":
    print("Good afternoon mam")
else:
    print("Unidentified Gender")

as35 = int(input("Enter the number: "))
if as35 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

as36_name = input("Enter your name: ")
as37_age = int(input("Enter your age: "))
if as37_age > 18:
    print(f"Hey {as36_name} you are eligible to vote")
else:
    print(f"Hey {as36_name} you are not eligible to vote")

year = int(input("Enter the year: "))
if year % 4 == 0 and year % 100 != 0:
    print(f"This year {year} is a leap year")
elif year % 400 == 0:
    print(f"This year {year} is a leap year")
else:
    print(f"this year {year} is not a leap year")

temp = int(input("Enter the temperature(in Celsius) : "))
if temp < 0:
    print("Freezing Cold")
elif temp > 0 and temp <= 10:
    print("Very cold")
elif temp > 10 and temp <= 20:
    print("Cold")
elif temp > 20 and temp <= 30:
    print("Pleasant")
elif temp > 30 and temp <= 40:
    print("Hot")
else:
    print("Very Hot")