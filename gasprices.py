def main1():
    file = open("python/gasprices.txt")
    belgium = 0
    usa = 0
    count = 0
    lines = file.read().split()
    for i in range(0, len(lines), 3):
        belgium += float(lines[i])
        usa += float(lines[i + 1])
        count=count+1
    print("Belgium average:", (belgium / count), "$/gal")
    print("USA average:", (usa / count), "$/gal")
main1()
#8.20 b 
#3.81 u count 1
#3/21/11
#8.08 b
#3.84 u count 2
#3/28/11 
#Belgium average: 8.3
#USA average: 3.9
