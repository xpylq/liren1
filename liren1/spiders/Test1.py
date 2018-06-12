file = open("/Users/youzhihao/Downloads/phone.txt", "r", encoding="utf-8")
list = []
for line in file.readlines():
    list.append(line.replace("\n", ""))

print(set(list).__len__())
