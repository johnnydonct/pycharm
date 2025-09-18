n = int(input("Insira um número inteiro positivo: "))
soma = 0
#para iniciar com a soma zerada
#criar o loop de for
for i in range (1, n+1):
#se for par, a soma "s" vai ser igual a n/2, e se for ímpar, -(n+1)/2
    if n%2==0:
        s= n/2
    if n%2==1:
        s= -(n+1)/2
print(s)

