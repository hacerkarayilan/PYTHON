def main2():
    file = open("python/hours.txt")
    lines = file.readlines()
    for line in lines:
        process_employee(line)
def process_employee(line):
    parts = line.split()
    id = parts[0] 
    name = parts[1] 
    sum = 0
    count = 0
    for i in range(2, len(parts)):
        sum += float(parts[i])
        count += 1
    average = sum / count
    print(name + " (ID#" + id + ") worked " +
    str(sum) + " hours (" + str(average) + " hours/day)")
main2()