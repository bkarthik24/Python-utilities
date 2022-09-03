def max(x,y):
    if x > y:
        print(str(x)+" is greater")
    elif y >x:
        print(str(y)+" is greater")
    else:
        print("both the numbers are eqaul")
first_number = input("Enter first number : ")
second_number = input("Enter second number : ")
int_first_number = int(first_number)
int_second_number = int(second_number)
max(int_first_number,int_second_number)