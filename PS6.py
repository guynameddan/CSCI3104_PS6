import numpy
x="exponential"
y="polynomial"
#add blank spaces
x= " " + x
y= " " + y

nx = len(x)
ny = len(y)

S = numpy.zeros((nx, ny))  # add row of zeros

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

	print( "left"+str(S[i][j-1]))

	if i==0 and j==0:
		c_indelLeft=0
	if j>0:
		c_indelLeft = c_indel + S[i][j-1]

	if i>0: #only use top indel if i>0
		print("i is greater ")
		c_indelUp = c_indel + S[i - 1][j]

	if i>0 and j>0:#sub operation
		if x[i]==y[j]: #no op
			sub=S[i-1][j-1]
		else:
			print("i is " + str(i)+ "j is " + str(j))
			print("previous sub is " + str(S[i-1][j-1]))
			sub=c_sub+S[i-1][j-1]
		print("top is " + str(c_indelUp))


	if j>2 and i>2: #swap op
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
	#cost(S,1,2)
	for i in range(0,nx):
		#print("i is" + str(i))
		#cost(i, j)

		for j in range (0,ny):
			print ("j is" + str(j))
			cost(i,j)
	print(S)



print(alignStrings())
# having trouble with the cost function guys.
# this is the hardest part of alignStrings.
# if you read the L7 notes you should be able
# to understand what I have down.
#print(alignStrings("Ape","Step"))


"""
	c_indel = 1
	c_sub = 10
	c_swap = 0

	# this brings back the value of a swap
	# based on the character(s) we are looking
	# at
	if x[i]=y[j-1] and x[i-1] = y[j]:
		c_swap = 10
	if x[i] = y[j-1] and x[i-1] != y[j]:
		c_swap = 20
	if x[i] != y [j-1] and x[i-1] = y[j]:
		c_swap = 20
	if x[i] != y [j-1] and x[i-1] != y[j]:
		c_swap = 30

	# this is for two characters that are the same
	# i.e. a no-op
	if x[i] = y[j]
		c_indel = c_sub = c_swap = 0

	C_swap = S[i-2,j-2] + c_swap
	C_sub = S[i-1,j-1] + c_sub
	C_indel1 = S[i-1,j] + c_indel
	C_indel2 = S[i,j-1] + c_indel

	return min(C_swap,C_sub,C_indel1,C_indel2)"""