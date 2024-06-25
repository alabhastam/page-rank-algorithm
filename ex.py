matrix = []

def request():
    Row = int(input("Enter the number of rows:"))
    Column = int(input("Enter the number of columns:"))
    if Row == Column :
        
        print("in this section you have input "+ str(Row * Column) +" numbers for relations between pages")

        #For user input
        # A for loop for row entries
        for row in range(Row): 
            a = []
            #A for loop for column entries
            for column in range(Column): 
                a.append(int(input()))
            matrix.append(a)

        # For printing the matrix
        for row in range(Row):
            for column in range(Column):
                print(matrix[row][column], end=" ")
            print()
        
        return matrix
    

def pagerank(matrix, num_iterations=100):
    
    len(matrix)  
    r = [1 / len(matrix)] * len(matrix)  #PageRank vector with equal values

    #make columns sum to 1
    for j in range(len(matrix)):
        col_sum = sum(matrix[i][j] for i in range(len(matrix)))
        if col_sum != 0:
            for i in range(len(matrix)):
                matrix[i][j] /= col_sum
        else:
            for i in range(len(matrix)):
                matrix[i][j] = 1.0 / len(matrix)

    #PageRank calculation
    for _ in range(num_iterations):
        new_r = [0] * len(matrix)
        for i in range(len(matrix)):
            new_r[i] = sum(matrix[i][j] * r[j] for j in range(len(matrix)))
        r = new_r

    return r


 
if __name__ == "__main__":
    
    
    request()
    ranks = pagerank(matrix)
    print("PageRank vector:", ranks)
