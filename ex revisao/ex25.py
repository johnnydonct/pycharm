# dar o tamanho da lista para depois encher ela
n = int(input("Insira o tamanho da sua primeira lista: "))
l1 = []
for i in range (n):
    l1.append(int(input("Insira os elementos da lista 1: ")))
print("a lista 1 é:", l1)
# dar o tamanho da segunda lista para depois encher ela
m = int(input("Insira o tamanho da sua primeira lista: "))
l2 = []
for i in range (m):
    l2.append(int(input("Insira os elementos da lista 1: ")))
print("A lista 2 é:", l2)
# l3= l1+l2 é a concatenação das listas, como se fosse a união
l3 = l1 + l2
list.sort(l3) #essa função deixa a lista em forma crescente 
dl3 = l3[::-1] #essa função inverte a ordem dos elementos da lista, e juntando com a função anterior, deixa a lista decrescente
print(f"A lista 3 crescente é {l3}")
print(f"A lista 3 decrescente é {dl3}")

