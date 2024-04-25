import traceback



def div(a,b):
    return a/b

def call_div(a,b):
    try:
        print("open file")
        r = div(a, b)
    finally:
        print("close file")
    return r

def main():
    try:
        a = 2
        b = 0
        r = call_div(a, b)
        print(r)
    except Exception as e:
        print(e)
    
    
    
    
def main01():
    try:
        a=2
        b=int(input("b :"))
        c = a/b

    except ZeroDivisionError as e:
        print("ZeroDivisionError Erreur")
        print(e)
        traceback.print_exc()
    # except TypeError as e:
    #     print("TypeError Erreur")
    #     print(e)
    # except ValueError as e:
    #     print("ValueError Erreur")
    #     print(e)
    except Exception as e:
        print("Exception Erreur")
        print(e)
        traceback.print_exc()
    else:
        print("Pas d'erreur")
    finally:    
        print("la suite")

if __name__=='__main__':
    main()
