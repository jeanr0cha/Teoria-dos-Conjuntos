import os

# def calcula_intersecao(A, B):
    
#     os.system('cls')
#     print(" A = ", A)
#     print(" B = ", B)
#     print("\nOperação de Interseção entre conjuntos\n")
#     print("A interseção de dois conjuntos A e B é o conjunto formado por todos os elementos que pertencem" \
#     " ao conjunto A quanto a B.")

#     intersecao = A.intersection(B)
#     print(f"A ∩ B = {intersecao}")


def calcula_intersecao(A, B): 
   
    os.system('cls')
    print(" A = ", A)
    print(" B = ", B)
    print("\nOperação de Interseção entre conjuntos\n")
    print("A interseção de dois conjuntos A e B é o conjunto formado por todos os elementos que pertencem" \
    " ao conjunto A quanto a B.")
    
    intersecao_AB = []

    for item in A:
        if item in B and item not in intersecao_AB:
            intersecao_AB.append(item)

    print(f"A ∩ B = {intersecao_AB}\n")
    return intersecao_AB