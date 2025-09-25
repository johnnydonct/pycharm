n = int(input("Entre com um número inteiro positivo, ele será o tamanho da sua lista: "))
l = []
for i in range (1, n+1):
    l.append(int(input("Entre com um número inteiro positivo maior que 1: ")))
print("Sua lista é:", l)
for i in range(1, n+2):
    if i%2==0:
        l.remove(i)
print("A lista sem os pares é:", l)
#Correto