import random
# import random.randint(1, 100)


def random_num():
    target = random.randint(1, 100)
    i = 0
    while i < 7:
        num = int(input("Guess a number: "))
        if num > target:
            print("too high")
        elif num < target:
            print("too low")
        else:
            print("correct")
        i += 1
    check = input("play again? (y/n):")
    match check:
        case "y":
            random_num()
        case "n":
            return


random_num()
