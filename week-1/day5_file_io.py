with open("todo.txt", "w",  encoding="utf-8")as f:
    f.write("1.学函数\n")
    f.write("2.学文件读写\n")
with open("todo.txt", "a", encoding="utf-8") as f:
    f.write("3.学异常处理\n")
with open("todo.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)