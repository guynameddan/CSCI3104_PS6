import numpy
from random import randrange
x="exponential"
y="polynomial"
#add blank spaces
x= " " + x
y= " " + y

nx = len(x)
ny = len(y)

#S = numpy.zeros((nx, ny),dtype=numpy.int)  # add row of zeros
S = [[0]*ny for i in range(nx)]
print(S)
print(ny)
print(nx)

def cost(i,j):
	c_indel=1
	c_sub=1
	c_swap=1
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

def alignStrings():
	for i in range(0,nx):
		for j in range (0,ny):
			cost(i,j)
	for row in S:
		print (str(row) + "\n")
	return S

def extractAlignment(S):
	ops=[]
	print("in function")
	columns=len(S[0])-1
	rows=len(S)-1
	print(rows)
	print(columns)
	print S[11][10]
	print S

	while rows>0 or columns>0:
		currentOps=[]
		if rows>0:
			indelUp=S[rows-1][columns]
			print("up " + str(indelUp))

		if columns>0:
			indelLeft=S[rows][columns-1]
			print("left " + str(indelLeft))

		if rows>0 and columns>0:
			sub=S[rows-1][columns-1]
			print ("sub " + str(sub))

		if rows>1 and columns>1:
			swap=S[rows-2][columns-2]
			print("swap " + str(swap))

		least=min(sub, swap, indelLeft, indelUp)
		string=["sub","swap","indelLeft","indelUp"]
		L = [sub, swap, indelLeft, indelUp]
		index=0
		print("list is" + str(least))
		for var in L: #find values that are mins
			if var==least:
				currentOps.append(index)
				print (index)
			index=index+1

		randIndex=randrange(0,len(currentOps)) #choose a random minimum if theres a tie
		stringIndex=currentOps[randIndex]
		op=string[stringIndex]
		print("operationg chosen " + op)
		ops.append(op)
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


#print(alignStrings())
print(extractAlignment(alignStrings()))

