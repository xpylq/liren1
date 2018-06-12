# /usr/bin/env python
# encoding=utf-8

def filterDuplicate(path):
    file = open(path, "r", encoding="utf-8")
    list = []
    for line in file.readlines():
        list.append(line.replace("\n", ""))
    file = open("/Users/youzhihao/PycharmProjects/liren1/liren1/doc/shop_url.txt", "w", encoding="utf-8")
    for line in set(list):
        file.write(line + "\n")


if __name__ == "__main__":
    filterDuplicate("/Users/youzhihao/PycharmProjects/liren1/liren1/doc/shop_url.txt")
