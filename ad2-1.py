def leituraDeMatriz():
    num_linhas_a = int(input("Digite o número de linhas da MATRIZ A: "))
    num_colunas_a = int(input("Digite o número de colunas da MATRIZ A: "))
    print("")
    num_linhas_b = int(input("Digite o número de linhas da MATRIZ B: "))
    num_colunas_b = int(input("Digite o número de colunas da MATRIZ B: "))

    # Matriz A
    matriz_a = []
    for i in range(num_linhas_a):
        linha = []
        for j in range(num_colunas_a):
            valor = int(input(f"Digite um valor para a posição ({i}, {j}) da MATRIZ A: "))
            linha.append(valor)
        matriz_a.append(linha)

    print("")

    # Matriz B
    matriz_b = []
    for i in range(num_linhas_b):
        linha = []
        for j in range(num_colunas_b):
            valor = int(input(f"Digite um valor para a posição ({i}, {j}) da MATRIZ B: "))
            linha.append(valor)
        matriz_b.append(linha)

    return matriz_a, matriz_b


def mostraMatriz(nome_matriz, matriz):
    print(f"\n{nome_matriz}:")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]:^5}", end="")
        print()


def multiplicaMatrizes(matriz_a, matriz_b):
    if len(matriz_a[0]) != len(matriz_b):
        print("Inexistente!!!")
    else:
        resultado_multiplicacao = [[0 for _ in range(len(matriz_b[0]))] for _ in range(len(matriz_a))]

        # Multiplicação das matrizes
        for i in range(len(matriz_a)):
            for j in range(len(matriz_b[0])):
                for k in range(len(matriz_b)):
                    resultado_multiplicacao[i][j] += matriz_a[i][k] * matriz_b[k][j]

        print("\nMatriz Multiplicação de A por B:")
        for i in range(len(resultado_multiplicacao)):
            for j in range(len(resultado_multiplicacao[0])):
                print(f"{resultado_multiplicacao[i][j]:^5}",end="")
            print()


def somaMatrizes(matriz_a, matriz_b):
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        print("\nInexistente!!!")
    else:
        resultado_soma = []

        for i in range(len(matriz_a)):
            linha_soma = []
            for j in range(len(matriz_a[0])):
                valor_soma = matriz_a[i][j] + matriz_b[i][j]
                linha_soma.append(valor_soma)
            resultado_soma.append(linha_soma)

        print("\nMatriz soma de A com B:")
        for i in range(len(resultado_soma)):
            for j in range(len(resultado_soma[0])):
                print(f"{resultado_soma[i][j]:^5}",end=" ")
            print()

# Principal
valoresA, valoresB = leituraDeMatriz()
mostraMatriz("Matriz A", valoresA)
mostraMatriz("Matriz B", valoresB)
somaMatrizes(valoresA, valoresB)
multiplicaMatrizes(valoresA, valoresB)
