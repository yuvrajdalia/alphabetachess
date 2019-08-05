from alphabeta import *
class game:
	def __init__(self):
		self.wert=""

def main():
	print("hey this is alphabeta chess enter the moves in the from of 1234b ")
	ab=alphabeta(4, 1000000, -1000000,"", 0)
	ab.show()
	s=input("enter the move ")
#	ab=alphabeta(4, 1000000, -1000000,"", 0)
	ab.letzdoit(s)
	s=input("enter the move ")
#	ab=alphabeta(4, 1000000, -1000000,"", 0)
	ab.letzdoit(s)
	s=input("enter the move ")
#	ab=alphabeta(4, 1000000, -1000000,"", 0)
	ab.letzdoit(s)
	#s=input("enter the move ")
	#ab.letzdoit(s)



if __name__ == '__main__':
	main()