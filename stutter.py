#?????
def stutter(nums):
    count=0
    list=[0]*len(nums)*2
    for i in range(0,len(nums)):
        for j in range(count,count+2):
            list[j]=nums[i]
        count+=2
    print(list)
stutter([1, 2, 3,4,5])