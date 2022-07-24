import random


class Game:
    # user chose between rock, paper, scissor
    def get_user_chose(self):
        user_chose = input("what's your choice?'r' for rock, 'p' for paper,'s' for scissors: ")
        return user_chose.lower()

    def get_computer_chose(self):
        return random.choice(['r', 'p', 's'])

    def is_player_win(self, player_choice, computer_choice):
        # winning condition r>s, s>p, p>r
        if (player_choice == 'r' and computer_choice == 's') or (player_choice == 's' and computer_choice == 'p') or \
                (player_choice == 'p' and computer_choice == 'r'):
            return True
        elif player_choice == computer_choice:
            return None

        return False

    # if get_user_chose == get_computer_chose:
    # 	print(f"you and computer have both chosen{get_computer_chose}. It is a tie")
    # # r>s, s>p, p>r
    # if is_win(get_user_chose, get_computer_chose):
    # 	print(f"you have chosen {get_user_chose} and the computer have chosen {get_computer_chose}. You won!.")
    #
    # print(f"you have chosen {get_user_chose} and the computer have chosen {get_computer_chose}. You lost!.")

    def start_game(self):
        player_choice = self.get_user_chose()
        computer_choice = self.get_computer_chose()
        print(f"user choice is {player_choice}\ncomputer choice is {computer_choice}")
        result = self.is_player_win(player_choice, computer_choice)
        if result == True:
            print("the player is the winner")
        elif result == None:
            print("this is a draw")
        else:
            print("The computer is the winner")


if __name__ == '__main__':
    Game().start_game()
