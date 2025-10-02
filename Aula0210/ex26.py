n = input("Informe uma sequência de números separados por espaço: ")
l = [int(i) for i in n.split()]
s = sum(l)
k = len(l)
media = s/k
print("A média da lista l é:", format(media, ".2f"))