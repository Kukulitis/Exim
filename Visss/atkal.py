class MyPoint:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.limits=[self.y+100,self.x+100,self.y-100,self.x-100]
    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y
    def getxy(self):
        return[self.x,self.y]
    def mover(self,d):
        if self.x+d>self.limits[1]:
            print('pa lielu')
        else:
            self.x+=d

    def movel(self,d):
        if self.x-d>self.limits[3]:
            print('pa lielu')
        else:
            self.x-=d

    def moveup(self,d):
        if self.y+d>self.limits[0]:
            print('pa lielu')
        else:
            self.y+=d

    def movedown(self,d):
        if self.y-d>self.limits[2]:
            print('pa lielu')
        else:
            self.y-=d

    def distance(self,point):
        d1=point.getxy()[0]-self.getxy()[0]
        d2=point.getxy()[1]-self.getxy()[1]
        d=(d1**2+d2**2)**0.5
        return d
p1=MyPoint(2,6)
print(getxy)

class circle:
    def __init__(self,r,centre):
        self.r=r
        self.centre=centre
    def getarea(self):
        return 3.1415*self.r**2
    def getcf(self):
        return 3.1415*self.r*2
    def overlap(self,circle):
        if self.centre.distance(circle.centre)>self.r + circle.r:
            return False
        else:
            return True
p1=MyPoint(4,2)
p2=MyPoint(7,7)

circle1=circle(4,p1)
circle2=circle(5,p2)
print(circle1.overlap(circle2))

