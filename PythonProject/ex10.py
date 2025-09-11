n = int(input("Insira um número inteiro positivo: "))
soma=0
for i in range(1,n+1):
    if n%i==0:
        soma = soma +1
print(f"A quantidade de divisores de {n} é:", soma)