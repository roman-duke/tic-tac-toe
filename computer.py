from board import Board
import random
import copy

class Computer(object):
    def __init__(self, board, maximizer="x", minimizer="o", mode="3"):
        self.board = board
        self.piece1 = maximizer
        self.piece2 = minimizer
        self.mode = mode.lower()

    def think(self) -> None:
        #Thought process of the computer is based off the minimax algorithm
        max_score, draw_score, min_score = 10, 0, -10
        
        def best_move(board, piece=None):
            if piece == None: piece = self.piece1

            player = piece

            available_pos = [i[0] for i in board.moves.items() if i[1] == " "]

            if player == self.piece1:
                scores = []
                for pos in available_pos:
                    temp_board = copy.deepcopy(board)
                    temp_board.move(pos, self.piece1)

                    if temp_board.game_win(): scores.append(max_score); break

                    elif (not temp_board.game_win()) and (" " not in temp_board.moves.values()): scores.append(draw_score); break

                    else: scores.append(best_move(temp_board, self.piece2))

                return (max(scores), available_pos[scores.index(max(scores))])

            elif player == self.piece2:
                scores = []
                for pos in available_pos:
                    temp_board = copy.deepcopy(board)
                    temp_board.move(pos, self.piece2)

                    if temp_board.game_win(): scores.append(min_score); break

                    elif (not temp_board.game_win()) and (" " not in temp_board.moves.values()): scores.append(draw_score); break

                    else: scores.append(best_move(temp_board, self.piece1)[0])

                return min(scores)

        if self.mode=="1":
            available_pos = [i[0] for i in self.board.moves.items() if i[1] == " "]
            self.board.move(random.choice(available_pos), self.piece1)

        elif self.mode=="2":
            if [i for i in self.board.moves.values() if i == " "].count(" ") >= 8:
                pos = random.choice([i[0] for i in self.board.moves.items() if i[1] == " "])
                self.board.move(pos, self.piece1)
            
            else: self.board.move(best_move(self.board)[1], self.piece1)

        elif self.mode=="3":
            if self.piece1 == "x" and "x" not in self.board.moves.values(): 
                pos = random.choice(["1", "3", "7", "9"])
                self.board.move(pos, self.piece1)

            else: self.board.move(best_move(self.board)[1], self.piece1)