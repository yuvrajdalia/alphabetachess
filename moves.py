from game import *
from possibleQ import *
from possibleK import *
from possibleP import *
from possibleR import *
from possibleB import *
from scratch import *
class moves:
	def __init__(self):
		self.ans=""

	def checking(self):
		self.p=game()
		#self.p.show()
		for i in range(64):
				if self.p.t[i//8][i%8]=="P":
					self.pP=possibleP(i)
					self.ans=self.ans+self.pP.calcmove()
				elif self.p.t[i//8][i%8]=="K":
					self.pK=possibleK(i)
					self.ans=self.ans+self.pK.calcmove()
				elif self.p.t[i//8][i%8]=="R":
					self.pR=possibleR(i)
					self.ans=self.ans+self.pR.calcmove()
				elif self.p.t[i//8][i%8]=="B":
					self.pB=possibleB(i)
					self.ans=self.ans+self.pB.calcmove()
				elif self.p.t[i//8][i%8]=="Q":
					self.pQ=possibleQ(i)
					self.ans=self.ans+self.pQ.calcmove()
				elif self.p.t[i//8][i%8]=="A":
					self.pA=scratch(i)
					self.ans=self.ans+self.pA.calcmove()
		return self.ans