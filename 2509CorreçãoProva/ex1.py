n = int(input("Entre com um número inteiro positivo: "))
soma = 0
for i in range (1, n+1):
    soma+=(n-i+1)/i
print(soma)
#Correto