
secret_number = str("4")
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_number and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Number: ")
        guess_count += 1
        if guess_count <= 1:
            print("Hint: Number is less than 8. ")
        if guess_count == 2:
            print("Hint: Number is more than 2. ")
        if guess_count == 4:
            print("Hint: Number is between 3 and 6. ")

    else:
        out_of_guesses = True


if out_of_guesses:
    print("Too bad, you lose!")

else:
    print("Conglaturation! ")

Variant = ""