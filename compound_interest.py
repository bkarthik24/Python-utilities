def compound_interest(p,r,t):
    amount = p * (pow((1+r/100),t))
    return float(amount-p) 
principle = float(input("Enter the principle amount :"))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time : "))
print(compound_interest(principle,rate,time))