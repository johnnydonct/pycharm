l = int(input("Entre com o numero de linhas: "))
c = int(input("Entre com o numero de colunas: "))
A = []
for i in range(l):
    en = []
    for j in range(c):
        en.append(int(input("Entre com o elemento da matriz: ")))
A.append(en)
def quadrada():
    if l == c:
        print("A matriz 'A' é quadrada")
    else:
        print("A matriz 'A' não é quadrada")
quadrada()