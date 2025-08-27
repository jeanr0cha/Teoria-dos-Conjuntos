#Função para realizar operações de união entre conjuntos
import os

# def calcula_uniao(A, B):
#     print("\nOperação de União entre conjuntos\n")
#     print("A união de dois conjuntos A e B é o conjunto formado por todos os elementos que pertencem a A ou a B (ou a ambos).")
#     print("A ∪ B = { x | x ∈ A ou x ∈ B }\n\n")
    
#     print(f"Conjunto A: {A}\n")
#     print(f"Conjunto B: {B}\n")
    
#     uniao = A.union(B)
    
#     print(f"A ∪ B = {uniao}\n")

# os.system('cls')

def calcula_uniao(A, B):

    os.system('cls')
    print("\nOperação de União entre conjuntos\n")
    print("A ∪ B = { x | x ∈ A ou x ∈ B }\n\n")

    print(f"Conjunto A: {A}\n")
    print(f"Conjunto B: {B}\n")

    uniao_AB = []

    for item in A:
        if item not in uniao_AB:
            uniao_AB.append(item) 
    
    for item in B:
        if item not in uniao_AB:
            uniao_AB.append(item)

    print(f"A ∪ B = {uniao_AB}\n")
    return uniao_AB

os.system('cls')
    
