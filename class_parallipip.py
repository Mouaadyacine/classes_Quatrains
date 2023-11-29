from class_rectangle import Rectangle

class ParallPip(Rectangle):
    _nbrParral = 0
    # def __init__(self, parall):
    #     super().__init__(parall)
    #     self._Haut = parall._Haut
    #     _nbrParral+=1
    def __init__(self, width = 2 , height = 22,haut = 44):
        super().__init__(height,width)
        self._Haut = haut
        _nbrParral+=1
    
    def getNbrParral():
        return ParallPip._nbrParral
    
    def surface(self):
        return super().surface() * self._Haut
    
    def volume(self):
        return super().surface() * self._Haut
    
    def toString(self):
        return super().toString() + " " + str(self._Haut)