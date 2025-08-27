import os

def calcula_produto_cartesiano(A,B):
    os.system('cls')
    print(" A = ", A)
    print(" B = ", B)
    print("\nOperação de Produto Cartesiano entre conjuntos\n")
    print("O produto cartesiano de dois conjuntos A × B, por exemplo onde Sejam A= {1,2} e B = {x, y} Então: A x B = {(1,x), (1,y), (2,x), (2,y)}")

    produto_cartesiano_A_B = []

    for a in A:

        for b in B:
            
            par_ordenado_A_B = (a, b)
            
            produto_cartesiano_A_B.append(par_ordenado_A_B)

    print(f"O produto cartesiano A × B = {produto_cartesiano_A_B}")

    return produto_cartesiano_A_B






