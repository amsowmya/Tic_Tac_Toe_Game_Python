from board import Board 
from player import Player


class TicTacToeGame:

    def start(self):
        print("**************************************************")
        print(" WELCOME TO TIC-TAC-TOE ")
        print("**************************************************")

        board = Board() 
        player = Player()
        computer = Player(is_human=False)

        board.print_board()

        while True:
            while True:
                player_move = player.get_move() 
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_game_over(player, player_move):
                    print("Awesome you won the game!")
                    break 
                elif board.check_is_tie():
                    print("It's a tie.. Try again")
                    break 
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("Oops computer won the game. Try again")
                        break 

            play_again = input("Would you like to play again? Press 'X' to continue or 'O' to exit: ").upper()

            if play_again == 'O':
                print("Bye! come back soon")
                break 
            elif play_again == 'X':
                self.start_new_round(board) 
            else:
                print("Your input was not valid I assume that you want to play again..!")
                self.start_new_round(self) 

    def start_new_round(self, board):
        print("************")
        print(" NEW ROUND")
        print("***********")
        board.reset_board()
        board.print_board()
        

game = TicTacToeGame()
game.start()