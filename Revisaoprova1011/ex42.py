#Incompleto, está dando errado

def transpor_matriz(A):
    if not A:
        return []
    num_linhas = len(A)
    num_colunas = len(A[0])
    A_T = []
    for j in range(num_colunas):
        nova_linha = []
        for i in range(num_linhas):
            nova_linha.append(A[i][j])
        A_T.append(nova_linha)
    return A_T


# --- Exemplo de Uso ---

# Matriz 3x2 (3 linhas, 2 colunas)
l = int(input("Entre com o numero de linhas: "))
c = int(input("Entre com o numero de colunas: "))
A = []
for i in range(l):
    en = []
    for j in range(c):
        en.append(int(input("Entre com o elemento da matriz: ")))
A.append(en)

print(transpor_matriz(A))

