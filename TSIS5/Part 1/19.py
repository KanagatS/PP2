import glob
newlist = []
files_list = glob.glob("*.txt")
for file_elem in files_list:
    with open(file_elem, "r") as f:
        newlist.append(f.read())

print(newlist)
