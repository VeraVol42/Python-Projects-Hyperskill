import random

rating_file = open('rating.txt', 'r')
user_list = {}
lines = rating_file.readlines()
for line in lines:
    name, score = line.split()
    score = int(score)
    user_list[name] = score
rating_file.close()

def main():
    current_name = input("Enter your name: ")
    print(f"Hello, {current_name}")

    if current_name in user_list:
        current_score = user_list[current_name]
    else:
        current_score = 0

    options = input()
    if options == '':
        options = 'rock,paper,scissors'
    options_list = options.split(',')
    print("Okay, let's start")

    game(options_list, current_score)

def game(options_list, current_score):
    while True:
        user_choice = input()
        if user_choice == "!exit":
            print("Bye!")
            break
        elif user_choice == "!rating":
            print("Your rating:", current_score)
            continue
        elif user_choice not in options_list:
            print("Invalid input")
            continue

        index_user_choice = options_list.index(user_choice)
        new_list = options_list[index_user_choice + 1:] + options_list[:index_user_choice]
        loose_list = new_list[len(new_list) // 2:]
        computer_choice = random.choice(options_list)

        if user_choice == computer_choice:
            print(f"There is a draw ({computer_choice})")
            current_score += 50
        elif computer_choice in loose_list:
            print(f"Well done. The computer chose {computer_choice} and failed")
            current_score += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")

main()