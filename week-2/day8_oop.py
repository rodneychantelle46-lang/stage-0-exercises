class TodoItem:
    def __init__(self, title):
        self.title = title
        self.done = False

task = TodoItem("学习文件读写")
homework = TodoItem("学习异常处理")

print(task.title,  task.done)
print(homework.title, homework.done)

