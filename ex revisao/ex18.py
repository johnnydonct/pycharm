n = int(input("Insira um número inteiro positivo: "))
soma = 0
# 1 e n+1 para ele ler do 1 até o número n e repetir n vezes
for i in range (1,n+1):
    soma = (2*(i**2))+(3*(i**3))+(4*(i**4))+soma
#     ou soma += (2*(i**2))+(3*(i**3))+(4*(i**4)) 
#     += serve para somar a próxima soma à soma feita anteriormente, assim como em 
#     "soma = algo + soma"
print(soma)
#111177 para 10, só pra ver se da certo
