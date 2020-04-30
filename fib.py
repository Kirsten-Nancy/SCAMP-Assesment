from functools import lru_cache


@lru_cache(maxsize=500)
def Fibonacci(number):
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    elif(number == 2):
        return 1
    elif(number > 2):
        return(Fibonacci(number-1) + Fibonacci(number-2))


number = int(input("Enter a number: "))
if(number < 0):
    raise ValueError("Please enter a positive integer")

print("The Fibonacci sequence is: ")

for i in range(number):
    print(Fibonacci(i))
