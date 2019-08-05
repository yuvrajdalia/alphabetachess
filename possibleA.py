from game import *
from moves import *
from kingsafe import *
class possibleA:
	def __init__(self,i):
		self.i=i
		self.ans=""
		self.r=i//8
		self.c=i%8
		self.p=game()
		
	def calcmove(self):
		for j in range(9):
			if j!=4:
				try:
					if((self.r-1+j//3)<0 or (self.c-1+j%3)<0):
						raise NameError()
					if (self.p.t[self.r-1+j//3][self.c-1+j%3]==" " or self.p.t[self.r-1+j//3][self.c-1+j%3].islower()) :
						oldpiece=self.p.t[self.r-1+j//3][self.c-1+j%3]
						self.p.t[self.r][self.c]=" "
						self.p.t[self.r-1+j//3][self.c-1+j%3]="A"
						kingtemp=self.p.kingC
						self.p.kingC=self.i+(j//3)*8+(j%3)*8-9
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:
							self.ans=self.ans+str(self.r)+str(self.c)+str((self.r-1+j//3))+str((self.c-1+j%3))+oldpiece
						self.p.t[self.r][self.c]="A"
						self.p.t[self.r-1+j//3][self.c-1+j%3]=oldpiece
						self.p.kingC=kingtemp
				except:
					pass
		return self.ans