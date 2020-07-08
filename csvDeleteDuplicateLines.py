filename1 = input("Enter name/path of file to be read: ")
filename2 = input("Enter name/path of output file: ")

file1 = open("%s" % filename1, "r")
file2 = open("%s" % filename2, "w")

newrows = []
for row in file1.readlines():
    if row not in newrows:
        newrows.append(row)

file2.writelines(newrows)
