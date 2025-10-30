l = int(input("Entre com o numero de linhas: "))
c = int(input("Entre com o numero de colunas: "))
A = []
for i in range(l):
    en = []
    for j in range(c):
        en.append(int(input("Entre com o elemento da matriz: ")))
def contarzero():
    z = 0
    for linha in A:
        for i in linha:
            if i == 0:
                z += 1
    return(z)
if l == c:
    nc = int(input("Insira o elemento a ser contado: "))
    q = contarzero(A, nc)
    print(f"O número {nc} aparece {q} vezes")
else:
    print("Sua matriz precisa ser quadrada")