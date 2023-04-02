l = 0
for i in open("wprawka5.txt"):
    para = [x.split("-") for x in i.rstrip().split(",")]
    if (int(para[0][0]) <= int(para[1][0]) and int(para[0][1]) >= int(para[1][1])) or (int(para[0][0]) >= int(para[1][0]) and int(para[0][1]) <= int(para[1][1])):
        l += 1
print(l)