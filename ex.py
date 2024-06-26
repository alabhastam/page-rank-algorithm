matrix = []
num_iterations=20

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
    

def pagerank(matrix ):
    
    try:
        
        if len(matrix)==0 :
            raise ValueError("The matrix should not be empty.")

        r = [1 / len(matrix)] * len(matrix)  #PageRank vector with equal values

        
        #PageRank calculation
        for _ in range(num_iterations):
            new_r = [0] * len(matrix)
            for i in range(len(matrix)):
                new_r[i] = sum(matrix[i][j] * r[j] for j in range(len(matrix)))
            r = new_r

        return r
    except ZeroDivisionError:
        print("Error: Division by zero encountered. The matrix might be empty or have an invalid structure.")


# I wrote this array just for ssorting and making code beutiful
def find_extremes(arr):
    
    # Sort the array to find the extremes easily
    sorted_arr = sorted(arr)
    
    # Find the smallest and largest elements
    smallest = sorted_arr[0]
    largest = sorted_arr[-1]
    
    # Find the second and third largest elements
    second_largest = sorted_arr[-2]
    third_largest = sorted_arr[-3]
    
    print("Smallest element:", smallest)
    print("Largest element:", largest)
    print("Second largest element:", second_largest)
    print("Third largest element:", third_largest)
    
    return smallest, largest, second_largest, third_largest



 
if __name__ == "__main__":
    
    
    request()
    pages = pagerank(matrix)
    print("rank of your pages are:", pages)
    find_extremes(pages)
