print("How many pencils would you like to use: ")
while True:
    try:
        pencils = int(input())
        if pencils < 1:
            print("The number of pencils should be positive")
        else:
            break
    except ValueError:
        print("The number of pencils should be numeric")

print("Who will be the first (John, Jack): ")
while True:
    name = input()
    if name in ["Jack", "John"]:
        break
    else:
        print("Choose between 'John' and 'Jack'")

current_player = name
print('|' * pencils)

while pencils > 0:
    print(current_player + "'s turn")
    while True:
        if current_player == "Jack":
            if pencils % 4 == 0: 
                taking_pencils = 3
            elif pencils % 4 == 3:
                taking_pencils = 2
            else:
                taking_pencils = 1
            print(taking_pencils)
            break
        elif current_player == "John":
            try:
                taking_pencils = int(input())
                if taking_pencils not in [1, 2, 3]:
                    print("Possible values: '1', '2' or '3'")
                elif taking_pencils > pencils:
                    print("Too many pencils were taken")
                else:
                    break
            except Exception:
                print("Possible values: '1', '2' or '3'")

    pencils -= taking_pencils
    print('|' * pencils)

    current_player = "John" if current_player == "Jack" else "Jack"

print(f"{current_player} won!")