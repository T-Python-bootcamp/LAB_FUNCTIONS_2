def myFun (firstPar:int,secondPar:int):
    if firstPar < 0 and secondPar < 0:
        if firstPar < secondPar:
            for num in range ( firstPar, secondPar + 1 ):
                print ( num )
        else:
            print("First number must be smaller than second number")
    else:
        print ( "The numbers should be negative")
        
myFun(-15, -4)