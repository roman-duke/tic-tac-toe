class Board(object):
    def __init__(self):
        self.moves = {"1": " ", "2": " ", "3":" ", "4":" ", "5":" ", 
                        "6":" ", "7":" ", "8":" ", "9":" "}

    def move(self, pos, piece) -> None:
        self.moves[pos] = piece


    def game_win(self):
        if ((self.moves["1"] == self.moves["2"] == self.moves["3"] != " ") or (self.moves["1"] == self.moves["4"] == self.moves["7"] != " ") or (self.moves["1"] == self.moves["5"] == self.moves["9"] != " ") or \
            (self.moves["9"] == self.moves["3"] == self.moves["6"] != " ") or (self.moves["9"] == self.moves["8"] == self.moves["7"] != " ") or (self.moves["7"] == self.moves["5"] == self.moves["3"] != " ") or \
            (self.moves["2"] == self.moves["5"] == self.moves["8"] != " ") or (self.moves["4"] == self.moves["5"] == self.moves["6"] != " ")):
            return True
    
        else: return False

    def __str__(self):
        return f' {self.moves["1"]} | {self.moves["2"]} | {self.moves["3"]}\n' +\
               f'--- --- ---\n' + \
               f' {self.moves["4"]} | {self.moves["5"]} | {self.moves["6"]}\n' +\
               f'--- --- ---\n' + \
               f' {self.moves["7"]} | {self.moves["8"]} | {self.moves["9"]}\n'
            