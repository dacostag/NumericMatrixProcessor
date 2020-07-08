def request_matrix():
    n, m = map(int, input().split())
    return [list(map(int, input().split())) for _ in range(n)]

def add_matrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("ERROR")
        return []
    else:
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

matrix_1, matrix_2 = request_matrix(), request_matrix()

for row in add_matrix(matrix_1, matrix_2):
    print(*row)