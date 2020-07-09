def request_matrix():
    """Take two values, n and m, from input and return a matrix of n rows and m columns. Each row takes its values from input as well."""
    n, m = map(int, input().split())
    return [[int(num) for num in input().split()] for _ in range(n)]

def add_matrix(a, b):
    """Take two matrices and return their sum if possible. Else, return an empty list."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("ERROR")
        return []
    else:
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]  # Probably can be done with zips.

def scalar_product(m, s):
    """Return the scalar product of matrix m with scalar s."""
    return [[m[i][j] * s for j in range(len(m[0]))] for i in range(len(m))] # range(len(m))'s should be properties of the matrix. Or even just rows and columns.

def matrix_product(a, b):
    columns = [[b[i][j] for i in range(len(b))] for j in range(len(b[0]))]  # Property of each matrix.
    return [[dot_product(row, col) for col in columns] for row in a]

def dot_product(v1, v2):
    """Return the dot product between vectors v1 and v2."""
    return sum(num1 * num2 for num1, num2 in zip(v1, v2))
