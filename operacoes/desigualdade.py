import os

def calcula_desigualdade(A, B):
    
    os.system('cls')
    print(" A = ", A)
    print(" B = ", B)
    print("\nOperação de Desigualdade entre conjuntos\n")
    print("Dois conjuntos A e B são desiguais se, e somente se, existe pelo menos um elemento em A" \
    " que não pertence a B ou existe pelo menos um elemento em B que não pertence a A.")

    if A != B:
        print("A é desigual a B (A ≠ B)")
    else:
        print("A é igual a B (A = B)")