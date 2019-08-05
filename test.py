from game import *
from Rating import *
from flipboard import *
class board1:
	def __init__(self):
		self.t=[["r","k","b","q","a","b","k","r" ],
				["p","p","p","p","p","p","p","p" ],
				[" "," "," "," "," "," "," "," " ],
				[" "," "," "," "," "," "," "," " ],
				[" "," "," "," "," "," "," "," " ],
				[" "," "," "," "," "," "," "," " ],
				["P","P","P","P","P","P","P","P" ],
				["R","K","B","Q","A","B","K","R" ]]


class alphabeta:
	def __init__(self,depth,beta,alpha,move,player):
		self.depth=depth
		self.alpha=alpha
		self.beta=beta
		self.move=move
		self.player=player
		self.list=""
		self.kingC=60
		self.kingL=4
		self.pawnBoard=[[ 0,  0,  0,  0,  0,  0,  0,  0],
						[50, 50, 50, 50, 50, 50, 50, 50],
						[10, 10, 20, 30, 30, 20, 10, 10],
						[ 5,  5, 10, 25, 25, 10,  5,  5],
						[ 0,  0,  0, 20, 20,  0,  0,  0],
						[ 5, -5,-10,  0,  0,-10, -5,  5],
						[ 5, 10, 10,-20,-20, 10, 10,  5],
						[ 0,  0,  0,  0,  0,  0,  0,  0]]

		self.rookBoard=[[ 0,  0,  0,  0,  0,  0,  0,  0],
						[ 5, 10, 10, 10, 10, 10, 10,  5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[ 0,  0,  0,  5,  5,  0,  0,  0]]

		self.knightBoard= [[-50,-40,-30,-30,-30,-30,-40,-50],
						   [-40,-20,  0,  0,  0,  0,-20,-40],
						   [-30,  0, 10, 15, 15, 10,  0,-30],
						   [-30,  5, 15, 20, 20, 15,  5,-30],
						   [-30,  0, 15, 20, 20, 15,  0,-30],
						   [-30,  5, 10, 15, 15, 10,  5,-30],
						   [-40,-20,  0,  5,  5,  0,-20,-40],
						   [-50,-40,-30,-30,-30,-30,-40,-50]]

		self.bishopBoard=[[-20,-10,-10,-10,-10,-10,-10,-20],
						  [-10,  0,  0,  0,  0,  0,  0,-10],
						  [-10,  0,  5, 10, 10,  5,  0,-10],
						  [-10,  5,  5, 10, 10,  5,  5,-10],
						  [-10,  0, 10, 10, 10, 10,  0,-10],
						  [-10, 10, 10, 10, 10, 10, 10,-10],
						  [-10,  5,  0,  0,  0,  0,  5,-10],
						  [-20,-10,-10,-10,-10,-10,-10,-20]]

		self.queenBoard=[[-20,-10,-10, -5, -5,-10,-10,-20],
						 [-10,  0,  0,  0,  0,  0,  0,-10],
						 [-10,  0,  5,  5,  5,  5,  0,-10],
						 [ -5,  0,  5,  5,  5,  5,  0, -5],
						 [  0,  0,  5,  5,  5,  5,  0, -5],
						 [-10,  5,  5,  5,  5,  5,  0,-10],
						 [-10,  0,  5,  0,  0,  0,  0,-10],
						 [-20,-10,-10, -5, -5,-10,-10,-20]]

		self.kingMidBoard=[[-30,-40,-40,-50,-50,-40,-40,-30],
						   [-30,-40,-40,-50,-50,-40,-40,-30],
						   [-30,-40,-40,-50,-50,-40,-40,-30],
						   [-30,-40,-40,-50,-50,-40,-40,-30],
						   [-20,-30,-30,-40,-40,-30,-30,-20],
						   [-10,-20,-20,-20,-20,-20,-20,-10],
						   [ 20, 20,  0,  0,  0,  0, 20, 20],
						   [ 20, 30, 10,  0,  0, 10, 30, 20]]

		self.kingEndBoard=[[-50,-40,-30,-20,-20,-30,-40,-50],
						   [-30,-20,-10,  0,  0,-10,-20,-30],
						   [-30,-10, 20, 30, 30, 20,-10,-30],
						   [-30,-10, 30, 40, 40, 30,-10,-30],
						   [-30,-10, 30, 40, 40, 30,-10,-30],
						   [-30,-10, 20, 30, 30, 20,-10,-30],
						   [-30,-30,  0,  0,  0,  0,-30,-30],
						   [-50,-30,-30,-30,-30,-30,-30,-50]]

	def logic(self):
		self.list=self.moves()
		#print(self.list,"heya ")
		if self.depth==0 or len(self.list)==0:
			return self.move+str((self.Rating(len(self.list),self.depth))*(self.player*2-1))
		#print(self.list)
		self.list=self.sortmove(self.list)
		#print(self.list)
		self.player=1-self.player #either 1 or 0
		for i in range(0,len(self.list),5):
			self.change(self.list[i:i+5])
			self.flipboard()
			rtn=alphabeta(self.depth-1,self.beta,self.alpha,self.list[i:i+5],self.player)
			rtnstr=rtn.logic()
			val=int(rtnstr[5:])
			self.flipboard()
			self.unchange(self.list[i:i+5])
			if self.player==0:
				if val<=self.beta:
					self.beta=val
					if self.depth==4:
						self.move=rtnstr[0:5]
			else:
				if val>self.alpha:
					self.alpha=val
					if self.depth==4:
						self.move=rtnstr[0:5]
			if self.alpha>=self.beta:
				if self.player==0:
					return self.move+str(self.beta)
				else:
					return self.move +str(self.alpha)

		if self.player==0:
			return self.move + str(self.beta) 
		else:
			return self.move + str(self.alpha)

	def moves(self):
		ans=""
		#self.show()
		for i in range(64):
				if board.t[i//8][i%8]=="P":
					ans=ans+self.possibleP(i)
				elif board.t[i//8][i%8]=="R":
					ans=ans+self.possibleR(i)
				elif board.t[i//8][i%8]=="K":
					ans=ans+self.possibleK(i)
				elif board.t[i//8][i%8]=="B":
					ans=ans+self.possibleB(i)
				elif board.t[i//8][i%8]=="Q":
					ans=ans+self.possibleQ(i)
				elif board.t[i//8][i%8]=="A":
					ans=ans+self.possibleA(i)
					#self.show()
		return ans

	def show(self):
		for i in range(9):
			if i ==0:
				print(" ",end=" ")
			else:
				print(i-1,end=" ")
		print()
		for i in range(8):
			for j in range(9):
				if j==0:
					print(i,end=" ")
				else:
					print(board.t[i][j-1],end=" ")
			print()

	def possibleP(self,i):
		#print("i was called")
		ans=""
		r=i//8
		c=i%8
		for j in range(-1,2,2):
			try:
				#print("i was called")
				if board.t[r-1][c+j].islower() and i>=16:
					#print("i was called")
					oldpiece=board.t[r-1][c+j]
					board.t[r][c]=" "
					board.t[r-1][c+j]="P"
					if r-1>=0 and c+j>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r-1)+str(c+j)+oldpiece
					#backtracking
					board.t[r][c]="P"
					board.t[r-1][c+j]=oldpiece

				if board.t[r-1][c+j].islower() and i<16:
					temp=["Q","R","B","K"]
					for k in range(0,4):
						oldpiece=board.t[r-1][c+j]
						board.t[r][c]=" "
						board.t[r-1][c+j]=temp[k]
						if r-1>=0 and c+j>=0:
							if self.kingsafe()==True:
							#column1,column2,captured-pice,new-piece,P
								ans=ans+str(c)+str(c+j)+oldpiece+temp[k]+"P"
						#backtracking
						board.t[r][c]="P"
						board.t[r-1][c+j]=oldpiece
			except:
				pass

		try:
			if board.t[r-1][c]==" " and i>=16:
					#print("i was called")
					oldpiece=board.t[r-1][c]
					board.t[r][c]=" "
					board.t[r-1][c]="P"
					if r-1>=0 and c>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r-1)+str(c)+oldpiece
					#backtracking
					board.t[r][c]="P"
					board.t[r-1][c]=oldpiece
		
			if board.t[r-1][c]==" " and i<16:
					temp=["Q","R","B","K"]
					for k in range(0,4):
						oldpiece=board.t[r-1][c]
						board.t[r][c]=" "
						board.t[r-1][c]=temp[k]
						if r-1>=0 and c+j>=0:
							if self.kingsafe()==True:
						#column1,column2,captured-pice,new-piece,P
								ans=ans+str(c)+str(c)+oldpiece+temp[k]+"P"
						#backtracking
						board.t[r][c]="P"
						board.t[r-1][c]=oldpiece
			#print(i,ans)

			if board.t[r-2][c]==" " and board.t[r-1][c]==" " and i>=48:
					oldpiece=board.t[r-2][c]
					board.t[r][c]=" "
					board.t[r-2][c]="P"
					if r-2>=0 and c>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r-2)+str(c)+oldpiece
					#backtracking
					board.t[r][c]="P"
					board.t[r-2][c]=oldpiece

		except:
			pass

		#print(i,ans)
		return ans

	def possibleK(self,i):
		ans=""
		r=i//8
		c=i%8	
		j=-1
		while j<2:
			k=-1
			while k<2:
				try:
					if (board.t[r + j][c+ k*2]==" " or board.t[r+j][c+k*2].islower()) :
						oldpiece=board.t[r+j][c+k*2]
						board.t[r][c]=" "
						board.t[r+j][c+k*2]="K"
						if self.kingsafe()==True:
							if r+j>=0 and c +k*2>=0:
								ans=ans+str(r)+str(c)+str(r+j)+str(c+k*2)+oldpiece
						board.t[r][c]="K"
						board.t[r+j][c+k*2]=oldpiece
				except:
					pass
				k=k+2
			j=j+2
	
		j=-1
		while j<2:
			k=-1
			while k<2:
				try:
					if (board.t[r+2*j][c+ k]==" " or board.t[r+j*2][c+k].islower()) :
						oldpiece=board.t[r+j*2][c+k]
						board.t[r][c]=" "
						board.t[r+j*2][c+k]="K"
						if self.kingsafe()==True:
							if r+j*2>=0 and c +k>=0:											
								ans=ans+str(r)+str(c)+str(r+j*2)+str(c+k)+oldpiece
						board.t[r][c]="K"
						board.t[r+j*2][c+k]=oldpiece
				except:
					pass
				k=k+2
			j=j+2
		return ans

	def possibleR(self,i):
		ans=""
		r=i//8
		c=i%8
		temp=1
		for j in range(-1,2):
			try:	
				while board.t[r+temp*j][c]==" ":
					oldpiece=board.t[r+temp*j][c]
					board.t[r][c]=" "
					board.t[r+temp*j][c]="R"
					if r+temp*j>=0:
						if self.kingsafe()==True:				
							ans=ans+str(r)+str(c)+str(r+temp*j)+str(c)+oldpiece
					#backtracking
					board.t[r][c]="R"
					board.t[r+temp*j][c]=oldpiece
					temp=temp+1


				if board.t[r+temp*j][c].islower():
					oldpiece=board.t[r+temp*j][c]
					board.t[r][c]=" "
					board.t[r+temp*j][c]="R"
					if r+temp*j>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r+temp*j)+str(c)+oldpiece
					#backtracking
					board.t[r][c]="R"
					board.t[r+temp*j][c]=oldpiece

				temp=1


				while board.t[r][c+temp*j]==" ":
					oldpiece=board.t[r][c+temp*j]
					board.t[r][c]=" "
					board.t[r][c+temp*j]="R"
					if c+temp*j>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r)+str(c+temp*j)+oldpiece
					#backtracking
					board.t[r][c]="R"
					board.t[r][c+temp*j]=oldpiece
					temp=temp+1


				if board.t[r][c+temp*j].islower():
					oldpiece=board.t[r][c+temp*j]
					board.t[r][c]=" "
					board.t[r][c+temp*j]="R"
					if c+temp*j>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r)+str(c+temp*j)+oldpiece
					#backtracking
					board.t[r][c]="R"
					board.t[r][c+temp*j]=oldpiece
				temp=1
			except:
				pass

		return ans

	def possibleB(self,i):
		ans=""
		r=i//8
		c=i%8
		temp=1
		for j in range(-1,2,2):
			for k in range(-1,2,2):
				try:
					#print("here",board.t[r+temp*j][c+temp*k])
					while board.t[r+temp*j][c+temp*k]==" ":
						#print("here")
						oldpiece=board.t[r+temp*j][c+temp*k]
						board.t[r][c]=" "
						board.t[r+temp*j][c+temp*k]="B"
						if r+temp*j>=0 and c+temp*k>=0:
							if self.kingsafe()==True:
								ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece
						#backtracking
						board.t[r][c]="B"
						board.t[r+temp*j][c+temp*k]=oldpiece
						temp=temp+1

					if board.t[r+temp*j][c+temp*k].islower():
						oldpiece=board.t[r+temp*j][c+temp*k]
						board.t[r][c]=" "
						board.t[r+temp*j][c+temp*k]="B"
						if r+temp*j>=0 and c+temp*k>=0:
							if self.kingsafe()==True:
								ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece
						#backtracking  
						board.t[r][c]="B"
						board.t[r+temp*j][c+temp*k]=oldpiece
					temp=1
				except:
					pass

		return ans

	def possibleQ(self,i):
		ans=""
		r=i//8
		c=i%8
		temp=1
		for j in range(-1,2):
			for k in range(-1,2):
				try:
					while board.t[r+temp*j][c+temp*k]==" ":
						#print(r+temp*j,c+temp*k)
						oldpiece=board.t[r+temp*j][c+temp*k]
						board.t[r][c]=" "
						board.t[r+temp*j][c+temp*k]="Q"
						if r+temp*j>=0 and c+temp*k>=0:
							if self.kingsafe()==True:						
								ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece
						#backtracking
						board.t[r][c]="Q"
						board.t[r+temp*j][c+temp*k]=oldpiece
						temp=temp+1

					if board.t[r+temp*j][c+temp*k].islower():
						oldpiece=board.t[r+temp*j][c+temp*k]
						board.t[r][c]=" "
						board.t[r+temp*j][c+temp*k]="Q"
						if r+temp*j>=0 and c+temp*k>=0:
							if self.kingsafe()==True:						
								ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece
						#backtracking  
						board.t[r][c]="Q"
						board.t[r+temp*j][c+temp*k]=oldpiece
					temp=1

				except:
					pass
		return ans

	def possibleA(self,i):
		ans=""
		r = i // 8
		c = i % 8
		for j in range(9):
			try:
				if j != 4:
					if ((r - 1 + j // 3) < 0 or (c - 1 + j % 3) < 0):
						raise NameError()
					if (board.t[r-1+j//3][c-1+j%3] == " " or board.t[r - 1 + j // 3][c-1+j%3].islower()):
						oldpiece = board.t[r - 1 + j // 3][c - 1 + j % 3]	
						board.t[r][c] = " "
						board.t[r - 1 + j // 3][c - 1 + j % 3] = "A"
						kingtemp = self.kingC
						self.kingC = i + (j // 3) * 8 + (j % 3) * 8 - 9
						if self.kingsafe() == True:
							ans = ans + str(r) + str(c) + str((r - 1 + j // 3)) + str((c - 1 + j % 3)) + oldpiece
						board.t[r][c] = "A"
						board.t[r - 1 + j // 3][c - 1 + j % 3] = oldpiece
						self.kingC = kingtemp
			except:
				pass
		return ans
	
	def kingsafe(self):
		#bishop+queen
		r=self.kingC//8
		c=self.kingC%8
		temp=1
		for j in range(-1,2,2):
			for k in range(-1,2,2):
				try:
					while board.t[r+temp*j][c+temp*k]==" ":
						temp=temp+1

					if board.t[r+temp*j][c+temp*k]=="b" or board.t[r+temp*j][c+temp*k]=="q" :
						return False
				except:
					pass
				temp=1
					
		#rook+queen
		for j in range(-1,2,2):
			try:			
				while board.t[r][c+temp*j]==" " and r+temp*j>=0 and r+temp*j<8:
					temp=temp+1
				#print(board.t[r+temp*j][c],r+temp*j,c)
				if board.t[r][c+temp*j]=="r" or board.t[r][c+temp*j]=="q":
					return False
			except:
				pass
			temp=1
			try:
				while board.t[r+temp*j][c]==" " and c+temp*j>=0 and c+temp*j<8:
					temp=temp+1
				if board.t[r+temp*j][c]=="r" or board.t[r+temp*j][c]=="q":
					return False
			except:
				pass
			temp=1

		#knight
		for i in range(-1,2,2):
			for j in range(-1,2,2):
				try:
					if board.t[r+i][c+j*2]=="k":
						return False
				except:
					pass
				try:
					if board.t[r+i*2][c+j]=="k":
						return False
				except:
					pass

		#pawn	
		if self.kingC>=16:
			try:
				if board.t[r -1][c-1]=="p":
					return False
			except:
				pass
			try:
				if board.t[r-1][c-1]=="p":
					return False
			except:
				pass

		#king
		for i in (-1,2):
			for j in (-1,2):
				if(i!=0 or j!=0):
					try:
						if board.t[r+i][c+j]=="a":
							return False
					except:
						pass
		return True

	def flipboard(self):
		for i in range(32):
			r=i//8
			c=i%8
			if board.t[r][c].isupper()==True:
				temp=board.t[r][c].lower()
			else:
				temp=board.t[r][c].upper()
			if board.t[7-r][7-c].isupper()==True:
				board.t[r][c]=board.t[7-r][7-c].lower()
			else:
				board.t[r][c]=board.t[7-r][7-c].upper()
			board.t[7-r][7-c]=temp
		kingtemp1=self.kingC
		self.kingC=63-self.kingL
		self.kingL=63-kingtemp1

	def Rating(self,lent,depth):
		counter=0
		material=self.rateMaterial()
		counter=counter+self.rateAttack()
		counter=counter+material
		counter=counter+self.rateMoveability(lent,depth,material)
		counter=counter+self.ratePosition(material)
		self.flipboard()
		material=self.rateMaterial()
		counter=counter-self.rateAttack()
		counter=counter-material
		counter=counter-self.rateMoveability(lent,depth,material)
		counter=counter-self.ratePosition(material)
		self.flipboard()
		#print(-(counter+depth*50),depth,"mai yaha hu")
		return -(counter+depth*50)

	def ratePosition(self,material):
		count=0
		for i in range(64):
			r=i//8
			c=i%8
			if board.t[r][c]=='P':
				count=count+self.pawnBoard[r][c]
			elif board.t[r][c]=='R':
				count=count+self.rookBoard[r][c]
			elif board.t[r][c]=='B':
				count=count+self.bishopBoard[r][c]
			elif board.t[r][c]=='K':
				count=count+self.knightBoard[r][c]
			elif board.t[r][c]=='Q':
				count=count+self.queenBoard[r][c]
			elif board.t[r][c]=='A':
				if material>=1750:
					count=count+self.kingMidBoard[r][c]
					count=count+len(self.possibleA(self.kingC))*10		
				else:
					count=count+self.kingEndBoard[r][c]
					count=count+len(self.possibleA(self.kingC))*30					

		return count

	def rateMoveability(self,lent,depth,material):
		count=0
		count=count+lent
		if lent==0:
			if self.kingsafe()==False:
				count=count+(-200000)*depth
			else:
				count=count+(-150000)*depth
		return count

	def rateMaterial(self):
		count=0
		biscount=0
		for i in range(64):
			if board.t[i//8][i%8]=='P':
				count=count+100
			elif board.t[i//8][i%8]=='R':
				count=count+500
			elif board.t[i//8][i%8]=='K':
				count=count+300
			elif board.t[i//8][i%8]=='B':
				biscount=biscount+1
			elif board.t[i//8][i%8]=='Q':
				count=count+900
		if biscount>=2:
			count=count+300*biscount
		elif biscount==1:
			count=count+250
		return count

	def rateAttack(self):
		count=0
		temp=self.kingC
		for i in range(64):
			r=i//8
			c=i%8
			if board.t[r][c]=='P':
				self.kingC=i
				if self.kingsafe()==False:
					count=count-64
			elif board.t[r][c]=='R':
				self.kingC=i
				if self.kingsafe()==False:
					count=count-500
			elif board.t[r][c]=='K':
				self.kingC=i
				if self.kingsafe()==False:
					count=count-300
			elif board.t[r][c]=='B':
				self.kingC=i
				if self.kingsafe()==False:
					count=count-300
			elif board.t[r][c]=='Q':
				self.kingC=i
				if self.kingsafe()==False:
					count=count-900
		self.kingC=temp
		if self.kingsafe()==False:
			count=count-200
		return count//2

	def change(self,ans):
		if ans[4]!="P":
			#print("here i am")
			board.t[int(ans[2])][int(ans[3])]=board.t[int(ans[0])][int(ans[1])]
			board.t[int(ans[0])][int(ans[1])]=" "
			if "A"==board.t[int(ans[2])][int(ans[3])]:
				self.kingC=int(ans[2])*8+int(ans[3])
		else:
			board.t[1][int(ans[0])]=" "
			board.t[0][int(ans[1])]=int(ans[2])
			#self.show()

	def unchange(self,ans):
			if ans[4]!="P":
				board.t[int(ans[0])][int(ans[1])]=board.t[int(ans[2])][int(ans[3])]
				board.t[int(ans[2])][int(ans[3])]=" "
				if "A"==board.t[int(ans[0])][int(ans[1])]:
					self.kingC=int(ans[0])*8+int(ans[1])
			else:
				board.t[1][int(ans[0])]="P"
				board.t[0][int(ans[1])]=int(ans[3])

	def sortmove(self,list):
		score=[0 for i in range(len(self.list)//5)]
		for i in range(0,len(self.list)//5,5):
			self.change(self.list[i:i+5])
			score[i//5]=-self.Rating(-1,0)
			self.unchange(self.list[i:i+5])
		newListA=""
		newListB=self.list
		for i in range(0,min(6,len(self.list)//5)):   #checking few moves only
			maximum=-1000000
			maxLocation=0
			for j in range(0,len(self.list)//5):
				if score[j]>maximum:
					maximum=score[j]
					maxLocation=j
			score[maxLocation]=-1000000
			newListA=newListA+self.list[maxLocation*5:maxLocation*5+5]
			newListB=newListB.replace(self.list[maxLocation*5:maxLocation*5+5],"")

		return newListA+newListB

	def playermove(self,s):
		board.t[int(s[2])][int(s[3])]=board.t[int(s[0])][int(s[1])]
		board.t[int(s[0])][int(s[1])]=" "

	def letzdoit(self,move):
		print("your move ")
		self.playermove(move)
		self.show()
		strr=self.logic()
		self.change(strr[0:5])
		print(strr)
		print("my move")
		self.show()


def main():
	print("hey this is alphabeta chess enter the moves in the from of 1234b ")
	global board
	board=board1()
	ab=alphabeta(4, 1000000, -1000000,"", 0)
	ab.show()
	while True:
		s=input("enter the move ")
		ab.letzdoit(s)
	#s=input("enter the move ")
	#ab.letzdoit(s)
	#s=input("enter the move ")
	#ab.letzdoit(s)


if __name__ == '__main__':
	main()