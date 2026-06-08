class TodoItem:
    def __init__(self, title):
        self.title = title
        self.done = False
    def mark_done(self):
        self.done = True
    def show(self):
        print(self.title, self.done)

task1 = TodoItem("学习文件读写")
task2 = TodoItem("学习异常处理")
task1.mark_done()
task1.show()
task2.show()
