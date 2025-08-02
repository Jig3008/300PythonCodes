# Number of rows
N = 5

# Outer loop runs N times, once for each row
for i in range(1, N + 1):
	# Inner loop prints 'N - i' spaces
	for j in range(1, N - i + 1):
		print(" ", end="")
		
	# Inner loop prints 'i' stars
	for j in range(1, i + 1):
		print("*", end="")
	# Move to the next line
	print()