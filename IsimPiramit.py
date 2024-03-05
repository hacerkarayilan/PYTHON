def main():
    name=input("isim ")
    for i in range(0,len(name)):
        print(" "*i,name[i:len(name)+1])
    for i in range(1,len(name)+1):
        print(" "*(len(name)-i),name[0:i])
main()