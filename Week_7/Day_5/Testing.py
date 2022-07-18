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
    position_entered = input("Please enter your position")
    position_entered_int = int(position_entered)
    if 1 <= position_entered_int <= 9 and position_entered in show_list_default:
        print(position_entered_int)
        print("Testing: ")
        print(show_list_default[position_dic[position_entered_int]])
        position_entered_int = position_dic[position_entered_int]
        if player is "Player_X":
            show_list_default[position_entered_int] = "X"
            print(' '.join(show_list_default))
        elif player is "Player_O":
            show_list_default[position_entered_int] = "O"
            print(' '.join(show_list_default))
    elif show_list_default[position_dic[position_entered_int]] is "X":
        print("Already taken")
    elif show_list_default[position_dic[position_entered_int]] is "O":
        print("Already taken")
    else:
        print("Wrong input")


players = ["Player_X", "Player_O"]

counter = 0
flag = False
while counter < 9 or flag is False:
    for play in players:
        counter = counter + 1
        player_input(play)
        print("Win?")
        if show_list_default[position_dic[1]] is show_list_default[position_dic[2]] is \
                show_list_default[position_dic[3]]:
            flag = True
            print("Winner")
        elif show_list_default[position_dic[4]] is show_list_default[position_dic[5]] is \
                show_list_default[position_dic[6]]:
            flag = True
            print("Winner")
        elif show_list_default[position_dic[7]] is show_list_default[position_dic[8]] is  \
                show_list_default[position_dic[9]]:
            flag = True
            print("Winner")

        elif show_list_default[position_dic[1]] is show_list_default[position_dic[4]] is \
                show_list_default[position_dic[7]]:
            flag = True
            print("Winner")

        elif show_list_default[position_dic[2]] is show_list_default[position_dic[5]] is \
                show_list_default[position_dic[8]]:
            flag = True
            print("Winner")

        elif show_list_default[position_dic[3]] is show_list_default[position_dic[6]] is \
                show_list_default[position_dic[9]]:
            flag = True
            print("Winner")

        elif show_list_default[position_dic[1]] is show_list_default[position_dic[5]] is \
                show_list_default[position_dic[9]]:
            flag = True
            print("Winner")

        elif show_list_default[position_dic[3]] is show_list_default[position_dic[5]] is \
                show_list_default[position_dic[7]]:
            flag = True
            print("Winner")
    break
else:
    print("No winner")
