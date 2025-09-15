a = int(input("Insira o lado a do triângulo: "))
b = int(input("Insira o lado b do triângulo: "))
c = int(input("Insira o lado c do triângulo: "))
if a==b==c:
    print("O triângulo é equilátero")
elif a!=b!=c:
    print("O triângulo é escaleno")
else:
    print("O triângulo é isóceles")
s = (a+b+c)/2
A = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"{A:.2f}")