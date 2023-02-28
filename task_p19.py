import random
number=random.randint(1,100)
guess_count=0
max_guess=7
print("I'm thinking of a number between 1-100. You have 7 guesses.")
while guess_count < max_guess:
    guess=int(input("Guess the number: "))
    guess_count += 1
    if guess==number:
        print("Perfect! You guess in {} tries.".format(guess_count))
        break
    elif guess<number:
        print("You are to low.")
    else:
        print("You are to high.")
if guess_count == max_guess:
    print("Sorry, You didn't guess it in {} tries. The number is {}.".format(max_guess,number))
