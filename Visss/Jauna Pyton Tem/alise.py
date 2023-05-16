f = open ("alise.txt")
gar =len(f.read())
f.seek(0)
parent= f.read(1)
mezgls=""
mezgli=[]
for i in range(gar):
    mezgls += f.read(1)
    if mezgls == " ":
        mezgls=""
    elif mezgls == "/n":
        print(mezgli)
        parent=f.read(1)
        mezgli=[]
    else:
        mezgli.insert(0,mezgls)