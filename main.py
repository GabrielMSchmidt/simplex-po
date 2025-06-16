import basic_functions as bf
import phase_1 as p1
import phase_2 as p2

def simplex(txt):
    A, b, c, l, max_min = bf.init_matrix(txt)
    z = p2.phase_2(A, b, c, l)

def main():
    simplex("input.txt")

if __name__ == "__main__":
    main()