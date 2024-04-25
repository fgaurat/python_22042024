from Rectangle import Rectangle

class Carre(Rectangle):
    
    def __init__(self, cote):
        super().__init__(cote, cote)
        print(f"def __init__(self, {cote}):")
        self.__cote = cote
    
    @property
    def cote(self):
        return self.__cote

    @cote.setter
    def cote(self,cote):
        self.longueur = cote
        self.largeur = cote
        self.__cote = cote
        
    
    def __str__(self):
        return f"{__class__.__name__} {self.__cote=}"

        