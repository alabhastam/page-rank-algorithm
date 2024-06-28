matrix = []
num_iterations=5


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
    
# preventing from getting high numbers maybe sometimes later I add some logic when 
# nesbat was same in level stop doing things 

def normalize(arr):
    total_sum = sum(arr)
    if total_sum == 0:
        return [0] * len(arr)  # Handle the case where the sum is zero
    normalized_arr = [x / total_sum for x in arr]
    return normalized_arr



def pagerank(matrix ):
    
    show_step = 0 #add this for showing level of answer in termianl in a better way
    
    try:
        
        if len(matrix)==0 :
            raise ValueError(" matrix should not be empty.")

        r = [1 / len(matrix)] * len(matrix)  #PageRank vector with equal values

        
        #main functionality
        for any in range(num_iterations):
            new_r = [0] * len(matrix)
            for i in range(len(matrix)):
                new_r[i] = sum(matrix[i][j] * r[j] for j in range(len(matrix)))
            r = new_r
            show_step += 1
            print("answer of matrix in step ", show_step, "is:", r)
            print("normilzed of this step is : ", normalize(r))
            
            
        return r
    
    #why I add this? if row != column we get a error for zero division 
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
    
    
    
#next time you came back think you need to normilize your numbers
