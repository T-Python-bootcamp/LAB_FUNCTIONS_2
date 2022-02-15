## Create a function that takes two parameters of type int . The function should do the following:
# - Check if all the variables are negative . Else print "The numbers should be negative"
# - Check that the first parameter is smaller than the second parameter .
# - Using a loop Print all the numbers bettween the smaller int up to the bigger int . 

def fun(firstNum:int, secondNum:int):
    if firstNum<0 and secondNum<0:
        if firstNum<secondNum:
            for num in range(firstNum,secondNum+1):
                print(num)
        else:
            print("Enter correct numbers")
    else:
        print("The numbers should be negative")

fun(-15,-4)