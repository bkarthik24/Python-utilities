def fact(x):
    factorial = 1 
    while(x != 1):
        factorial =factorial * x 
        x = x - 1 
    return factorial
number = int(input("Enter the number :"))
print(fact(number))