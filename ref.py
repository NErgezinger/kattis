r, c = map(int, input("Input number of rows, columns: ").split())
print(r, "rows,", c, "columns")

matrix = []


for i in range(r):
    row = list(map(int, input("Enter row " + str(i+1) + " separated by spaces: ").split()))
    matrix.append(row)

# check for zero rows
for i in range(len(matrix)-1,-1,-1):
    if sum(map(abs, matrix[i])) == 0:
        matrix.append(matrix.pop(i))

#for row in matrix:
 #   print(row)


for ri, row in enumerate(matrix):
    pass