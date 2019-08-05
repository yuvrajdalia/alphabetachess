from Board import *
class flipboard:
	def __init__(self):
		self.p=Board()
	def flipboard(self):
		for i in range(32):
			r=i//8
			c=i%8
			if self.t[r][c].isupper()==True:
				temp=self.t[r][c].lower()
			else:
				temp=self.t[r][c].upper()
			if self.t[7-r][7-c].isupper()==True:
				self.t[r][c]=self.t[7-r][7-c].lower()
			else:
				self.t[r][c]=self.t[7-r][7-c].upper()
			self.t[7-r][7-c]=temp
		self.kingC=63-self.kingC
		self.kingL=63-self.kingL
		 