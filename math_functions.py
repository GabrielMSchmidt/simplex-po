import math

def calculate_determinant(A:list[list[int]]): # Laplace Method
  det = 0
  if len(A) == 1:
    det = A[0][0]
  elif len(A) == 2:
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
  elif len(A) == 3:
    det = A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[0][2]*A[1][0]*A[2][1] - A[0][2]*A[1][1]*A[2][0] - A[0][1]*A[1][0]*A[2][2] - A[0][0]*A[1][2]*A[2][1]
  else:
    for i in range(len(A)):
      det += math.pow(-1,1+i+1)*A[0][i]*calculate_determinant(find_matrix(A, i))
  return det


def find_matrix(A:list[list[int]], l:int):
  matrix = []
  for i in range(1, len(A)):
    aux = []
    for j in range(len(A[0])):
      if j != l:
        aux.append(A[i][j])
    matrix.append(aux)
  return matrix


def augment_matrix(matrix):
  return [[elem] for elem in matrix]


def transpose_matrix(matrix):
  rows = len(matrix)
  cols = len(matrix[0])

  transposed = [[0 for _ in range(rows)] for _ in range(cols)]

  for i in range(rows):
    for j in range(cols):
      transposed[j][i] = matrix[i][j]

  return transposed


def multiply_matrix(A, B):
  if type(B[0]) != list:
    B = augment_matrix(B)
  if type(A[0]) != list:
    A = augment_matrix(A)

  print(f"A: {len(A)}x{len(A[0])}")
  print(f"B: {len(B)}x{len(B[0])}")

  if len(A[0]) != len(B):
    print(f"Erro - Matrizes não multiplicáveis / A: {len(A[0])} / B: {len(B)}")
    return None

  matrix = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
  print(f"C: {len(matrix)}x{len(matrix[0])}")

  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      aux = 0
      for u in range(len(A[0])):
        aux += A[i][u] * B[u][j]
      matrix[i][j] = aux

  return matrix


def inverse_matrix(A):
    n = len(A)
    if calculate_determinant(A) == 0:
      return -1

    identity = [[float(i == j) for j in range(n)] for i in range(n)]
    M = [A[i][:] + identity[i][:] for i in range(n)]

    for i in range(n):
      if M[i][i] == 0:
        for j in range(i+1, n):
          if M[j][i] != 0:
            M[i], M[j] = M[j], M[i]
            break
        else:
          print("A matriz é singular e não possui inversa.")
          return None

      pivot = M[i][i]
      M[i] = [x / pivot for x in M[i]]

      for j in range(n):
        if j != i:
          mult = M[j][i]
          M[j] = [M[j][k] - mult * M[i][k] for k in range(2 * n)]

    inverse = [row[n:] for row in M]
    return inverse
