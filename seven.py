def seven():
    for i in range(1, 11):
        num = randint(1, 30)
        print(str(num) + " ", end='')
        if num == 7: 
            return True
    return False
seven()