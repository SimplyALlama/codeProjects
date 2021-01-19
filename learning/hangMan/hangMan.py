import random
import time

print("\nWelcome to the game\n")
name = input("What is your name? \n")
print("Hello " + name + "! Good Luck!")

time.sleep(2)

print("Lets start the game!")

time.sleep(3)


def main():
    global count
    global display
    global word
    global alreadyGuessed
    global wordLength
    global playGame

    # get a list of words from a text file
    wordsToGuessFrom = open("words.txt").read().split()

    # the word we will be trying to guess
    word = random.choice(wordsToGuessFrom)
    wordLength = len(word)

    display = "_" * wordLength

    alreadyGuessed = []  # words that have already been guessed

    playGame = ""


def playLoop():
    playGame = input("do you want to play again? y or n \n")

    # if the input is not expect ask again
    while playGame not in ["Y", "y", "N", "n"]:
        playGame = input("do you want to play again? y or n \n")

    if playGame == "Y" or "y":
        main()

    else:
        print("Thank you for playing!")
        exit()


def hangMan():
    global count
    global display
    global word
    global alreadGuessed
    global playGame

    count = 0

    limit = 5
    print("This is the hangman word " +
          display + " it has " + str(len(word)) + " letters.")
    guess = input("What is your next guess? \n")

    guess = guess.strip()
    if len(guess.strip()) != 1:
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        alreadyGuessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in alreadyGuessed:
        print("Try another letter.\n")

    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) +
                  " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed, word)
            play_loop()

    if word == '_' * wordLength:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangMan()


main()
hangMan()
