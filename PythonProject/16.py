n = int(input("Qual o tamanho da sua lista? "))
lista=[]
for i in range(n):
    lista.append(int(input("Insira um número inteiro: ")))
print("Lista atual:", lista)
for i in lista:
    if i%2==0:
        lista.remove(i)
print("Lista sem os pares", lista)