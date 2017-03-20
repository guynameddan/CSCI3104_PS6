def alignStrings(x,y):
	S = []
	nx = len(x)
	ny = len(y)
	for i in range(0,nx + 1):
		for j in range (0,ny + 1):
			S[i,j] = cost(i,j)

	return S

# having trouble with the cost function guys.
# this is the hardest part of alignStrings.
# if you read the L7 notes you should be able
# to understand what I have down.
def cost(i,j):
	c_indel = 1
	c_sub = 10
	c_swap = 0

	# this brings back the value of a swap
	# based on the character(s) we are looking
	# at
	if x[i] = y [j-1] and x[i-1] = y[j]:
		c_swap = 10
	if x[i] = y [j-1] and x[i-1] != y[j]:
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

	return min(C_swap,C_sub,C_indel1,C_indel2)