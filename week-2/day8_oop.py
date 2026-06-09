class TodoItem:
    def __init__(self, title):
        self.title = title
        self.done = False
    def mark_done(self):
        self.done = True
    def show(self):
        print(self.title, self.done)

class TodoList:
    def __init__(self):
        self.items = []

    def add(self, item):
        item = TodoItem(item)
        self.items.append(item)

    def show_all(self):
        for item in self.items:
            item.show()

    def mark_done_by_index(self, index):
        if 0 <= index < len(self.items):
            self.items[index].mark_done()
        else:
            print("任务不存在")

    def delete_by_index(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
        else:
            print("任务不存在")


todo = TodoList()
todo.add("学习AI")
todo.add("学习Python")
todo.show_all()
todo.mark_done_by_index(1)
todo.delete_by_index(0)
todo.show_all()
