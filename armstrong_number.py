def armstrong_check(n):
    num_array = []
    arm_list = []
    while (n != (n%10)):
        mod_result = n % 10 
        num_array.append(mod_result)
        n = int(n /10)
    num_array.append(n)
    for i in range(len(num_array)):
        arm_list.append(pow(num_array[i],len(num_array)))
    return sum(arm_list)
number = int(input("Input : "))
if (armstrong_check(number) == number):
    print("Output : Yes")
else:
    print("Output : No")