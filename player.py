class Player(object):
    def __init__(self, piece, other):
        self.other = other
        self.piece = piece
        
    def move(self, pos):
        self.other.move(pos, self.piece)