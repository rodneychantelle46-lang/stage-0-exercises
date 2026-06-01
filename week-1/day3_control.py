score = 50
if score >= 60 :
    print("pass")
else :
    print("fail")

for hobbies in ["AI", "reading", "fitness"] :
    print(hobbies)

count = 3

while count > 0 :
    print(count)
    count = count - 1

print("go")


secret = 217
guess = 0
tries = 0
while secret != guess :
    guess = int(input("请输入一个数字："))
    tries = tries + 1

    if guess == secret :
        print("猜对了")
    elif guess < secret :
        print("猜小了")
    else :
        print("猜大了") 

print("你总共猜了", tries, "次")