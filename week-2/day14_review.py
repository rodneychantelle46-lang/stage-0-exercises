from pathlib import Path
import json

class TodoItem:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return{
            "title": self.title,
            "done": self.done
        }
    
class TodoList:
    def __init__(self):
        self.items = []
    def add(self, item):
        item = TodoItem(item)
        self.items.append(item)
    def mark_done_by_index(self, index):
        if 0 <= index < len(self.items):
            self.items[index].mark_done()
        else:
            print("任务不存在")
    def show_all(self):
        for item in self.items:     
            if item.done:
                print(f"[x] {item.title}")
            else:
                print(f"[ ] {item.title}")
    def save(self, filename):
        path = Path(filename)
        data =[]
        for item in self.items:
            data.append(item.to_dict())
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

todo_list = TodoList()
todo_list.add("学习AI")
todo_list.add("学习Python") 
todo_list.add("学习Git")
todo_list.mark_done_by_index(1)
todo_list.show_all()
todo_list.save("todos.json")