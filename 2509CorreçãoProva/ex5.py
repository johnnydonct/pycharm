ano = int(input("Entre com um ano (número inteiro positivo): "))
if ano%4==0 and ano%100!=0:
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto")
    #Correto