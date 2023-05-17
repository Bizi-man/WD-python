import random

secret = print(random.randint(0,100))

quess = int(input("Guess the secret: "))

if guess == secret:
    print("Damn son you guessed it")
else:
    print("Nope try again!")