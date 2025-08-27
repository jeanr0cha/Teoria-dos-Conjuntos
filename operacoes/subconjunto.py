import os

def calcula_subconjunto_A_B(A, B):
    
    os.system('cls')
    print(" A = ", A)
    print(" B = ", B)
    print("\nOperação de Subconjunto entre conjuntos\n")
    print("Um conjunto A é subconjunto de um conjunto B se, e somente se, todos os elementos de A" \
    " também pertencem a B.")
    

    # Dizemos que A é subconjunto conjunto de B
    e_subconjunto = True

    for item in A:

        if item not in B:
           e_subconjunto = False
           break
        

    if e_subconjunto:
        print("A é subconjunto de B (A ⊆ B)")
    else:
        print("A não é subconjunto de B (A ⊈ B)")


def calcula_subconjunto_B_A(B, A):
    
    os.system('cls')
    print(" B = ", B)
    print(" A = ", A)
    print("\nOperação de Subconjunto entre conjuntos\n")
    print("Um conjunto B é subconjunto de um conjunto A se, e somente se, todos os elementos de B" \
    " também pertencem a A.")
    

    # Dizemos que B é subconjunto conjunto de A
    e_subconjunto = True

    for item in B:

        if item not in A:
           e_subconjunto = False
           break
        

    if e_subconjunto:
        print("B é subconjunto de A (A ⊆ B)")
    else:
        print("B não é subconjunto de A (A ⊈ B)")

# def calcula_subconjunto_B_A(B, A):
    
#     os.system('cls')
#     print(" A = ", A)
#     print(" B = ", B)
#     print("\nOperação de Subconjunto entre conjuntos\n")
#     print("Um conjunto B é subconjunto de um conjunto A se, e somente se, todos os elementos de B" \
#     " também pertencem a A.")
#     print("B ⊆ A se todo x ∈ B implica que x ∈ A\n\n")

#     if B.issubset(A):
#         print("B é subconjunto de A (B ⊆ A)")
#     else:
#         print("B não é subconjunto de A (B ⊈ A)")