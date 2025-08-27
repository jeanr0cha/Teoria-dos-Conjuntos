import os

# def calcula_pares_ordenados(A, B):
#     os.system('cls')
#     print(" A = ", A)
#     print(" B = ", B)
#     print("\nOperação de Produto Cartesiano entre conjuntos\n")
#     print("O produto cartesiano de dois conjuntos A e B, denotado por A × B, é o conjunto de todos os pares ordenados (a, b) onde a ∈ A e b ∈ B.\n")
    
#     produto_cartesiano = {(a, b) for a in A for b in B}
    
#     print("O produto cartesiano A × B é:")
#     print(produto_cartesiano)
#     print()

def calcula_produto_cartesiano(A,B):
    os.system('cls')
    print(" A = ", A)
    print(" B = ", B)
    print("\nOperação de Produto Cartesiano entre conjuntos\n")
    print("O produto cartesiano de dois conjuntos A × B, exemplo onde Sejam A= {1,2} e B = {x, y} Então: A x B = {(1,x), (1,y), (2,x), (2,y)}")

    # produto_a = A.split(',')
    # produto_b = B.split(',')
    produto_cartesiano_A_B = []

    for a in A:

        for b in B:
            
            par_ordenado_A_B = (a, b)
            
            produto_cartesiano_A_B.append(par_ordenado_A_B)

    print(f"O produto cartesiano A × B = {produto_cartesiano_A_B}")

    return produto_cartesiano_A_B






