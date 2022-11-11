
def swapAdjecent(l):	

	if len(l) %2 == 0:
		for i in range(0, len(l), 2):
			l[i], l[i+1] = l[i+1], l[i]
	else:
		for i in range(0, len(l)-1, 2):
			l[i], l[i+1] = l[i+1], l[i]

	return l

if __name__ == "__main__":
	list = ['a','b','c','d']
	print(swapAdjecent(list))


