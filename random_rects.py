def random_rects():
    total=0
    x=int(input("How many rectangles? "))
    for i in range(1,x+1):
        print("width",str(i)+"?",end=" ")
        w=int(input())
        print("Height",str(i)+"?",end=" ")
        h=int(input())
        total+=w*h
        for i in range(0, h):
            for i in range(0,w):
                print("*" ,end="")
            print()
    print("Total area:", total)
random_rects()