def add_todo(text):
    with open("todo_list.txt", "a", encoding="utf-8")as f:
        f.write(text + "\n")

def show_todos():
    with open("todo_list.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print(content)

def delete_todo(index):
    with open("todo_list.txt", "r", encoding="utf-8") as f:
        todos = f.readlines()
    del todos[index]
    with open("todo_list.txt", "w", encoding="utf-8") as f:
        f.writelines(todos)

def clear_todos():
    with open("todo_list.txt", "w", encoding="utf-8") as f:
        f.write("")


clear_todos()
add_todo("学习文件读写")
add_todo("学习异常处理")
delete_todo(0)
show_todos()    