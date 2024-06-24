matrix1 = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],]


#print(matrix1)

#trying diffrent method for using matrix

Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row): 
	a = []
	# A for loop for column entries
	for column in range(Column): 
		a.append(int(input()))
	matrix.append(a)

# For printing the matrix
for row in range(Row):
	for column in range(Column):
		print(matrix[row][column], end=" ")
	print()

#also I search about wht if I can ask user for inputing properties of pages





