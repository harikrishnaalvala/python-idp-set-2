def sum_of_neighbours(matrix, i, j):
    matrix_length = len(matrix)
    matrix_row_length = len(matrix[0])
    neighbour_sum = 0
    if (i-1>=0):
        neighbour_sum += matrix[i - 1][j]
    if (i + 1 < matrix_length):
        neighbour_sum += matrix[i + 1][j]
    if (j-1>= 0):
        neighbour_sum += matrix[i][j - 1]
    if (j + 1 < matrix_row_length):
        neighbour_sum += matrix[i][j + 1]
    return neighbour_sum

def replacing_zeros(matrix, temp_matrix, rows, columns):
    neighbour_sum_set={}
    for i in range(rows):
        for j in range(columns):
            if (matrix[i][j] == 0):
                set_row(temp_matrix, i)
                set_column(temp_matrix, j)
                neighbour_sum_set[(i, j)] = sum_of_neighbours(matrix, i, j)

    for each_set in neighbour_sum_set:
        temp_matrix[each_set[0]][each_set[1]] = neighbour_sum_set[each_set]
    return temp_matrix
def set_row(temp_matrix, i):
    for column_index in range(len(temp_matrix[0])): 
        temp_matrix[i][column_index] =0
def set_column(temp_matrix, j):
    for row_index in range(len(temp_matrix)):
        temp_matrix[row_index][j] = 0
def read_matrix(rows):
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix
def create_matrix_copy(matrix):
    temp_matrix = []
    for row in matrix:
        temp_matrix.append(row.copy())
    return temp_matrix

def print_matrix(modified_matrix, rows, columns):
    for i in range(rows):   
        row = ""
        for j in range(columns):  
            row += str(modified_matrix[i][j]) +" "
        print (row) 
def main(): 
    rows, columns = map(int, input().split()) 
    matrix = read_matrix(rows)
    temp_matrix = create_matrix_copy(matrix)
    modified_matrix = replacing_zeros(matrix, temp_matrix, rows, columns)
    print_matrix(modified_matrix, rows, columns)
main()
                
                
                
                
                
                
                
                
                
                
                
                
                
