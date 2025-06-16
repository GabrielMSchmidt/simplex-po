def pre_phase_1(max_min, A, b, c, sig_ig):
  if max_min:
    max_min = False
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

  if (">" or "≥" or "=") in sig_ig:
    return True
  else:
    return False


def phase_1(max, A, b, c):
  pass


if __name__ == '__main__':
  A = [[-1, 1, -1, 0, 0], [1, -1, 0, 1, 0], [-1, 1, 0, 0, 1]]
  b = [-6, 4, 4]
  c = [-1, -2, 0, 0, 0]
  l = 3
  sig_ig = ["≥", "≥", "≤"]
  max_min = True

  pre_phase_1(max_min, A, b, c, sig_ig)

  print(f"Sinais: {sig_ig}")
  print(f"A: {A}")
  print(f"b: {b}")
  print(f"c: {c}")

