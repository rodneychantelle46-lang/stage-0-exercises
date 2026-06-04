def get_guess():
    try:
        number = int(input("请输入一个整数:"))
        return number
    except ValueError:
        print("输入无效，请输入一个整数。")
        return None

def check_guess(guess, secret):
    if guess == secret:
        return "猜对了"
    elif guess < secret:
        return "猜小了" 
    else:
        return "猜大了"
    
def play_game():
    secret = 372
    guess = 0
    tries = 0

    while guess != secret:
        guess = get_guess()
        if guess is None:
            continue
        tries += 1

        message = check_guess(guess, secret)
        print(message)
    
    print("你猜对了！你一共猜了" , tries , "次")
play_game()