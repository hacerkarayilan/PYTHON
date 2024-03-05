def main():
    a1=[1,5,9]
    a2=[2,4,6]
    birles=[0]*(len(a1)+len(a2))
    for i in range(0, len(a1)):
        birles[i]=a1[i]
    for i in range(0,len(a2)):
        birles[i+len(a1)]=a2[i]
    print(birles)
main()