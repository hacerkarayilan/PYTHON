def slope(x1,x2,y1,y2):
    dy=y2-y1
    dx=x2-x1
    result=dy/dx
    return result
def main():
    s=slope(5,6,7,8)
    print("sonuc", s)
main()