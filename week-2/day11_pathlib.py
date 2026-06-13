from pathlib import Path
file = Path("sample.txt")

if file.exists():
    content = file.read_text(encoding="utf-8")
    lines = content.splitlines()
    count = len(lines)
    print(f"文件行数: {count}")
    for number, line in enumerate(lines, start=1):
        print(number, line)
else:
    print("文件不存在")

folder = Path(".")
if folder.exists():
    for py_file in folder.glob("*.py"):
        print(py_file.name)
else:
    print("文件夹不存在")
