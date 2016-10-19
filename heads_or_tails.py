import random

random_number=random.randrange(0, 10)
guess=input("heads or tails")

if random_number%2==0:
    coin="tails"
else
    coin="heads"

if guess==coin:
    print("You win")
else
    print("You loose")
