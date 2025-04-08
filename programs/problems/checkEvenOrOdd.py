# Write a program to check if a number is even or odd.

def checkEvenOrOdd(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

num = int(input("Enter a number: "))

checkEvenOrOdd(num)