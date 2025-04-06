# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
    

# print(fact(5))

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     return fact

# print(factorial(5))

# def checkEvenOdd(num):
#     if(num%2 == 0):
#         return "even"
#     else:
#         return "odd"

# num = int(input("Enter a number: "))

# print(checkEvenOdd(num))

def sumOfNum(num):
    if(num == 1):
        return 1
    else:
        return num + sumOfNum(num-1)
print(sumOfNum(10))