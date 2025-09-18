# primeiro passo: ler um número natural n;
n = int(input("Entre com um número natural: "))
#criar uma lista para ser preenchida
l = []
#criar um input que preencherá a lista
for i in range(n):
    l.append(int(input(f"Insira um número da sau sequência: ")))
print(l)
i=i
for i in l:
  if l[i]> l[i+1]: #isso aqui ta dando errado
      print("A sequência está crescente")
  else:
      print("A lista não está ordenada de forma crescente")
