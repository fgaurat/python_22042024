from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from RectangleData import RectangleData

def main():
    ce = Cercle(2)
    print(ce.get_surface())
    
def main02():
    c= Carre(2)
    print(c)
    print(c.cote)
    print(c.get_surface())
    c.cote = 458
    print(c.get_surface())
    
    
    
    
    
    
    
    
    
    
    
    
    
    



def main01():
    r = Rectangle(5,6) # __init__
    # longueur = r.get_longueur() # 5
    
    print(r.longueur)
    r.longueur = -25
    # longueur = r.get_longueur() # 15
    # print(longueur)
    print(r.longueur)
    surface = r.get_surface()
    print(surface)
    
    
    s = str(r)
    print(s)
    print(50*'-')
    r1 = Rectangle(5,6)
    r2 = Rectangle(5,6)
    if(r1==r2):
        print("ok")
    else:
        print("ko")
    print(50*'-')
    r3 = RectangleData(5,9)
    r4 = RectangleData(5,9)
    
    if r3 ==r4:
        print("ok RectangleData")
        
    print(r3)
    print("cpt",Rectangle.get_cpt())
    
    

if __name__=='__main__':
    main()
