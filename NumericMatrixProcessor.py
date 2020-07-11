class Matrix:
    OP_ERROR = "The operation cannot be performed."

    def __init__(self, n=0, m=0, data=None):
        self.row_n = n
        self.col_n = m
        self.data = [data[m*i:m*(i+1)] for i in range(n)]  # Probably should add self.rows = self.data for clarity.
        self.columns = [data[i::m] for i in range(m)]

    def __repr__(self):
        return "\n".join(" ".join(str(num) for num in row) for row in self.data)

    def __add__(self, other):
        """If both matrices have the same number of rows and columns, return a new Matrix with the sum. Else, print OP_ERROR and return an empty Matrix."""
        if isinstance(other, Matrix) and self.row_n == other.row_n and self.col_n == other.col_n:
            return Matrix(self.row_n, self.col_n, [a + b for a_row, b_row in zip(self.data, other.data) for a, b in zip(a_row, b_row)])
        else:
            print(self.OP_ERROR)
            return Matrix()

    def __mul__(self, other):
        """If other is type float or int, return the scalar product. If other is type Matrix, return the matrix product. Else, print OP_ERROR and return an empty Matrix."""
        if isinstance(other, (int, float)):
            return Matrix(self.row_n, self.col_n, [a * other for a_row in self.data for a in a_row])
        elif isinstance(other, Matrix):
            return Matrix(self.row_n, other.col_n, [self.dot_product(a_row, b_col) for a_row in self.data for b_col in other.columns])
        else:
            print(self.OP_ERROR)
            return Matrix()

    def transpose(self):
        """Return a transposed version of the Matrix."""
        return Matrix(self.col_n, self.row_n, [num for col in self.columns for num in col])

    def side_transpose(self):
        """Return a side diagonal transposed version of the Matrix."""
        return Matrix(self.col_n, self.row_n, [num for col in self.columns[::-1] for num in col[::-1]])

    def v_transpose(self):
        """Return a vertically transposed version of the Matrix."""
        return Matrix(self.row_n, self.col_n, [num for row in self.data for num in row[::-1]])

    def h_transpose(self):
        """Return a horizontally transposed version of the Matrix."""
        return Matrix(self.row_n, self.col_n, [num for row in self.data[::-1] for num in row])
    
    def det(self):
        """Return the determinant of self, calculated across the first row. If not possible to calculate, return None."""
        if self.row_n != self.col_n:
            print("No determinant defined for non-square matrices.")
            return None
        if self.row_n == 1:
            return self.data[0][0]
        if self.row_n == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        return sum(num * self.cofactor(1, j) for j, num in enumerate(self.data[0], 1))

    def inverse(self):
        """Return the inverse matrix of self as a Matrix. If not inversible, return an empty Matrix."""
        if not self.det():
            print("This matrix doesn't have an inverse.")
            return Matrix()
        return self.cofactor_matrix().transpose() * (1 / self.det())
    
    def cofactor_matrix(self):
        """Return the cofactor matrix of self as a Matrix."""
        return Matrix(self.row_n, self.col_n, [self.cofactor(i, j) for i in range(1, self.row_n + 1) for j in range(1, self.col_n + 1)])
    
    def cofactor(self, i, j):
        """Return the i, j cofactor of self."""
        return (-1) ** (i + j) * self.minor(i, j)

    def minor(self, i, j):
        """Return the i, j minor of self."""
        return self.submatrix(i, j).det()

    def submatrix(self, i, j):
        """Return a Matrix identical to self with row i and column j removed."""
        return Matrix(self.row_n - 1, self.col_n - 1, [num for n, row in enumerate(self.data, 1) if n != i for m, num in enumerate(row, 1) if m != j])

    @staticmethod
    def dot_product(v1, v2):
        """Return the dot product between vectors v1 and v2."""
        return sum(num1 * num2 for num1, num2 in zip(v1, v2))

def display_menu():
    print("1. Add matrices",
          "2. Multiply matrix by a constant",
          "3. Multiply matrices",
          "4. Transpose matrix",
          "5. Calculate a determinant",
          "6. Inverse matrix",
          "0. Exit", sep="\n")

def display_diagonals():
    print("1. Main diagonal",
          "2. Side diagonal",
          "3. Vertical line",
          "4. Horizontal line", sep="\n")

def display_result(m):
    print("The result is: ", m, sep="\n")

def request_matrix(ordinal="\b"):
    """Requests rows and columns from input, then builds data based on rows provided as separate lines of input. Displays a message based on ordinal provided."""
    n, m = map(int, input(f"Enter size of {ordinal} matrix: ").split())
    data = []
    print(f"Enter {ordinal} matrix: ")
    for _ in range(n):
        data += [float(num) if "." in num else int(num) for num in input().split()]
    return Matrix(n, m, data)

while True:
    display_menu()
    choice = int(input("Your choice: "))
    if choice == 0:
        break
    elif choice == 1:
        a, b = request_matrix("first"), request_matrix("second")
        result = a + b
    elif choice == 2:
        a = request_matrix()
        b = int(input("Enter constant: "))
        result = a * b
    elif choice == 3:
        a, b = request_matrix("first"), request_matrix("second")
        result = a * b
    elif choice == 4:
        display_diagonals()
        diagonal_choice = int(input("Your choice: "))
        if diagonal_choice == 1:
            result = request_matrix().transpose()
        elif diagonal_choice == 2:
            result = request_matrix().side_transpose()
        elif diagonal_choice == 3:
            result = request_matrix().v_transpose()
        elif diagonal_choice == 4:
            result = request_matrix().h_transpose()
    elif choice == 5:
        result = request_matrix().det()
    elif choice == 6:
        result = request_matrix().inverse()
    display_result(result)