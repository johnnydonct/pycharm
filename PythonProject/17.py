p1tamanho= int(input("Número de provas p1: "))
p2tamanho= int(input("Número de provas p2: "))
p1= []
p2= []
for p1n in range(p1tamanho):
    p1.append(float(input("Nota da p1: ")))
print(p1)
for p2n in range(p2tamanho):
    p2.append(float(input("Nota da p2: ")))
print(p2)
for i in p1:
