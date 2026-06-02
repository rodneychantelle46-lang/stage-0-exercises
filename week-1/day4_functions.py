def say_hello(name):
    print("你好", name)

say_hello("陆恒成")
say_hello("AI")

def introduce(name, major, age):
     return "我是" + name + ",专业是" + major + ",今年" + str(age) + "岁"

message = introduce("陆恒成", "管理科学与工程", 23)
print(message)


def no_return(name):
    print("你好", name)

result = no_return("AI")