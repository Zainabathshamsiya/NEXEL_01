def animal_game():
    animal = "elephant"  # Computer's chosen animal

    print("Welcome to the Animal Guessing Game!")
    print("Think of an animal and I'll try to guess it.")
    print("You can ask me yes-or-no questions.")

    while True:
        guess = input("Is it an " + animal + "? ").lower()

        if guess == "yes":
            print("Hooray! I guessed it right. It's an", animal.capitalize(), "!")
            break
        elif guess == "no":
            print("Oh no! That's not it.")
        else:
            print("I don't understand. Please answer with 'yes' or 'no'.")

animal_game()