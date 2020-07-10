class Matrix:
    OP_ERROR = "The operation cannot be performed."

    def __init__(self, n=0, m=0, data=None):
        self.row_n = n
        self.col_n = m
        self.data = [data[m*i:m*(i+1)] for i in range(n)]  # Probably should add self.rows = self.data
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

    @staticmethod
    def dot_product(v1, v2):
        """Return the dot product between vectors v1 and v2."""
        return sum(num1 * num2 for num1, num2 in zip(v1, v2))

def display_menu():
    print("1. Add matrices",
          "2. Multiply matrix by a constant",
          "3. Multiply matrices",
          "0. Exit", sep="\n")

def display_result_matrix(m):
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
    display_result_matrix(result)
    print()