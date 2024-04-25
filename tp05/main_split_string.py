def main():
    line = "value01;value02;value03;value04"
    data = line.split(';')
    print(data)
    
    l1 = ['name','firstName','age']
    l2 = ['GAURAT',"Frédéric",47]
    # d={}
    # for p,k in enumerate(l1):
    #    d[k] = l2[p] 
    # print(d)
    
    z = dict(zip(l1,l2))
    print(z)
if __name__=='__main__':
    main()
