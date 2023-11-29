class Rectangle:
    _nbrRec = 0
    def __init__(self,height = 33 , width = "22"):
        self._height = height
        self._width = width
        _nbrRec +=1 
    # def __init__(self, Rec):
    #     self._height = Rec.height
    #     self._width = Rec.width
    #     _nbrRec +=1 

    
    def getwidth(self):
        return self.width
    def setwidth(self,width):
        self._width = width
    
    def getheight(self):
        return self.height
    def setheight(self,height):
        self._height = height
    
    def getnbrRec():
        return Rectangle._nbrRec
    
    def premietre(self):
        return self._width * self._height
    
    def surface(self):
        return (self._height + self._width)*2

    def toString(self):
        return str(self._height) + " " + str(self._width) 

    def equals(self,Rec):
        return self._width == Rec._width and self._height == Rec._height
        

    
