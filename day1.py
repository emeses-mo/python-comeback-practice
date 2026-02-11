#Day 1 python basics

name = input("Enter Name: ")
birthyear = int(input("Enter your birth year: "))

curYr = 2026
age =  curYr - birthyear

print(f"Hello {name} - you are {age} yrs old.")

yrsto30 = 30-age

print(f" you will be 30 in {yrsto30} years")

if age<18:
    print("Minor")
else:
    print("Adult")
