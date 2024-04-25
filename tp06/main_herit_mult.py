class A:
    
    def __init__(self):
        super().__init__()
        print("A")
    def show(self):
        print("show a")


class B(A):
    
    def __init__(self):
        super().__init__()
        print("B")
    def show(self):
        print("show b")

class C(A):
    
    def __init__(self):
        super().__init__()
        print("C")
    def show(self):
        print("show c")

class D(B,C):
    
    def __init__(self):
        super().__init__()
        print("D")
    
    def show(self):
        super(B,self).show()
        print("show d")


def main():
    print(D.mro())
    d = D()
    d.show()

if __name__=='__main__':
    main()
