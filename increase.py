def main():
    iq = [126, 167, 95]
    print(iq)
    increase(iq)
    print(iq)
def increase(a):
    for i in range(0, len(a)):
        a[i] = a[i] * 2
main()