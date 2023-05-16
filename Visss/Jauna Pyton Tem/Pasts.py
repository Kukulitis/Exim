f = open ("pasts.txt")

# print(f.read(1))
# print(len(f.read()))

gar =len(f.read())
f.seek(0)
vards=""
vieata=[]
for i in range(gar):
    c=f.read(1)
    if c== " ":
        print (vards)
        if len(vieata) ==0:
            vieata.append(vards)
        else:
            i=0
            while vards[0]> vieata[i][0]:
                i += 1
                vieata.insert(i,vards)
        vards=""
    else:
        vards += c