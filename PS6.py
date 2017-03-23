from random import randrange
#y="abcdefg"
#x="abcdefg"
#x="abxfg"

#longString="exponential"
#subString="polynomial"
#add blank spaces
longString=open("PS6DataFiles/csci3104_S2017_PS6_data_string_x.txt","r").read()
subString=open("PS6DataFiles/csci3104_S2017_PS6_data_string_y.txt","r").read()
#longString="abcdefgh"
#subString="abcde"



def cost(x,y,i,j,S):
	x = " " + x
	y = " " + y
	c_indel=1
	c_sub=1
	c_swap=1
	#print(S)
	sub=None
	c_indelUp=None
	c_indelLeft=None
	swap=None #initializ swap so it isn't chosen until its in bounds (swap doesn't make sense till i=1, j=1


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



	if j>1 and i>1: #swap op
		swap = 0
		swap=c_swap+S[i-2][j-2]
		if x[i-1] != y[j]:
			swap=swap+c_sub
		if x[i] != y[j-1]:
			swap=swap+c_sub

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


	while rows>0 or columns>0:
		currentOps=[]

		if rows>0:
			indelUp=S[rows-1][columns]

		if columns>0:
			indelLeft=S[rows][columns-1]

		if rows>0 and columns>0:
			sub=S[rows-1][columns-1]

		if rows>1 and columns>1:
			swap=S[rows-2][columns-2]

		least=min(sub, swap, indelLeft, indelUp)
		string=["sub","swap","indelLeft","indelUp"]
		L = [sub, swap, indelLeft, indelUp]

		index=0
		for var in L: #find values that are mins
			if var==least:
				currentOps.append(index)
			index=index+1

		if 0 in currentOps and 1 in currentOps: #if both sub and swap are minimums
			currentOps.pop(1) #get rid of swap because its probably 2 no-ops

		randIndex=randrange(0,len(currentOps)) #choose a random minimum if theres a tie
		stringIndex=currentOps[randIndex]

		if stringIndex == 0: # if its a sub operation check if its a sub or no op
			if S[rows-1][columns-1]==S[rows][columns]: # if no op
				ops.append("no ops" + " rows are " + str(rows) + " columns are " + str(columns))
			else:
				ops.append("sub "+" rows are " + str(rows) + " columns are " + str(columns))
		else:
			op = string[stringIndex]
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

def commonSubstring(x,l,S):
	x=" " + x
	if l>len(x):
		return "error"
	subStrings=[]
	rows = len(S)-1
	columns=len(S[0])-1
	currString=[]

	for j in range(0,2): #iterate through
		if j==0:
			iterator=rows
			fixed=columns
		if j==1:
			iterator=columns
			fixed=rows

		for i in range(iterator,0,-1):
			if j==0:
				diagonal1=i
				diagonal2=fixed
			if j==1:
				diagonal1=fixed
				diagonal2=i
			count=0
			currString=[]

			while diagonal1>0 and diagonal2>0:


				sub = S[diagonal1 - 1][diagonal2 - 1]
				indelLeft = S[diagonal1 - 1][diagonal2]
				indelUp = S[diagonal1][diagonal2 - 1]

				if S[diagonal1][diagonal2]==S[diagonal1-1][diagonal2-1] and sub <= min(indelLeft,indelUp): #if no op
					currString.append(x[diagonal1])
					diagonal1=diagonal1-1
					diagonal2=diagonal2-1
					count=count+1

				else: #if we've missed a letter start over in same diagonal
					if count>=l:
						subStrings.append(''.join(currString[::-1]))
					diagonal1=diagonal1-1
					diagonal2=diagonal2-1
					currString=[] #restart string
					count=0 # reset count



			if count >= l: #incase all things have matched until diagonal1>0 and diagonal2>0 we need to put found string into substrings list
				subStrings.append(''.join(currString[::-1]))

	for subber in reversed(subStrings):
		print (subber + '\n')

print(commonSubstring(longString,80,alignStrings(longString,subString)))

