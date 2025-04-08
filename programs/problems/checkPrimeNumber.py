# def checkPrime(number):
#     # if number == 2:
#     #     return True
#     if number <= 1:
#         return False
#     else:
#         for i in range(2,int(number/2+1)):
#             if number % i == 0 :
#                 return False
                
            
#     return True

# num = int(input("Enter a number: "))

# if checkPrime(num):
#     print("Prime")
# else: 
#     print("Not Prime")

def checkPrime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2,int(number**0.5 + 1)):
            if number % i == 0:
                return False
    return True

count = 0
for i in range(1,101):
    if checkPrime(i):
        print("prime:", i)
        count += 1
    else:
        print("notPrime", i)

print("prime number between 1 to 101: ", count)