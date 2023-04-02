data = [x.split("/")[0].rstrip() for x in open("popularne_slowa.txt","r")]
f = open("slowa.txt","w")
for i in data:
    f.write(i + "\n")