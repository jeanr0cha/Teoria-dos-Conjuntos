
import os

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
    
