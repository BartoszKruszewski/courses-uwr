l = 0
for i in open("wprawka5.txt"):
    para = [x.split("-") for x in i.rstrip().split(",")]
    if set(range(int(para[0][0]),int(para[0][1])+1)) & set(range(int(para[1][0]),int(para[1][1])+1)):
        l += 1
print(l)