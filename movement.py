import random

def main():
    arr1 = []
    maxIt = 10000
    t = 0
    for i in range(0, 10):
        arr1.append(random.uniform(-100, 100))
    while t < maxIt:
        n = movement(arr1)
        if func(n) < func(arr1):
            arr1 = n
        t += 1
        print(func(arr1))

def movement(arr):
    z=[]
    for i in arr:
        z.append(i)
    a = random.randint(0, 9)
    number = random.randint(-2, 2)
    if z[a] + number > 100:
        z[a] = 100
    elif z[a] + number < -100:
        z[a] = -100
    else:
        z[a] += number
    return z
main()