with open ("fails.txt") as file:
    persons=file.readlines()

words=[]
for line in persons:
    words+=line.split()
    print(words)    
    for i in range(len(persons)):
        persons[i]=persons[i].replace("\n","")
        
    persons.sort()
    print(persons)