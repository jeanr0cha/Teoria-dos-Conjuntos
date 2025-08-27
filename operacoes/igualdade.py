import os

def calcula_igualdade(A, B):
    
    os.system('cls')

    print(" A = ", A)
    print(" B = ", B)
    print("\nOperação de Igualdade entre conjuntos\n")
    print("Dois conjuntos A e B são iguais se, e somente se, eles possuem os mesmos elementos.")

    if A == B:
        print("A é igual a B (A == B)")
    else:
        print("A não é igual a B (A != B)")