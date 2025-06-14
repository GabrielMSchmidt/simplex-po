def simplex():
  max, l, c, var = initVar()
  A, b, c = initMatrix(l, c, var)
  if pre_fase_1(max, A, b, c):
    fase_1(A, b, c, l)
  else:
    z = fase_2(A, b, c, l)


def fase_1(max, A, b, c):
  pass


def pre_fase_1(max, A, b, c):
  if max:
    max = False
    c = [x * -1 for x in c]

  for i, n in enumerate(b):
    if n < 0:
      b[i] = n*(-1)
      A[i] = [x * -1 for x in A[i]]
      match sig_ig[i]:
        case '>':
          sig_ig[i] = '<'
        case '<':
          sig_ig[i] = '>'
        case '≥':
          sig_ig[i] = '≤'
        case '≤':
          sig_ig[i] = '≥'

  if (sig_ig.find(">") or sig_ig.find("≥") or sig_ig.find("=")) != -1:
    return True
  else:
    return False


  print(f"Sinais: {sig_ig}")
  print(f"A: {A}")
  print(f"b: {b}")
  print(f"c: {c}")



max = True
A = [[-1, 1, -1, 0, 0], [1, -1, 0, 1, 0], [-1, 1, 0, 0, 1]]
b = [-6, 4, 4]
c = [-1, -2, 0, 0, 0]
l = 3
sig_ig = ["≥", "≥", "≤"]

pre_fase_1(max, A, b, c, l)