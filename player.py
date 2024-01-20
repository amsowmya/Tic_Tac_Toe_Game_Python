import random
from move import Move


class Player:

    HUMAN_MARKER = 'X'
    COMPUTER_MARKER = 'O'

    def __init__(self, is_human=True):
        self._ishuman = is_human

        if self._ishuman:
            self._marker = Player.HUMAN_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER 

    @property 
    def marker(self):
        return self._marker 

    def get_move(self):
        if self._ishuman:
            return self.get_human_move()
        else:
            return self.get_computer_move()
        
    def get_human_move(self):
        while True:
            user_input = int(input("Please enter your move (1 - 9): "))
            move = Move(user_input)

            if move.is_valid():
                break 
            else:
                print("Please enter you input between 1 to 9")
        return move 
    
    def get_computer_move(self):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print("Computer move 1-9 : ", move.value)
        return move 
    

