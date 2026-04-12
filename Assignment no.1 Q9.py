def add_matrices(A, B):
    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result


# Input matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [1, 2, 3]
]

# Addition
sum_matrix = add_matrices(A, B)

print("Addition of matrices:")
for row in sum_matrix:
    print(row)
def multiply_matrices(A, B):
    
    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)

    return result


# Input matrices
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Multiplication
product_matrix = multiply_matrices(A, B)

print("Multiplication of matrices:")
for row in product_matrix:
    print(row)
