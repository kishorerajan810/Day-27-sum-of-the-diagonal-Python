n=int(input("enter :"))
matrix , i ,j = [] ,0 ,[]
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input("enter:")))
    matrix.append(a)
while(n>0):
    x = abs(matrix[i][n-1] - matrix[i+1][n-2])
    j.append(x)
    n = n - 1
    i = i + 1
print(j)
