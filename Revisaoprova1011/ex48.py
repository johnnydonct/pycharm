l = int(input("Entre com o numero de linhas: "))
c = int(input("Entre com o numero de colunas: "))
A = []
for i in range(l):
    en = []
    for j in range(c):
        en.append(int(input("Entre com o elemento da matriz: ")))
A.append(en)
def verificar_matriz(A):
    if not A:
        return (0, 0)

    num_linhas = len(A)
    num_colunas_esperado = len(A[0])

    if all(len(linha) == num_colunas_esperado for linha in A):
        return (num_linhas, num_colunas_esperado)
    else:
        return ()
verificar_matriz(A)