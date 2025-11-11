def lemtz():
    M=[]
    while True:
        temp = input().split()
        if temp == []:
            return M
        linha = []
        for i in temp:
            linha.append(int(i))
        M.append(linha)

M = lemtz()

def dim(M):
    linhas = len(M)
    colunas = len(M[0])
    for i in range (1, linhas):
        if len(M[i]) != colunas:
            return()
    print(linhas, colunas)
dim(M)
