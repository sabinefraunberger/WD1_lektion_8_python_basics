# guess the secret number - game
secret = 8
guess = int(input("Choose a number between 1 and 20: "))

if guess == secret:
    print("Yeah, you got it right! Congratulation! The secret number is 8.")
else:
    print("Sorry, that's wrong! The secret number isn't " + str(guess) + ".")
