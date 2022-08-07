def display():
    return """
    --------------------------------------------
    |  Is word valid:                          | 
    |                                          |
    |  Get Anagrams:                           |  
    |                                          |    
    |  Is Anagram:                             |   
    |                                          |   
    --------------------------------------------       
    """


def menu():
    flag = False
    while not flag:
        command_input = input("Enter 'y' to continue and enter 'x' to exit ").lower()
        display()
        if command_input == "x":
            flag = True



