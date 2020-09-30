import random
hiddenNumber = random.randrange(1, 100)
chances = 4
print("Guess the number")
while chances != 0:
    guess = int(input())
    chances = chances-1
    if guess == hiddenNumber:
        print("You Won!")
        break
    elif guess > hiddenNumber:
        print("Smaller Number Please")
        print(chances, "chances left")
        continue
    else:
        print("Higher Number Please")
        print(chances, "chances left")
        continue
