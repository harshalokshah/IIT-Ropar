n=int(input('Enter the numbere of rows in matrix:'))
matrix=[]
a=n
b=0
while n>0:
    b+=1
    row=[]
    for i in range(a):
        row.append(int(input(f'Enter the element of row {b} and column {i+1}:')))
    matrix.append(row)
    n-=1
print(matrix)
for i in range(len(matrix)):
    print((matrix[i])[i])