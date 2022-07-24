import random


class Game:
    def __init__(self):
        flag = False

        while flag is False:
            user_item = input("Select (r)ock, (p)aper, or (s)cissors: ")
            if (user_item == "r") or (user_item == "p") or (user_item == "s"):
                print(f"{user_item} selected by user ")
                flag = True
            else:
                print("Wrong input")

    def get_computer_item(self):
        computer_choice_list = ["r", "p", "s"]
        computer_item = random.choice(computer_choice_list)
        print(f"{computer_item} selected by computer ")
        return computer_item

    def get_game_result(self, user_item, computer_item):
        counter_win = 0
        counter_loss = 0
        counter_draw = 0
        if (user_item == 'r' and computer_item == 'p') or (user_item == 'p' and computer_item == 'r') or\
                (user_item == 's' and computer_item == 'p'):
            counter_win += 1
            return counter_win
        elif (user_item == 'r' and computer_item == 'p') or (user_item == 'p' and computer_item == 's') or \
                (user_item == "s" and computer_item == 'r'):
            counter_loss += 1
            return counter_loss
        elif user_item == computer_item:
            counter_draw += 1
            return counter_draw
        print("finished")
        print(counter_win, counter_loss, counter_draw)

        mydict = {}

        mydict["win"] = counter_win
        mydict["loss"] = counter_loss
        mydict["draw"] = counter_draw
        results = mydict
        return results

    def play(self):
        pass


g = Game()
user_item1 = Game()
computer_item1 = g.get_computer_item()

print(g.get_game_result(user_item1, computer_item1))


def get_user_menu_choice():
    return \
        f"""
        Menu:
        (g) Play a new game
        (x) Show scores and exit
        {input("Input")}
        """
