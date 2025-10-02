texto = str(input("Escreva algo aqui: "))
pont = ". , : ; ! ? ( )"
for i in pont:
    texto = texto.replace(i, " ")
t = texto.split()
print(len(t))