from words import words
from Hangman import lives_visual_dict
import random
import string

def valid(list_words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = valid(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    #print(f"Word: {word}")
    #print(f"The letters for your word are: {word_letters}")
    #print(f"Alphabet: {alphabet}")
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:

        print(f"You have {lives} lives / life left and you have used these letters: {', '.join(used_letters)}")

        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")

        print(lives_visual_dict[lives])
        print(f"Current word: {', '.join(word_list)}")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            print(f"used letters; {used_letters}")
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print()
            else:
                lives = lives - 1
                print(f"\n Your letter, {user_letter} is not in the word.")
        elif user_letter in used_letters:
            print(f"\nYou have used this letter b4")
        else:
            print(f"\nThat is a valid letter")

    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"You lost. The word was {word}")
    else:
        print(f"hooray! you answered it correctly!! The word was {word}")

if __name__ == "__main__":
    hangman()