# Klase MyPoint, kas implementē sekojošo:
class MyPoint:
# konstruktors, kur tiek padots punkta x un y
    def __init__(self,x,y):
        self.x=x
        self.y=y
# Funkcijas setX, setY, getXY, moveRight(d), moveLeft(d),
    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y
    def getxy(self):
        return[self.x,self.y]
    def moveRight(self,d):
        self.x+=d
    def moveLeft(self,d):
        self.x-=d
# moveUp(d), moveDown(d), distanceTo(point)
    def moveUp(self,d):
        self.y+=d
    def moveDown(self,d):
        self.y-=d
    def distanceTo(self,point):
        x1=self.getxy()[0]
        x2=point.getxy()[0]
        y1=self.getxy()[1]
        y2=point.getxy()[1]

        x=x2-x1
        y=y2-y1
        (x**2+y**2)**0.5
# Nodrošināt funkcionalitāti tā, lai punktu nebūtu iespējams
# pārvietot tālāk par 100 vienībām uz jebkuru pusi no
# _sākotnējās_ pozīcijas
# izveidot MyPoint objektu, nodemonstrēt vismaz četru
# iekšējo funkciju darbību

# Klase Circle, kas par centra punktu izmanto MyPoint klases objektu
# implementē visas funkcijas, kas raksturīgas riņķa līnijai
# konstruktorā MyPoint objekts un rādiuss
p=MyPoint(9,9)

p.moveLeft(3)
p1=MyPoint(69,57)
print(p.distanceTo(p1))
print(p.getxy())
