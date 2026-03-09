file = open("students.csv", "r")

lines = file.readlines()

for line in lines[1:]:
    data = line.strip().split(",")

    name = data[0]
    section = data[1]
    age = data[2]

    print(name + " is in section " + section + ", her age is " + age)

file.close()