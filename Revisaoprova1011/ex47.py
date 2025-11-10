sx = str(input("Insira seu sexo em F ou M:")).upper()
h = float(input("Inira sua altura em mentros (EX: 1.64): "))
p = float(input("Insira seu peso atual: "))
if sx == "F":
    pi = 62.1*h-44.7
    if p<pi:
        print(f"Seu peso ideal é {pi:.2f}, você está abaixo do peso.")
    elif p>pi:
        print(f"Seu peso ideal é {pi:.2f}, você está acima do peso.")
    elif p == pi:
        print(f"Seu peso ideal é {pi:.2f}, você está dentro do peso.")
if sx == "M":
    pi = 72.7*h-58
    if p<pi:
        print(f"Seu peso ideal é {pi:.2f}, você está abaixo do peso.")
    elif p>pi:
        print(f"Seu peso ideal é {pi:.2f}, você está acima do peso.")
    elif p == pi:
        print(f"Seu peso ideal é {pi:.2f}, você está dentro do peso.")
