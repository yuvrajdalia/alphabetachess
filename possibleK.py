from game import *
from moves import *
from kingsafe import *
class possibleK:
	def __init__(self,i):
		self.i=i
		ans=""
		r=i//8
		c=i%8
		self.p=game()

	def possibleK(self,i):
		ans=""
		r=i//8
		c=i%8	
		j=-1
		while j<2:
			k=-1
			while k<2:
				try:
					if (self.t[r + j][c+ k*2]==" " or self.t[r+j][c+k*2].islower()) :
						oldpiece=self.t[r+j][c+k*2]
						self.t[r][c]=" "
						self.t[r+j][c+k*2]="K"
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:
							if r+j>=0 and c +k*2>=0:
								ans=ans+str(r)+str(c)+str(r+j)+str(c+k*2)+oldpiece
						self.t[r][c]="K"
						self.t[r+j][c+k*2]=oldpiece
				except:
					pass
				k=k+2
			j=j+2
	
		j=-1
		while j<2:
			k=-1
			while k<2:
				try:
					if (self.t[r+2*j][c+ k]==" " or self.t[r+j*2][c+k].islower()) :
						oldpiece=self.t[r+j*2][c+k]
						self.t[r][c]=" "
						self.t[r+j*2][c+k]="K"
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:
							if r+j*2>=0 and c +k>=0:											
								ans=ans+str(r)+str(c)+str(r+j*2)+str(c+k)+oldpiece
						self.t[r][c]="K"
						self.t[r+j*2][c+k]=oldpiece
				except:
					pass
				k=k+2
			j=j+2
		return ans