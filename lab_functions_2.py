def func(num1: int, num2: int):
    if(num1 < 0 and num2 < 0):
        if(num1 < num2):
            for number in range(num1, num2+1):
                print(number)
        else:
            for number in range(num2, num1+1):
                print(number)
    else:
        print("The numbers should be negative")


func(-15, -4)
func(-4, -15)