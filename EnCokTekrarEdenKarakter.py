word="rlllllrrrrrıııııııırrllıı"
dic={}
for w in word:
    if w in dic.keys():
        dic[w]+=1
    else:
        dic[w]=1 
print(dic)
x=max(dic.keys())
print(x)