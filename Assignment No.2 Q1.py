def main():
    # Take matrices
    A = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    B = [
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2]   
    ]

    # Check if matrix is singular
    def is_singular(matrix):
        determinant = (matrix[0][0] * matrix[1][1] * matrix[2][2] +
                       matrix[0][1] * matrix[1][2] * matrix[2][0] +
                       matrix[0][2] * matrix[1][0] * matrix[2][1] -
                       matrix[0][2] * matrix[1][1] * matrix[2][0] -
                       matrix[0][1] * matrix[1][0] * matrix[2][2] -
                       matrix[0][0] * matrix[1][2] * matrix[2][1])
        return determinant == 0

    print("Matrix A is singular:", is_singular(A))
    print("Matrix B is singular:", is_singular(B))


if __name__ == "__main__":
    main()