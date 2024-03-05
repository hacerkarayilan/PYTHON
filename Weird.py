import random
def main():
    n = random.randint(1, 100)
    
    if n % 2 == 1 and n <= 20:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
main()