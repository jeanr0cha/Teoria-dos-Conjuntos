import os
from operacoes.uniao import calcula_uniao
from operacoes.interseccao import calcula_intersecao
from operacoes.diferenca import calcula_diferenca_A_B, calcula_diferenca_B_A
from operacoes.igualdade import calcula_igualdade
from operacoes.subconjunto import calcula_subconjunto_A_B, calcula_subconjunto_B_A
from operacoes.desigualdade import calcula_desigualdade
from operacoes.pares_produto_cartesiano import calcula_produto_cartesiano
from operacoes.relacoes_binarias import calcula_relacoes_binarias
from operacoes.relacoes_n_areas import calcula_relacoes_n_areas

def converte_entrada_em_conjunto_a_b(entrada):
    elementos = [elem.strip() for elem in entrada.split(',')]
    conjunto = [] 
    for elem in elementos:     # neste trecho convertemos valores vazio em 'λ' 
        if elem == ' ':         # se for vazio, espaço no caso, converte para 'λ'
            conjunto.add('λ')
        else:
            try:
                valor_elemento = int(elem)
            except ValueError:
                try:
                    valor_elemento = float(elem)
                except ValueError:
                    valor_elemento = elem
           
        if valor_elemento not in conjunto:
            conjunto.append(valor_elemento)

    return conjunto

while True:
    os.system('cls')
    print ("Representação dos conjuntos em Python\n\n")
    
    conjunto_a = input("Digite os valores do conjunto A separados por vírgula: ")
    conjunto_b = input("Digite os valores do conjunto B separados por vírgula: ")

    A = converte_entrada_em_conjunto_a_b(conjunto_a)
    B = converte_entrada_em_conjunto_a_b(conjunto_b)

    while True:
        os.system('cls')
        print(f"\nA = {{{', '.join(map(str, A))}}}")
        print(f"B = {{{', '.join(map(str, B))}}}\n")

        print("============================================================\n\n")
        print ("Selecione uma das opções para fazer operações de conjuntos\n"
               "============================================================\n\n"
               "1 - União A ∪ B\n" # ok
               "2 - Interseção A ∩ B\n" # ok
               "3 - Diferença A - B\n" # ok
               "4 - Verificação de igualdae A == B\n" # ok
               "5 - Subconjunto A ⊆ B\n" # ok
               "6 - Desigualdade A ≠ B\n" # ok
               "7 - Produto cartesiano A x B pares ordenados (a, b)\n" # ok
               "8 - Relações Binarias\n" #ok
               "9 - Relações n-áreas\n" #ok
               "0 - Sair\n"
               "10 - Digitar novos conjuntos\n\n")
        
        opcao = int(input("Digite a opção desejada: "))

        match opcao:
            case 1:
                calcula_uniao(A, B)
            case 2:
                calcula_intersecao(A, B)
            case 3:                
                opcao_diferenca = int(input("Escolha a operação de diferença:\n 1 - A-B\n 2 - B-A \n 3- retornar ao menu principal\n"))
                match opcao_diferenca:
                    case 1:
                        calcula_diferenca_A_B(A, B)
                    case 2:
                        calcula_diferenca_B_A(B, A)
                    case 3:
                        continue
            case 4:
                calcula_igualdade(A, B)            
            case 5:
                opcao_subconjunto = int(input("Escolha a operação de subconjunto:\n 1 - A ⊆ B\n 2 - B ⊆ A \n 3- retornar ao menu principal\n"))
                match opcao_subconjunto:
                    case 1:
                        calcula_subconjunto_A_B(A, B)
                    case 2:
                        calcula_subconjunto_B_A(B, A)
                    case 3:
                        continue
            case 6:
                calcula_desigualdade(A, B)
            case 7:
                calcula_produto_cartesiano(A, B)
            case 8:
                calcula_relacoes_binarias(A, B)
            case 9:
                calcula_relacoes_n_areas(A, B)
            case 0:
                print("Saindo...")
                exit()
            case 10:
                break  # Sai do laço interno e volta para digitar novos conjuntos

        input("\nPressione Enter para continuar...")





