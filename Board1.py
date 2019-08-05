from Board import *
class Board1:
    def __init__(self):
        self.a=Board()

    def printe(self):
        for i in range(8):
            for j in range(8):
                print(self.a.t[i][j], end=" ")
            print()