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
	sub=0
	swap=10000 #initializ swap so it isn't chosen until its in bounds (swap doesn't make sense till i=1, j=1
	print("i is " + str(i) + " x[i] is " + x[i-1] + " j is " + str(j) + " y[j] is " + str(y[j-1]))
	c_indel1 = c_indel + S[i][j-1]

	if x[i]==y[j]: #sub operation
		sub=S[i-1][j-1]
	else:
		sub=c_sub+S[i-1][j-1]
	if j==1:
		c_indel2 = c_indel + S[i-1][j]

	if j>2 and i>2: #swap op
		swap = 0
		swap=c_swap+S[i-2][j-2]
		if x[i-1] != y[j]:
			swap=swap+c_sub
		if x[i] != y[j-1]:
			swap=swap+c_sub
		#S[i][i] = S[i-2][i-2] + c_swap
	print ("c_sub is " + str(sub) + " c_swap " + str(swap) + " c_indel1 " + str(c_indel1) + " c_indel2 " + str(c_indel2) + "\n")
	#print("min is " + str(min(sub,swap,c_indel2,c_indel1)))#,c_indel1,c_indel2)))

	S[i][j]=min(sub,swap,c_indel1,c_indel2)

def alignStrings():
	#cost(S,1,2)
	print(S)
	print(ny)
	print(nx)
	i=1
	for j in range(1,ny):
		#print("i is" + str(i))
		cost(i, j)
		#for j in range (1,ny):
			#print ("j is" + str(j))
			#cost(i,j)
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