

def nagative_func(num_1: int, num_2: int):
    if(num_1 < 0 and num_2 < 0):
        if(num_1 < num_2):
            negative_numbers = range(num_1, num_2+1)
            for num in negative_numbers:
                print(num)
    else:
        print("The numbers should be negative")


nagative_func(-15, -4)
