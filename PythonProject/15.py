n = int(input("Quantos números inteiros serão lidos na lista? "))
lista = []
for i in range(n):
    lista.append(int(input("Número: ")))
print(f"Lista com {n} números", lista)
p= int(input("Insira um número a ser verificado: "))
if p in lista:
    print(f"{p} está na lista!")
else:
    print(f"{p} não está na lista!")