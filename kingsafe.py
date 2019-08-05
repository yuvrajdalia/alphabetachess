class kingsafe:
	def __init__(self,bo,kc):
		self.p=bo
		self.kc=kc
		r=self.kc//8
		c=self.kc%8
		"""for i in range(8):
			for j in range(8):
				print(self.t[i][j],end=" ")
			print()"""

	def kingsafe(self):
		#bishop+queen
		r=self.kingC//8
		c=self.kingC%8
		temp=1
		for j in range(-1,2,2):
			for k in range(-1,2,2):
				try:
					while self.t[r+temp*j][c+temp*k]==" ":
						temp=temp+1

					if self.t[r+temp*j][c+temp*k]=="b" or self.t[r+temp*j][c+temp*k]=="q" :
						return False
					temp=1
				except:
					pass
		#rook+queen
		temp=1
		for j in range(-1,2,2):
			try:			
				while self.t[r+temp*j][c]==" " and r+temp*j>=0 and r+temp*j<8:
					temp=temp+1
				#print(self.t[r+temp*j][c],r+temp*j,c)
				if self.t[r+temp*j][c]=="r" or self.t[r+temp*j][c]=="q":
					return False
			except:
				pass
		temp=1
		for j in range(-1,2,2):
			try:
				while self.t[r][c+temp*j]==" " and c+temp*j>=0 and c+temp*j<8:
					temp=temp+1
				if self.t[r][c+temp*j]=="r" or self.t[r][c+temp*j]=="q":
					return False
				temp=1
			except:
				pass
		#knight
		j=-1
		while j<2:
			k=-1
			while k<2:
				try:
					if self.t[r + j][c+ k*2]=="k" :
						return False
				except:
					pass
				k=k+2
			j=j+2
		j=-1
		while j<2:
			k=-1
			while k<2:
				try:
					if self.t[r+2*j][c+ k]=="k":
						return False
				except:
					pass
				k=k+2
			j=j+2
		#pawn	
		if self.t[r -1][c-1]=="p":
			return False
		elif self.t[r-1][c-1]=="p":
			return False
		return True