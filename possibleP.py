from game import *
from moves import *
class possibleP:
	def __init__(self,i):
		self.i=i
		ans=""
		r=i//8
		c=i%8
		self.p=game()
	def possibleP(self,i):
		ans=""
		r=i//8
		c=i%8
		for j in range(-1,2,2):
			try:
				if self.t[r-1][c+j].islower() and self.i>=16:
					oldpiece=self.t[r-1][c+j]
					self.t[r][c]=" "
					self.t[r-1][c+j]="P"
					if r-1>=0 and c+j>=0:
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:
							ans=ans+str(r)+str(c)+str(r-1)+str(c+j)+oldpiece+" "
					#backtracking
					self.t[r][c]="P"
					self.t[r-1][c+j]=oldpiece
			except:
				pass

			try:
				if self.t[r-1][c+j].islower() and self.i<16:
					temp=["Q","R","B","K"]
					for k in range(0,4):
						oldpiece=self.t[r-1][c+j]
						self.t[r][c]=" "
						self.t[r-1][c+j]=temp[k]
						if r-1>=0 and c+j>=0:
							self.g=kingsafe(self.p,self.p.kingC)
							if self.g.test()==True:
							#column1,column2,captured-pice,new-piece,P
								ans=ans+str(c)+str(c+j)+oldpiece+temp[k]+"P"+" "
						#backtracking
						self.t[r][c]="P"
						self.t[r-1][c+j]=oldpiece
			except:
				pass
		try:
			if self.t[r-1][c]==" " and self.i>=16:
					oldpiece=self.t[r-1][c]
					self.t[r][c]=" "
					self.t[r-1][c]="P"
					if r-1>=0 and c>=0:
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:
							ans=ans+str(r)+str(c)+str(r-1)+str(c)+oldpiece
					#backtracking
					self.t[r][c]="P"
					self.t[r-1][c]=oldpiece
		except:
			pass


		try:
			if self.t[r-1][c]==" " and self.i<16:
				temp=["Q","R","B","K"]
				for k in range(0,4):
					oldpiece=self.t[r-1][c]
					self.t[r][c]=" "
					self.t[r-1][c]=temp[k]
					if r-1>=0 and c+j>=0:
						self.g=kingsafe(self.p,self.p.kingC)
						if self.g.test()==True:
					#column1,column2,captured-pice,new-piece,P
							ans=ans+str(c)+str(c)+oldpiece+temp[k]+"P"+" "
					#backtracking
					self.t[r][c]="P"
					self.t[r-1][c]=oldpiece
		except:
			pass

		try:
			if self.t[r-2][c]==" " and self.t[r-1][c]==" " and self.i>=48:
				oldpiece=self.t[r-2][c]
				self.t[r][c]=" "
				self.t[r-2][c]="P"
				if r-2>=0 and c>=0:
					self.g=kingsafe(self.p,self.p.kingC)
					if self.g.test()==True:
						ans=ans+str(r)+str(c)+str(r-2)+str(c)+oldpiece
				#backtracking
				self.t[r][c]="P"
				self.t[r-2][c]=oldpiece
		except:
			pass
		return ans