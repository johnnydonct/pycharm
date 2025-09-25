x = int(input("Entre com um número inteiro positivo: "))
y = int(input("Entre com um número inteiro positivo: "))
z = int(input("Entre com um número inteiro positivo: "))
if (x+y<=z) or (x+z<=y) or (y+z<=x):
    if x==y==z:
        print("Este é possível e é um triângulo é equilátero")
    elif x==y!=z or x!=y==z or x==z!=y:
        print("Este triângulo é possível e é isóceles")
    else:
        print("Este triângulo é possível e é escaleno")
elif x+y>z or y+z>x or x+z>y:
    print("Este triângulo não existe")
#O AND é necessário para que todas as condições sejam consideradas
#Correção
#x = int(input("Entre com um número inteiro positivo: "))
#y = int(input("Entre com um número inteiro positivo: "))
#z = int(input("Entre com um número inteiro positivo: "))
#if (x+y<z) AND (x+z<y) AND (y+z<x):
    #if x==y==z:
        #print("Este é possível e é um triângulo é equilátero")
   # elif x==y!=z or x!=y==z or x==z!=y:
        #print("Este triângulo é possível e é isóceles")
    #else:
        #print("Este triângulo é possível e é escaleno")
#else:
    #print("Este triângulo não existe")