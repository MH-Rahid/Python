filePath = r"C:\Users\Rahid\Desktop\CODING\Python\programs\basic\sample.txt"

# with open(filePath, "w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using Java.\nI like programming in Java")

# with open(filePath, "r") as f:
#     data = f.read()

# newData = data.replace("Java", "Python")
# print(newData) 

# with open(filePath, "w") as f:
#     f.write(newData)


with open(filePath, "r") as f:
    data = f.read()

if(data.find("learning") != -1):
    print("found")
else:
    print("not found")