def main():
    a = 2
    b = 3
    c = a/b
    
    s = "valeur de a : "+str(a)
    print("valeur de a :",a)
    
    s = f"valeur de a : {a}, b = {b}"
    s = f"{a=} / {b=} = {c=:.2}"
    print(s)
    s = f"{a=} / {b=} = {c=:.2%}"
    print(s)
    
    print(f"{a:>10}")
    print(f"{a:<10}-")
    
    l = [a,b,c]
    s=f"{l[0]}"
    print(s)
    s = "les valeurs : {},{},{}".format(l[0],l[1],l[2])
    s = "les valeurs : {},{},{}".format(22,878,"toto")
    s = "les valeurs : {1},{0},{2}".format(*l)
    print(s)
    
    # s = ""
    # for i in l:
    #     s+="{} "
    # print(s.format(*l))
    
    d = {
        "name":"GAURAT",
        "firstName":"Fred",
        "age":47,
    }
    s = "nom:{name} , prénom:{firstName} ".format(name="GAURAT",firstName="fred")
    print(s)
    
    s = "nom:{name} , prénom:{firstName} ".format(**d)
    print(s)
if __name__=='__main__':
    main()
