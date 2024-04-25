import json
import argparse
from pprint import pprint
from Todo import Todo
from TodoDAO import TodoDAO
import configparser


def main():
    # Paramètres de la ligne de commande
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file',help="The config file")           
    args = parser.parse_args()
    
    # Lecture du fichier de configuration
    config = configparser.ConfigParser()
    config.read(args.config_file)
    
    db_file = config["DB"]["file"]
    #Data Access Object
    todoDAO = TodoDAO(db_file)
    all_todos = todoDAO.find_all()
    # l = list(all_todos)

    # t = next(all_todos)
    for todo in all_todos:
        print(todo)













    
    
def main01():
    with open("todos.json") as f:
        todos = json.load( f)
    # pprint(todos)    
    
    for t in todos:
        # todo = Todo(id=t['id'],title=t['title'],completed=t['completed'])
        del t['userId']
        todo = Todo(**t)
        print(todo)
    
    #Data Access Object
    todoDAO = TodoDAO("todos_db.db")
    
        
    # for t in todos:
    #     todo = Todo(**t)
    #     todoDAO.save(todo)
        
    


if __name__=='__main__':
    main()
