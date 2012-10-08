
height = input("How high do you want your box? ")
width = input("How wide do you want your box? ")

height = int(height)
width = int(width)	

for i in range(height):
	for j in range(width):
		if i is 0 or i is height-1 or j is 0 or j is width-1:
			print("#", end="")
		else:
			print(" ", end="")
	print("")