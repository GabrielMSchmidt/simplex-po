def initVar() -> int:
  c, l = 0, 0
  sig_ig = []
  max = False

  arquivo = open("input.txt", "r")
  linha = arquivo.readline()

  if linha.find("max") != -1:
    print("achei o max")
    max = True
  else:
    print("achei o min")

  if max:
    var = linha.count('x') - 1
  else:
    var = linha.count('x')

  print(f"Variaveis: {var}")
  linha = arquivo.readline()

  while linha != "":
    l += 1

    if linha.find(" = ") != -1:
      sig_ig.append("=")
    else:
      c += 1
      if linha.find(">") != -1:
        sig_ig.append(">")
      elif linha.find("≥") != -1:
        sig_ig.append("≥")
      elif linha.find("<") != -1:
        sig_ig.append("<")
      elif linha.find("≤") != -1:
        sig_ig.append("≤")

    linha = arquivo.readline()

  print(f"Sinais: {sig_ig}")
  print(f"Linhas: {l}\nVariaveis de folga: {c}")
  c += var
  arquivo.close()
  return max, l, c, var


def initMatrix(l: int, c: int, var: int) -> list[list[int]]:
  lin, signal, aux, var_ind = 0, 1, 0, 0

  A = [[0.0 for _ in range(c)] for _ in range(l)]
  print(f"Matriz A = Linhas: {len(A)} / Colunas: {len(A[0])}")

  b = [0.0 for _ in range(l)]
  print(f"Vetor b = Posições: {len(b)}")

  c = [0.0 for _ in range(c)]
  print(f"Vetor c = Posições: {len(c)}")

  arquivo = open("input.txt", "r")
  linha = arquivo.readline()

  for i, char in enumerate(linha):
    match char:
      case '-':
        signal = -1
      case '+':
        signal = 1
      case 'x':
        if linha[i-1] == 'a':
          continue
        elif linha[i-1] != ' ' and linha[i-1].isdigit():
          num_str = ""
          pointer = 1
          while True:
            if linha[i-pointer].isdigit() or linha[i-pointer] == '.':
              num_str += linha[i-pointer]
              pointer += 1
            else:
              break

          num_str = num_str[::-1]
          print(f"num_str[c]: {float(num_str) * signal}")
          c[int(linha[i+1])-1] = float(num_str) * signal
        else:
          print(f"num_str[c]: {1.0 * signal}")
          c[int(linha[i+1])-1] = 1.0*signal

  linha = arquivo.readline()
  while linha != "":
    signal = 1
    for i, char in enumerate(linha):
      match char:
        case '-':
          signal = -1
        case '+':
          signal = 1
        case 'x':
          if i != 0 and linha[i-1].isdigit():
            num_str = ""
            pointer = 1
            while True:
              print(f"num_str: {num_str} / index: {i-pointer}")
              if (linha[i-pointer].isdigit() or linha[i-pointer] == '.') and (i-pointer >= 0):
                num_str += linha[i-pointer]
                pointer += 1
              else:
                break

            num_str = num_str[::-1]
            print(f"num_str[A]: {float(num_str) * signal}")
            A[lin][int(linha[i+1])-1] = (float(num_str) * signal)
          else:
            print(f"num_str[A]: {1.0 * signal}")
            A[lin][int(linha[i+1])-1] = 1.0*signal
        case '>':
          A[lin][var+aux] = -1.0
          aux += 1
        case '≥':
          A[lin][var+aux] = -1.0
          aux += 1
        case '<':
          A[lin][var+aux] = 1.0
          aux += 1
        case '≤':
          A[lin][var+aux] = 1.0
          aux += 1

      if char == '=' or char == '≤' or char == '≥':
        num_str = ""
        signal = 1
        for j in range(i + 1, len(linha)):
          if linha[j].isdigit() or linha[j] == '.':
            num_str += linha[j]
          elif linha[j] == ' ':
            continue
          elif linha[j] == '-':
            signal = -1
          else:
              break
        print(f"sinal: {signal}")
        print(f"num_str[b]: {float(num_str) * signal}")
        b[var_ind] = float(num_str) * signal
        var_ind += 1

    lin += 1
    linha = arquivo.readline()

  print(f"Matriz A: {A}")
  print(f"Vetor b: {b}")
  print(f"Vetor c: {c}")

  return A, b, c