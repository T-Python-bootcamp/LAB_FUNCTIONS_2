def negativeDesc(first:int, second:int):
    if first < 0 and second < 0:
        if first < second:
            for num in range(first, second+1):
                print(num)
    else:
        print("The numbers should be negative")

negativeDesc(-15,-4)