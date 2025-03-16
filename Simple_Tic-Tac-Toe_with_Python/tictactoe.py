a = "         "
print(f"""---------
| {a[0]} {a[1]} {a[2]} |
| {a[3]} {a[4]} {a[5]} |
| {a[6]} {a[7]} {a[8]} |
---------""")

current_player = "X"

while True:
    x_str, y_str = input("Enter the coordinates: ").split()
    x = int(x_str)
    y = int(y_str)
    index = (((x - 1) * 3) + (y + 2)) - 3

    if x not in [1, 2, 3] or y not in [1, 2, 3]:
        print("Coordinates should be from 1 to 3!")
    
    elif a[index] != " ":
        print("This cell is occupied! Choose another one!")

    else:
        try:
            a = a[:index] + current_player + a[index+1:]
            print(f"""---------
| {a[0]} {a[1]} {a[2]} |
| {a[3]} {a[4]} {a[5]} |
| {a[6]} {a[7]} {a[8]} |
---------""")

            X_wins = (a[0] == "X" == a[1] == a[2]) or (a[3] == "X" == a[4] == a[5]) or (a[6] == "X" == a[7] == a[8]) or (a[0] == "X" == a[3] == a[6]) or (a[1] == "X" == a[4] == a[7]) or (a[2] == "X" == a[5] == a[8]) or (a[0] == "X" == a[4] == a[8]) or (a[2] == "X" == a[4] == a[6])
            O_wins = (a[0] == "O" == a[1] == a[2]) or (a[3] == "O" == a[4] == a[5]) or (a[6] == "O" == a[7] == a[8]) or (a[0] == "O" == a[3] == a[6]) or (a[1] == "O" == a[4] == a[7]) or (a[2] == "O" == a[5] == a[8]) or (a[0] == "O" == a[4] == a[8]) or (a[2] == "O" == a[4] == a[6])
            
            if X_wins:
                print("X wins")
                break

            if O_wins:
                print("O wins")
                break
                
            if current_player == "X":
                current_player = "O"
            elif current_player == "O":
               current_player == "X" 

        except ValueError:
            print("You should enter numbers!")


