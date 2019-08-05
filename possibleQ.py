from game import *
from moves import *
class possibleQ:  
	def __init__(self,i):
		self.i=i
		ans=""
		r=i//8
		c=i%8
		self.p=game()

	def possibleQ(self,i):
		ans=""
		r=i//8
		c=i%8
		temp=1
		for j in range(-1,2):
			for k in range(-1,2):
				try:
					while self.t[r+temp*j][c+temp*k]==" ":
						#print(r+temp*j,c+temp*k)
						oldpiece=self.t[r+temp*j][c+temp*k]
						self.t[r][c]=" "
						self.t[r+temp*j][c+temp*k]="Q"
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:						
							ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece
						#backtracking
						self.t[r][c]="Q"
						self.t[r+temp*j][c+temp*k]=oldpiece
						temp=temp+1

					if self.t[r+temp*j][c+temp*k].islower():
						oldpiece=self.t[r+temp*j][c+temp*k]
						self.t[r][c]=" "
						self.t[r+temp*j][c+temp*k]="Q"
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:						
							ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece+" "
						#backtracking  
						self.t[r][c]="Q"
						self.t[r+temp*j][c+temp*k]=oldpiece


					temp=1

				except:
					pass
		return ans