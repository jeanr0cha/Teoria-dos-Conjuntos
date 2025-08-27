import os

def calcula_relacoes_n_areas(A, B):

    print("\n--- Relações n-áreas ---\n")
    print("Definição: Uma relação n-áreas é um subconjunto do produto cartesiano de n conjuntos.")
    print("Por exemplo, uma relação entre os conjuntos A, B e C é um subconjunto de A × B × C.")
    print("Iremos trabalhar com dois conjuntos A e B para formar pares ordenados (a, b)\n")

    # 1. Gera o produto cartesiano A x B
    relacoes_binarias_A_B = []

    for a in A:

        for b in B:
            
            relacoes_binarias_A_B.append((a, b))

    if not relacoes_binarias_A_B:
        print("Não é possível formar pares binários")
        return []
    
    print("O produto cartesiano A × B gerou os seguintes pares ordenados:")
    for i, par in enumerate(relacoes_binarias_A_B, start=1):
        print(f"{i}: {par}")

    print("\nDigite os números dos pares ordenados que deseja incluir na relação, separados por vírgula.")
    escolha = input("Separe por virgulas (ex: 1,3): ")

        # 4. Constrói a Relação com base na escolha do usuário
    relacao_r = []
    try:
        
        indices_escolhidos = [int(i.strip()) for i in escolha.split(',')]
        
        for indice in indices_escolhidos:
            
            if 1 <= indice <= len(relacoes_binarias_A_B):
                par_escolhido = relacoes_binarias_A_B[indice - 1]
                
                if par_escolhido not in relacao_r:
                    relacao_r.append(par_escolhido)
            else:
                print(f"Aviso: O número {indice} é inválido e foi ignorado.")
    
    except ValueError:
        print("\nErro: Entrada inválida. A relação não foi criada.")
        return [] 

    print("\n------------------------------------------------------------")
    print("A Relação Binária (subconjunto de A x B) definida é:")
    print("r = ", relacao_r)


