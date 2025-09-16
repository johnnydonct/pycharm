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
l3 = l1 + l2
cl3 = list.sort(l3)
dl3 = l3[::-1]
print(f"A lista 3 crescente é {l3}")
print(f"A lista 3 decrescente é {dl3}")
