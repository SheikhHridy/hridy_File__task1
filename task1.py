# A. Write to the file using 'w'
file = open("student_info.txt", "w")

file.write("C12\n")
file.write("C23\n")
file.write("C44\n")

file.close()


# B. Append more student IDs using 'a'
file = open("student_info.txt", "a")

file.write("C55\n")
file.write("C66\n")
file.write("C77\n")
file.write("C88\n")

file.close()


# C. Read and print using 'r'
file = open("student_info.txt", "r")

for line in file:
    print(line.strip())

file.close()