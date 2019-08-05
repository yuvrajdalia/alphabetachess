from game import *
from moves import *
class possibleR:
	def __init__(self,i):
		self.i=i
		ans=""
		r=i//8
		c=i%8
		self.p=game()

	def possibleR(self,i):
		ans=""
		r=i//8
		c=i%8
		temp=1
		for j in range(-1,2):
			try:
				
				while self.t[r+temp*j][c]==" ":
					oldpiece=self.t[r+temp*j][c]
					self.t[r][c]=" "
					self.t[r+temp*j][c]="R"
					if r+temp*j>=0:
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:				
							ans=ans+str(r)+str(c)+str(r+temp*j)+str(c)+oldpiece
					#backtracking
					self.t[r][c]="R"
					self.t[r+temp*j][c]=oldpiece
					temp=temp+1


				if self.t[r+temp*j][c].islower():
					oldpiece=self.t[r+temp*j][c]
					self.t[r][c]=" "
					self.t[r+temp*j][c]="R"
					if r+temp*j>=0:
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:
							ans=ans+str(r)+str(c)+str(r+temp*j)+str(c)+oldpiece+" "
					#backtracking
					self.t[r][c]="R"
					self.t[r+temp*j][c]=oldpiece

				temp=1


				while self.t[r][c+temp*j]==" ":
					oldpiece=self.t[r][c+temp*j]
					self.t[r][c]=" "
					self.t[r][c+temp*j]="R"
					if c+temp*j>=0:
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:
							ans=ans+str(r)+str(c)+str(r)+str(c+temp*j)+oldpiece
					#backtracking
					self.t[r][c]="R"
					self.t[r][c+temp*j]=oldpiece
					temp=temp+1


				if self.t[r][c+temp*j].islower():
					oldpiece=self.t[r][c+temp*j]
					self.t[r][c]=" "
					self.t[r][c+temp*j]="R"
					if c+temp*j>=0:
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:
							ans=ans+str(r)+str(c)+str(r)+str(c+temp*j)+oldpiece+" "
					#backtracking
					self.t[r][c]="R"
					self.t[r][c+temp*j]=oldpiece
				temp=1
			except:
				pass

		return ans