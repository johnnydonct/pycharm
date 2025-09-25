n = int(input("Entre com um número inteiro positivo: ")) #Exercício incompleto com raciocínio errado
ndivisores = 0
for i in range (1, n+1):
    if n%i==0:
        ndivisores +=
        print (ndivisores)
#Correção
#n = int(input("Entre com um número inteiro positivo: "))
#p = []
#if n>=1:
    #p.append(2)
#i=3
#while len(p) <n:
    #Éprimo = True
    #for primo in p:
        #if i % primo==0:
        #Éprimo = False
        #break
    #if Éprimo:
        #p.append(i)
    #i+=1
#if n == 1:
    #print("O primeiro número primo é 2")
#else:
    #print(f"{str(p).strip('[]').replace(', ', '+')} = {sum(p)}")