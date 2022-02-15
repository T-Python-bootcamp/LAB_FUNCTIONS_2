
def checkerOfTwo (number1,number2):
    if number1>=0 or number2>=0:
        print('The numbers should be negative')
        return
    if(number1>number2):
        print('number1 is bigger than number2')
    for i in range(min(number1,number2),max(number1,number2)+1):
        print(i)
    

checkerOfTwo(-4,-15)