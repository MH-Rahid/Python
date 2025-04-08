# score = 85
# if score >= 90:
#     print("a")
# elif score >= 85:
#     print("b")
# elif score >=70:
#     print("c")
# else:
#     print("d")

# def checkPrime(num):
#         for num in range(1,1000):
#                 for i in range(2,num):
#                         if(num % 2 != 2 and num % i != 0):
#                                 return 1                            
#                         else:
#                                 return -1

# prime = checkPrime(8)

# if(prime == 1):
#         print("prime")
# else: 
#         print("not prime")
        

def checkPrime(num):
    if(num >= 1 and num <= 1000):
        for i in range(2, num):
            if(num % 2 != 0 and num % i/2 == 0):
                return 1
            else: 
                return -1

prime = checkPrime(9)
print(prime)