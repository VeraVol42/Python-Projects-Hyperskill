import random

win = 0
lost = 0

print("H A N G M A N\n")

while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    chose = input()
    
    if chose == "play":
        word_list = ["python", "java", "swift", "javascript"]
        attempts = 8 
        word = random.choice(word_list)
        replaced_word = "-" * len(word)
        letter_list = []
        
        while "-" in replaced_word and attempts > 0:
            print(replaced_word)
            print("Input a letter: ")
            letter_guess = input()
            temp_word = list(replaced_word)

            if len(letter_guess) != 1:
                print("Please, input a single letter.")
                continue
            elif str.islower(letter_guess) == False or str.isalpha(letter_guess) == False:
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if letter_guess in letter_list:
                print("You've already guessed this letter.")
            else:
                letter_list.append(letter_guess)
                
            if letter_guess in word:
                for i in range(len(word)):
                    if letter_guess == word[i] and replaced_word[i] == "-":
                        temp_word[i] = letter_guess
                    elif letter_guess == word[i] and replaced_word[i] != "-":
                        print("No improvements.")
                replaced_word = "".join(temp_word)
    
            elif letter_guess not in word:
                attempts -= 1
                print("That letter doesn't appear in the word.")

        if "-" not in replaced_word:
            print(f"\nYou guessed the word {word}!\nYou survived!")
            win += 1

        if attempts <= 0:
            print("You lost!")
            lost += 1

    elif chose == "results":
        print(f"You won: {win} times. You lost: {lost} times.")

    elif chose == "exit":
       break 
