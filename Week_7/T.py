print("Tic Tac Toe")

show = \
        " * * * * * * * * * * * * * \n" \
        " *   1   |   2   |   3   * \n" \
        " * - - - | - - - | - - - * \n" \
        " *   4   |   5   |   6   * \n" \
        " * - - - | - - - | - - - * \n" \
        " *   7   |   8   |   9   * \n" \
        " * * * * * * * * * * * * * "


def display():
    print(show)


display()

position_dic = {
    1: 33,
    2: 41,
    3: 49,
    4: 89,
    5: 97,
    6: 105,
    7: 145,
    8: 153,
    9: 161
}
show_list_default = list(show)


def player_input(player):
    print(player)
    position_entered = int(input("Please enter your position"))

    if 1 <= position_entered <= 9:
        print(position_entered)
        print("Testing: ")
        print(show_list_default[position_dic[position_entered]])
        position_entered = position_dic[position_entered]
        if player is "Player_X":
            show_list_default[position_entered] = "X"
            print(' '.join(show_list_default))
        elif player is "Player_O":
            show_list_default[position_entered] = "O"
            print(' '.join(show_list_default))
    elif show_list_default[position_dic[position_entered]] is "X":
        print("Already taken")
    elif show_list_default[position_dic[position_entered]] is "O":
        print("Already taken")
    else:
        print("Wrong input")


players = ["Player_X", "Player_O"]
for play in players:
    player_input(play)
