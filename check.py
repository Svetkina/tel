a = open("data/text/covid19.txt", "r")
b = list()
for i in a:
    if len(i) > 0:
        b.append(i)
print(b)