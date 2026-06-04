def check_guess(guess,secret):
    if guess == secret:
        return "猜对了"
    elif guess < secret:
        return "猜小了" 
    else:
        return "猜大了"
    
def paly_game():
    secret = 372
    guess = 0
    tries = 0

    while guess != secret:
        guess = int(input("请输入一个数字："))
        tries = tries + 1

        message = check_guess(guess, secret)
        print(message)
    print("你猜对了！你一共猜了" , tries , "次")
    
play_game()