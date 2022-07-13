print("Tic Tac Toe")
show = \
    " * * * * * * * * * * * * * \n" \
    " *   1   |   2   |   3   * \n" \
    " * - - - | - - - | - - - * \n" \
    " *   4   |   5   |   6   * \n" \
    " * - - - | - - - | - - - * \n" \
    " *   7   |   8   |   9   * \n" \
    " * * * * * * * * * * * * * "

# show_list = [
#     " * * * * * * * * * * * * * ",
#     " *   1   |   2   |   3   * ",
#     " * - - - | - - - | - - - * ",
#     " *   4   |   5   |   6   * ",
#     " * - - - | - - - | - - - * ",
#     " *   7   |   8   |   9   * ",
#     " * * * * * * * * * * * * * "
# ]
#
# print(show_list)


def display():
    # display_grid_list =  \
    #     " * * * * * * * * * * * * * \n"\
    #     " *   1   |   2   |   3   * \n"\
    #     " * - - - | - - - | - - - * \n"\
    #     " *   4   |   5   |   6   * \n"\
    #     " * - - - | - - - | - - - * \n"\
    #     " *   7   |   8   |   9   * \n"\
    #     " * * * * * * * * * * * * * "
    print(show)


position_list = {
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
player_list = ["Player_X", "Player_O"]
show_list_default = list(show)


def player_input(player):

    position_enter = int(input("Enter the position "))

    possible_position = range(1, 10)
    for n in possible_position:
        if position_enter is n:
            position_enter = position_list[n]
            # print(position_enter)
            # n_to_string = str(n)
            # print(show_list)
            # index = show_list.index(n_to_string)
            # print(index)
            if player is "Player_X":
                show_list_default[position_enter] = "X"
                # print(show_list)
                # a = ' '.join(show_list_default)
                # print(a)
            else:
                show_list_default[position_enter] = "O"
                # print(show_list)
                # a = ' '.join(show_list_default)
                # print(a)
            # a = ' '.join(show_list_default)
            # print(a)
        # else:
        #     print(position_list[position_enter])
            # if position_list[position_enter] is "X" or "O":
            #     print("Taken")
            #     break

    a = ' '.join(show_list_default)
    print(a)


# elif position_enter is "X":
#     print("Already Taken")
# elif position_enter is "O":
#     print("Already Taken")

# def check_win ():


counter = 0
while counter < 1:

    for player1 in player_list:
        counter = counter + 1
        print(counter)
        print("It's is the {}'s turn".format(player1))
        player_input(player1)
