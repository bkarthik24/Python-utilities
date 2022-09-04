def simple_interest(p,r,t):
    return (p * r * t)/100 
amount = int(input("Enter the Principle amount : "))
rate = int(input("Enter the rate : "))
time = int(input("Enter the time :"))
print(simple_interest(amount,rate,time))