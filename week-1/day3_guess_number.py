secret = 372
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