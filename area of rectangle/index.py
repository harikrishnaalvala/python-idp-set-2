def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0 
    for row in matrix: 
        for i in range(n):
            height[i] = height[i] + 1 if row[i] == 'X' else 0 
        stack = [-1]
        for i in range(n + 1):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()] 
                w=i-1- stack[-1]
                ans = max(ans, h * w)  ;
            stack.append(i)
    return ans
def read_matrix(rows):
    matrix = []
    for i in range(rows):
        row = input().split()
        matrix.append(row)
    return matrix
def main():
    rows, columns = map(int, input().split(" "))
    matrix = read_matrix(rows)
    max_area_of_rectangle = maximalRectangle(matrix)
    print(max_area_of_rectangle)
main()
