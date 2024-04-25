def main_write():
    with open('mon_fichier.txt','a') as f:
        print('toto',file=f)


def main():
    # with open('mon_fichier.txt') as f:
    with open('mon_fichier.txt','r') as f:
        # for line in f.readlines():
        for line in f:
            print(line,end="")
            print(line.strip())
        
    
    
if __name__=='__main__':
    # main_write()
    main()
    
    s = " toto    "
    s2 = s.strip()
    print(s)
    print(s2)
