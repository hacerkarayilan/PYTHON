from random import randint
out = open("output.txt", "a")
for i in range(5):
    out.write(str(randint(1,100))+"\n")
out.close()
print(open("output.txt").read())