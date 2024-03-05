from random import*
def abc():
    count = 0
    x = []
    for i in range(0,5):
        x.append(randint(1,5))    
    for i in range(0,5):
        print(x[i])
    print("*************")
    for i in range(0,5):
        count += x[i]*x[i]
        print(x[i]*x[i])
    print("*************")
    print (count)
abc()