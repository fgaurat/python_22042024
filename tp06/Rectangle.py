
class Rectangle:
    __cpt=0
    
    def __init__(self,longueur,largeur):
        print(f"def __init__(self,{longueur},{largeur})")
        self.__longueur = longueur
        self.__largeur = largeur
        Rectangle.__cpt+=1
    
    @staticmethod
    def get_cpt():
        return Rectangle.__cpt
    
    @property    
    def longueur(self):
        return self.__longueur
    
    @property    
    def largeur(self):
        return self.__largeur
    
    @longueur.setter
    def longueur(self,longueur):
        self.__longueur = longueur

    @largeur.setter
    def largeur(self,largeur):
        self.__largeur = largeur
        
    def get_surface(self):
        return self.__largeur*self.__longueur


    def __str__(self):
        return f"{__class__.__name__} {self.__longueur=},{self.__largeur=}"
    
    # if(r1==r2):
    # if(r1.__eq__(r2)):
    def __eq__(self, o):
        r = False
        if isinstance(o, Rectangle):
            r= self.__longueur == o.__longueur and self.__largeur == o.__largeur
        return r
        # return True if isinstance(o, Rectangle) and self.__longueur == o.__longueur and self.__largeur == o.__largeur else False
    
