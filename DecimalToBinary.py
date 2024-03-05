def DecimalToBinary(num):  
    while num >= 1:
        num=num/2
        print(num % 2, end = '')
DecimalToBinary(10)
