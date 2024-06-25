matrix = []
def request():
    Row = int(input("Enter the number of rows:"))
    Column = int(input("Enter the number of columns:"))
    if Row == Column :
        
        print("in this section you have input "+ str(Row * Column) +" numbers for relations between pages")

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
            
        return matrix

request()