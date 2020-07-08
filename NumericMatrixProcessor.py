n1, m1 = map(int, input().split())
matrix_1 = [input().split() for i in range(n1)]
n2, m2 = map(int, input().split())
matrix_2 = [input().split() for j in range(n2)]

if n1 != n2 or m1 != m2:
    print("ERROR")
else:
    matrix_sum = [[int(matrix_1[i][j]) + int(matrix_2[i][j]) for j in range(m1)] for i in range(n1)]
    for i in matrix_sum:
        print(*i)