#  Projeto Proposto pelo Professor Lucas Teixeiras Alves

## 📝 Descrição

Este projeto, desenvolvido em Python, que permite ao usuário realizar diversas operações de teoria dos conjuntos. O usuário pode inserir os elementos de dois conjuntos (A e B) e escolher uma operação a ser executada a partir de um menu.

## ✨ Funcionalidades

O programa suporta as seguintes operações:

* **União:** Retorna todos os elementos que pertencem a A ou a B.
* **Interseção:** Retorna os elementos que pertencem a A e a B.
* **Diferença:** Calcula A - B ou B - A.
* **Subconjunto:** Verifica se A é subconjunto de B e vice-versa.
* **Igualdade/Desigualdade:** Verifica se os dois conjuntos possuem os mesmos elementos.
* **Produto Cartesiano:** Gera todos os pares ordenados (a, b).
* **Relações Binárias:** Permite ao usuário definir uma relação como um subconjunto do produto cartesiano.
* **Verificação de Pertinência:** Verifica se um par ordenado pertence a uma relação previamente definida.

## 🚀 Como Usar

### Pré-requisitos

* Python 3.x

### Clone do Repositório

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd SEU-REPOSITORIO
    ```
3.  Execute o script principal:
    ```bash
    python program.py
    ```

### Caso Deseje gerar o executavel 

É possível gerar um arquivo executável que não requer a instalação do Python para rodar, é importante ativar o ambiente virtual .venv.

1.  Instale o PyInstaller:
    ```bash
    pip install pyinstaller
    ```
2.  Execute o comando na pasta raiz do projeto:
    ```bash
    pyinstaller --onefile --name TeoriaDosConjuntos program.py
    ```
3.  O arquivo `TeoriaDosConjuntos.exe` estará na pasta `dist/`.

---
*Desenvolvido em Agosto de 2025.*