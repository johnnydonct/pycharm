
def transpor_matriz(A):
    if not A:
        return []
    num_linhas = len(A)
    num_colunas = len(A[0])
    AT = []
    for j in range(num_colunas):
        nova_linha = []
        for i in range(num_linhas):
            nova_linha.append(A[i][j])
        AT.append(nova_linha)
    return AT

l = int(input("Entre com o numero de linhas: "))
c = int(input("Entre com o numero de colunas: "))
A = []
for i in range(l):
    en = []
    for j in range(c):
        en.append(int(input("Entre com o elemento da matriz: ")))
    A.append(en)

AT= transpor_matriz(A)
print(f"A matriz original: {A}")
print(f"A matriz transposta de A: {AT}")
