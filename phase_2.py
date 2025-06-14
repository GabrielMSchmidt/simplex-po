def verify_b_n(Bi, Ni, l, all_idx):

  idx = [i for i in range(len(A[0]))]
  random.shuffle(idx)

  Bi = idx[:l]
  Ni = idx[l:]

  for idx in all_idx:
    if idx == sorted(Ni):
      print(f"Ni: {Ni} are in all_idx: {all_idx}. Alterando...")
      Bi, Ni = verify_b_n(Bi, Ni, l, all_idx)
      break
  return Bi, Ni


def matrix_b_n(A, l, all_idx):       # Verificar det de B
  B, Bi, N, Ni = [], [], [], []

  Bi, Ni = verify_b_n(Bi, Ni, l, all_idx)
  all_idx.append(sorted(Ni))

  print(f"Bi: {Bi}")
  print(f"Ni: {Ni}")
  print(f"all_idx: {all_idx}")


  for i in range(len(A)):
    aux_b = []
    aux_n = []
    for j in range(len(A[0])):
      if j in Bi:
        aux_b.append(A[i][j])
      else:
        aux_n.append(A[i][j])

    B.append(aux_b)
    N.append(aux_n)

  print(f"B: {B}")
  print(f"N: {N}")
  return B, N, Bi, Ni, all_idx


def passo_1(B, b):
  B_1 = inverse_matrix(B)
  xb_aprox = multiply_matrix(B_1, b)
  print(f"xb_aprox: {xb_aprox}")

  xn_aprox = 0
  return xb_aprox, xn_aprox


def passo_2(c, Bi, B, Ni, N):
  B_1 = inverse_matrix(B)
  print(f"B_1: {B_1}")
  cbt = []
  cnt = []
  cnt_aprox = []
  k = -1
  print(f"N: {N}")
  Nt = augment_matrix(N)
  print(f"Nt: {Nt}")

  for i in range(len(c)):
    if i in Bi:
      cbt.append(c[i])
    else:
      cnt.append(c[i])

  print(f"cbt: {cbt}")
  print(f"cnt: {cnt}")
  vms = multiply_matrix([cbt], B_1)
  print(f"vms: {vms}")

  for i in range(len(Ni)):
    aux = cnt[i] - multiply_matrix(vms[0], Nt[i])[0][0]
    print(f"aux: {aux}")
    cnt_aprox.append(aux)
    if cnt_aprox[i] < 0:
      if (i > 0 and cnt_aprox[i] < cnt_aprox[k]) or (i == 0):
        k = i

  print(f"cnt_aprox: {cnt_aprox}")
  print(f"k: {k}")

  return k


def passo_3(k:int):
  if k == -1:
    return True
  else:
    return False

def passo_4(B, N, k):
  print(f"N: {N}")
  N = transpose_matrix(N)
  print(f"Nt: {N}")
  B = inverse_matrix(B)
  y = multiply_matrix(B, N[k])
  print(f"y: {y}")
  return y


def passo_5(xb_aprox, y):
  e_aprox = []
  aux = 0
  for i in range(len(xb_aprox)):
    if y[i][0] > 0:
      e_aprox.append(xb_aprox[i][0] / y[i][0])
    else:
      e_aprox.append(999)


  menor = 999
  for i in range(len(e_aprox)):
    if y[i][0] > 0 and e_aprox[i] <= menor:
      index_e = i

  print(f"e_aprox: {e_aprox} / index_e: {index_e}")
  return e_aprox, index_e


def passo_6(A, N, Ni, B, Bi, index_k, index_e):
  Ni = Ni[index_k]
  Bi = Bi[index_e]

  N_t = transpose_matrix(N)
  B_t = transpose_matrix(B)
  A_t = transpose_matrix(A)

  N_t[index_k] = A_t[Ni]
  B_t[index_e] = A_t[Bi]

  N = transpose_matrix(N_t)
  B = transpose_matrix(B_t)

  return N, B


def fase_2(A, b, c, l):
  cont = 1
  all_idx = []
  while cont < 6:
    print(f"Iteração: {cont}")
    B, N, Bi, Ni, all_idx = matrix_b_n(A, l, all_idx)
    while calculate_determinant(B) == 0:
      print(f"Determinante da matriz Básica == {calculate_determinant(B)}. Alterando...")
      B, N, Bi, Ni, all_idx = matrix_b_n(A, l, all_idx)
    print(f"Determinante de B: {calculate_determinant(B)}")

    xb_aprox, xn_aprox = passo_1(B, b)
    k = passo_2(c, Bi, B, Ni, N)
    if passo_3(k):
      break
    y = passo_4(B, N, k)
    e_aprox, index_e = passo_5(xb_aprox, y)
    N, B = passo_6(A, N, Ni, B, Bi, k, index_e)
    cont += 1

  print(f"Bi: {Bi}")
  print(f"xb_aprox: {xb_aprox}")
  print(f"c: {c}")
  z = 0
  for i, val in enumerate(Bi):
    print(f"idx[c]: {val} / val_c: {c[val]}")
    print(f"idx[xb_aprox]: {i} / val_xb_aprox: {xb_aprox[i][0]}")
    z+= xb_aprox[i][0] * c[val]

  print(f"z: {z}")
  return z