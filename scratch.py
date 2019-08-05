from game import *
from moves import *
from kingsafe import *


class scratch:
    def __init__(self, i):
        self.i = i
        ans = ""
        r = i // 8
        c = i % 8
        self.p = game()

    def possibleA(self,i):
        ans = ""
        r = i // 8
        c = i % 8
        for j in range(9):
            try:
                if j != 4:
                    if ((r - 1 + j // 3) < 0 or (c - 1 + j % 3) < 0):
                        raise NameError()
                    if (self.t[r - 1 + j // 3][c - 1 + j % 3] == " " or self.t[r - 1 + j // 3][
                        c - 1 + j % 3].islower()):
                        oldpiece = self.t[r - 1 + j // 3][c - 1 + j % 3]
                        self.t[r][c] = " "
                        self.t[r - 1 + j // 3][c - 1 + j % 3] = "A"
                        kingtemp = self.p.kingC
                        self.p.kingC = self.i + (j // 3) * 8 + (j % 3) * 8 - 9
                        self.g = kingsafe(self.p, self.p.kingC)
                        if self.g.test() == True:
                            ans = ans + str(r) + str(c) + str((r - 1 + j // 3)) + str(
                                (c - 1 + j % 3)) + oldpiece
                        self.t[r][c] = "A"
                        self.t[r - 1 + j // 3][c - 1 + j % 3] = oldpiece
                        self.p.kingC = kingtemp
            except:
                pass
        return ans