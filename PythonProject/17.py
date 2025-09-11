p1tamanho= int(input("Número de provas p1: "))
p1= []
for p1n in range(p1tamanho):
    p1.append(float(input("Nota da p1: ")))
print("Notas da prova 1:", p1)
p2tamanho= int(input("Número de provas p2: "))
p2= []
for p2n in range(p2tamanho):
    p2.append(float(input("Nota da p2: ")))
print("Notas da prova 2:", p2)
mediap1= sum(p1)/p1tamanho
mediap2= sum(p2)/p2tamanho
print("Media da prova 1:", mediap1)
print("Media da prova 2:", mediap2)
if mediap1 > mediap2:
    print("Essa turma se saiu melhor na p1")
else:
    print("Essa turma se saiu melhor na p2")
