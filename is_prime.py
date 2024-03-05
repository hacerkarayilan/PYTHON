def is_prime(n):
    factors = 0;
    for i in range(1, n + 1):
        if (n % i == 0):
            factors += 1
    if factors == 2:
        return True
    else:
        return False
        
if not is_prime(6):
    print("not")