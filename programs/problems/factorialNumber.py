def factorial(num):
    fact = 1
    if num < 0:
        return "Not defined"
    for i in range(1, num+1):
        fact *= i
    return fact 


num = int(input("Enter a number : "))
print(f"Factorial of {num} is :",factorial(num))