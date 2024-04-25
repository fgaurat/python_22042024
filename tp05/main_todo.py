def main():

    todos = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        },
        {
            "userId": 1,
            "id": 4,
            "title": "et porro tempora",
            "completed": True
        },
        {
            "userId": 1,
            "id": 5,
            "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
            "completed": False
        }
    ]

    
    for todo in todos:
        #completed = cond?"ok":"ko"
        completed = "ok" if todo['completed'] else "ko"
        
        # print(f"id:{todo['id']}, {todo['title']} => {completed}" )
        print("id:{id}, {title} => {isCompleted}".format(**todo,isCompleted = completed) )

if __name__ == '__main__':
    main()
