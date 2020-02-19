
# Hangman Game 1 #
import turtle
# --- Define Variables --- #
word_of_choice = list(input("Enter your word\n"))
clue_for_player = input("Enter your Clue\n")
underscored_Word = list("")
lives_left = 10
length_of_word = len(word_of_choice)
Correct = False
for count in range(length_of_word):    # loop through each character and replace with an '_'
    if word_of_choice[count] == " ":        # if there is a space between the words, then ensure that
        underscored_Word += " "             # there is a space
    else:
        underscored_Word += "_"
print(str(underscored_Word))                     # display to the user
while underscored_Word != word_of_choice and lives_left > 0:
    guess_character = input("Enter your character guess\n")
    print(clue_for_player)
    for character in range(length_of_word):
        if guess_character == word_of_choice[character] or guess_character.capitalize() == word_of_choice[character]:
            underscored_Word[character] = word_of_choice[character]
            Correct = True
    if not Correct:
        lives_left -= 1
        print("Wrong! You have " + str(lives_left) + " lives left\n")
    print(underscored_Word)  # display to the user
    print(lives_left)
    Correct = False

if lives_left == 0:
    print("Failure!\n")                         # if you have lost all your lives that's game over
else:
    print("Success!\n")                         # otherwise, you have won
