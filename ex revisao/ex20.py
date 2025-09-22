n = int(input("Insira um número inteiro positivo: "))
soma = 0
for i in range(1, n+1):
    i = i 
    soma = i/(1+n-i)+ soma #+1 pra não zerar o denominador
print(soma)
