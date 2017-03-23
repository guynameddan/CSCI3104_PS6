from random import randrange
#y="abcdefg"
#x="abcdefg"
#x="abxfg"

#x="exponential"
#y="polynomial"
#add blank spaces
longString=open("PS6DataFiles/csci3104_S2017_PS6_data_string_x.txt","r").read()
subString=open("PS6DataFiles/csci3104_S2017_PS6_data_string_y.txt","r").read()
#longString="abcdefgh"
#subString="abcde"


#S = numpy.zeros((nx, ny),dtype=numpy.int)  # add row of zeros
def cost(x,y,i,j,S):
	x = " " + x
	y = " " + y
	c_indel=1
	c_sub=10
	c_swap=10
	#print(S)
	sub=None
	c_indelUp=None
	c_indelLeft=None
	swap=None #initializ swap so it isn't chosen until its in bounds (swap doesn't make sense till i=1, j=1
	#print("i is " + str(i) + " x[i] is " + x[i-1] + " j is " + str(j) + " y[j] is " + str(y[j-1]))

	#print( "left"+str(S[i][j-1]))

	if i==0 and j==0:
		c_indelLeft=0
	if j>0:
		c_indelLeft = c_indel + S[i][j-1]

	if i>0: #only use top indel if i>0
		c_indelUp = c_indel + S[i - 1][j]

	if i>0 and j>0:#sub operation
		if x[i]==y[j]: #no op
			sub=S[i-1][j-1]
		else:
			sub=c_sub+S[i-1][j-1]
		#print("top is " + str(c_indelUp))


	if j>1 and i>1: #swap op
		swap = 0
		swap=c_swap+S[i-2][j-2]
		if x[i-1] != y[j]:
			swap=swap+c_sub
		if x[i] != y[j-1]:
			swap=swap+c_sub

	#print ("c_sub is " + str(sub) + " c_swap " + str(swap) + " c_indel left " + str(c_indelLeft) + " c_indel2 ")# + str(c_indelUp) + "\n")
	#print("min is " + str(min(sub,swap,c_indel2,c_indel1)))#,c_indel1,c_indel2)))
	S[i][j]=min(value for value in [sub,swap,c_indelLeft,c_indelUp] if value is not None)

def alignStrings(x,y):
	nx = len(x)+1
	ny = len(y)+1
	S = [[0] * ny for i in range(nx)]
	for i in range(0,nx):
		for j in range (0,ny):
			cost(x,y,i,j,S)
	#for row in S:
		#print (str(row) + "\n")
	return S

def extractAlignment(S):
	ops=[]
	columns=len(S[0])-1
	rows=len(S)-1
	#print(rows)
	#print(columns)
	#print S

	while rows>0 or columns>0:
		currentOps=[]

		if rows>0:
			indelUp=S[rows-1][columns]
			#print("up " + str(indelUp))

		if columns>0:
			indelLeft=S[rows][columns-1]
			#print("left " + str(indelLeft))

		if rows>0 and columns>0:
			sub=S[rows-1][columns-1]
			#print ("sub " + str(sub))

		if rows>1 and columns>1:
			swap=S[rows-2][columns-2]
			#print("swap " + str(swap))

		least=min(sub, swap, indelLeft, indelUp)
		string=["sub","swap","indelLeft","indelUp"]
		L = [sub, swap, indelLeft, indelUp]

		#print("list is" + str(least))
		index=0
		for var in L: #find values that are mins
			if var==least:
				currentOps.append(index)
				#print(index)
			index=index+1

		#print ("current ops are " + str(currentOps))
		if 0 in currentOps and 1 in currentOps:
			#print("current ops is " + str(currentOps))
			currentOps.pop(1)
			#print("now it is "+ str(currentOps))

		randIndex=randrange(0,len(currentOps)) #choose a random minimum if theres a tie
		stringIndex=currentOps[randIndex]

		if stringIndex == 0: # if its a sub operation check if its a sub or no op
			if S[rows-1][columns-1]==S[rows][columns]: # if no op
				ops.append("no ops" + " rows are " + str(rows) + " columns are " + str(columns))
			else:
				ops.append("sub "+" rows are " + str(rows) + " columns are " + str(columns))
		else:
			op = string[stringIndex]
			# print("operationg chosen " + op)
			ops.append(op + " rows are " + str(rows) + " columns are " + str(columns))

	#decide which direction to move in table
		if stringIndex==0:
			columns = columns - 1
			rows = rows - 1
		if stringIndex==1:
			columns = columns - 2
			rows = rows - 2
		if stringIndex==2:
			columns = columns - 1
		if stringIndex==3:
			rows = rows - 1

	print(ops)

		#print (min(sub, swap, indelLeft, indelUp))

def commonSubstring(x,l,S):
	x=" " + x
	if l>len(x):
		return "error"

	subStrings=[]
	#print(len(S))
	#print(len(S[0]))
	#print(l)
	currString=[]
	#print(S[14][4])
	for j in range(len(S[0])-1,0,-1): #iterate through
		noop = True
		currString=[]
		#print "     i is " + str(i)
		#print("j is" + str(j))
		for i in range(len(S)-1,0,-1):
			#print ("      i is " + str(i))
			#print("start is " + str(S[i][j]) + " next is " + str(S[i - 1][j - 1]))
			#print("comparison is " + str(x[i]) + y[j])
			diagonal1=i
			diagonal2=j
			count=0
			currString=[]

			while diagonal1>0 or diagonal2>0:
				sub = S[diagonal1 - 1][diagonal2 - 1]
				indelLeft = S[diagonal1 - 1][diagonal2]
				indelUp = S[diagonal1][diagonal2 - 1]
				#print("diagonal 1 is " + str(diagonal1)+ " diagonal 2 is " + str(diagonal2) )
				#print(str(S[diagonal1][diagonal2]) + " and " + str(S[diagonal1-1][diagonal2-1]))

				if S[diagonal1][diagonal2]==S[diagonal1-1][diagonal2-1] and sub <= min(indelLeft,indelUp): #if no op
					#print("diag 1 is " + str(diagonal1)+ " diag2 is "+str(diagonal2))
					#print("matched letters are " + x[diagonal1] + " and " )#+ y[diagonal2])
					currString.append(x[diagonal1])
					diagonal1=diagonal1-1
					diagonal2=diagonal2-1
					count=count+1

				else:
					break
				if count==l:
					#currString.append(x[diagonal1])
					#print ("full string is " + str(currString[::-1]))
					subStrings.append(''.join(currString[::-1]))

					#print("found right length string " + str(subStrings), "diagonal is " + str(diagonal1))
					break
	for subber in subStrings:
		print (subber + '\n')

#print(alignStrings("exponential","polynomial"))

print(commonSubstring(longString,88,alignStrings(longString,subString)))
#print(alignStrings())
#print(extractAlignment(alignStrings()))

