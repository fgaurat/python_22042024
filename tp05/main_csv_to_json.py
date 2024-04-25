from pprint import pprint
import json

def main():
    with open("MOCK_DATA.csv","r") as f:
        
        rows = [l.strip() for l in f.readlines()]
        keys = rows[0].split(",")
        values = rows[1:]
        
        all_data=[]
        for value in values:
            value = value.split(",")
            data = dict(zip(keys,value))
            all_data.append(data)
        # pprint(all_data)
            
    with open("todos.json","w") as f:
        json.dump(all_data, f,indent=4)
        
if __name__=='__main__':
    main()
