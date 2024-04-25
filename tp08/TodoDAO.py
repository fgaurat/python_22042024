import sqlite3
from pprint import pprint
from Todo import Todo

class TodoDAO:
    
    
    def __init__(self,db_file:str):
        self.__con = sqlite3.connect(db_file)
        
    def __del__(self):
        self.__con.close()
        
    def find_all(self):
        cur = self.__con.cursor()
        res = cur.execute("SELECT id,title,completed FROM todos_tbl")
        all_data = res.fetchall()
        
        for id,title,completed in all_data:
            t = Todo(id,title,completed)
            yield t
        
        
        
    
    def find_all_old(self):
        cur = self.__con.cursor()
        res = cur.execute("SELECT id,title,completed FROM todos_tbl")
        all_data = res.fetchall()
        todos = []        
        # for d in all_data:
        #     t = Todo(*d)

        # for d in all_data:
        #     id,title,completed = d
        #     t = Todo(id,title,completed)
        
        for id,title,completed in all_data:
            t = Todo(id,title,completed)
            todos.append(t)
        
        # return [Todo(*d) for d in all_data]
        return todos
    
    
    
    def save(self,todo):
        cur = self.__con.cursor()
        sql="""INSERT INTO todos_tbl(title,completed) 
        VALUES (?,?)
"""
        cur.execute(sql,[todo.title,todo.completed])        
        self.__con.commit()
        

