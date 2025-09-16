# dar o tamanho da lista para depois encher ela
n = int(input("Insira o tamanho da sua lista: "))
lista=[]
# agora o usuário vai preencher a lista
for i in range(n):
    lista.append(int(input("Insira um número inteiro: ")))
print(lista)
total = 0
# adicione o elemento atual (valor) ao total acumulado (total)
for i in lista:
    total = total + i
print(f"A soma dos elementos da lista é {total}")