#Exercício 40
l = int(input("Entre com o numero de linhas: "))
c = int(input("Entre com o numero de colunas: "))
A = []
for i in range(l):
    en = []
    for j in range(c):
        en.append(int(input("Entre com o elemento da matriz: ")))
A.append(en)

h = A
def mid(A):
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if i == j and A[i][j] !=1:
                return False
            if i!=j and A[i][j]!=0:
                return False
    return True
print("A matriz é matriz identidade?", mid(A))