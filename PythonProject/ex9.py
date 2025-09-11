n = int(input("Insira um número inteiro positivo: "))
for i in range(1,n+1):
    if n%i==0:
        print(f"Os divisores de {n} são:", i)
        