#????
def mirror(letters):
    count=len(letters)
    count1=0
    list=[0]*count*2
    for i in range(0,len(letters)):
        list[i]=letters[i]
    for i in range(count, len(list)):
        list[i]=letters[count-1-count1]
        count=count-1
    print(list)
mirror(["a", "b", "c","d"])