import os

def calcula_diferenca_A_B(A, B):

    os.system('cls')
    print(" A = ", A)
    print(" B = ", B)
    print("\nOperação de Diferença entre conjuntos\n")
    print("A diferença entre dois conjuntos A e B é o conjunto formado por todos os elementos" \
    " que pertencem ao conjunto A mas não pertencem ao conjunto B.")
    
    diferenca_AB = []

    for item in A:
        
        if item not in B and item not in diferenca_AB:
            diferenca_AB.append(item)

    print(f"(A - B) = {diferenca_AB}\n")
    
    return diferenca_AB


def calcula_diferenca_B_A(B, A):

    os.system('cls')
    print(" B = ", B)
    print(" A = ", A)
    print("\nOperação de Diferença entre conjuntos\n")
    print("A diferença entre dois conjuntos A e B é o conjunto formado por todos os elementos" \
    " que pertencem ao conjunto B mas não pertencem ao conjunto A.")
    
    diferenca_BA = []

    for item in B:
        
        if item not in A and item not in diferenca_BA:
            diferenca_BA.append(item)

    print(f"(A - B) = {diferenca_BA}\n")
    
    return diferenca_BA