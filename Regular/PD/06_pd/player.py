import random
class MyPlayer:
    '''The player is a random betrayal or cooperation.'''
    number_of_iterations = 20
    def __init__(self,payoff_matrix,number_of_iterations = 20):
        self.payoff=payoff_matrix
        # Define self.payoff
    def move(self):
        return random.choice([True,False])
        # ramdom bool number
    def record_last_moves(self,my_last_move,opponent_last_move):
        ml=my_last_move
        ol=opponent_last_move
        # Assignment Variables
