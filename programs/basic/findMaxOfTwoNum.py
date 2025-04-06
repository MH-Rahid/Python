def findMax(a, b):
    max = a if a > b else b
    return max 

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

res = findMax(a, b)

print("Maximum Number: ", res)
