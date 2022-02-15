def func(num1:int,num2:int):
    if not(num1<0 and num2<0):
        print("The numbers should be negative")
    elif not(num1<num2):
        print(" first number should be smaller than the second number ")
    else:
        for x in range(num1,num2+1):
            print(x)

func(3,-4)
func(-3,-4)
func(-15,-4)
