class Board:
	def __init__(self):
		self.t=[["r","k","b","q","a","b","k","r" ],
				["p","p","p","p","p","p","p","p" ],
				[" "," "," "," "," "," "," "," " ],									
				[" "," "," "," "," "," "," "," " ],									
				[" "," "," "," "," "," "," "," " ],									
				[" "," "," "," "," "," "," "," " ],									
				["P","P","P","P","P","P","P","P" ],									
				["R","K","B","Q","A","B","K","R" ]]
		self.kingC=60
		self.kingL=4

	def show(self):
		for i in range(8):
			for j in range(8):
				print(self.t[i][j],end=" ")
			print()

	def change(self,ans):
		i=len(ans)//5
		for j in range(i):
			if ans[j*5+4]!="P":
				self.t[int(ans[j*5+2])][int(ans[j*5+3])]=self.t[int(ans[j*5+0])][int(ans[j*5+1])]
				self.t[int(ans[j*5+0])][int(ans[j*5+1])]=" "
				if "A"==self.t[int(ans[j*5+2])][int(ans[j*5+3])]:
					self.kingC=int(ans[j*5+2])*8+int(ans[j*5+3])
			else:
				self.t[1][int(ans[j*5+0])]=" "
				self.t[0][int(ans[j*5+1])]=int(ans[j*5+2])
			#self.show()
			j=j+1
	
	def unchange(self,ans):
		i=len(ans)//5
		for j in range(i):
			if ans[j*5+4]!="P":
				self.t[int(ans[j*5+0])][int(ans[j*5+1])]=self.t[int(ans[j*5+2])][int(ans[j*5+3])]
				self.t[int(ans[j*5+2])][int(ans[j*5+3])]=" "
				if "A"==self.t[int(ans[j*5+0])][int(ans[j*5+1])]:
					self.kingC=int(ans[j*5+0])*8+int(ans[j*5+1])
			else:
				self.t[1][int(ans[j*5+0])]="P"
				self.t[0][int(ans[j*5+1])]=int(ans[j*5+3])
			#self.show()
			j=j+1
