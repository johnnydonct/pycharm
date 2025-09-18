n = int(input("Insira um número inteiro positivo: "))
soma = 0
for i in range (1, n+1):
    if n%2==0:
        s= n/2
    if n%2==1:
        s= -(n+1)/2
print(s)
