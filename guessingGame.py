secret_word = "zebra"
inp = input("Guess the word in 3 tries: ")
guess_count = 1
guess_limit = 3
out_of_guesses = False

while inp != secret_word:
    if guess_count < guess_limit:
        inp = input("Guess again: ")
        guess_count += 1
    else:
        out_of_guesses = True
        break

if(out_of_guesses):
    print("Out of guesses, you lost!")
else:
    print("You win!")