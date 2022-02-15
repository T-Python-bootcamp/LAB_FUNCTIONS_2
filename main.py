def negNum(p1, p2):
    if  p1 >= 0 and p2 >= 0:
        print("The numbers should be negative")
        
    elif p1 > p2:
        print("the p1 should be smaller than p2")
        
    else:
        for i in range(p1, p2+1):
            print(i)
        
    
    
        
negNum(-15, -4)