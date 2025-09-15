n = str(input("Insira F para Farenheit ou C para Celsius: ")).upper()
temp = int(input("Agora insira a temperatura em números inteiros: "))
print(temp, n)
if n == "F":
    ctemp = 5/9*(temp-32)
    print(f"Sua temperatura em Celsius é {ctemp} Celsius")
elif n == "C":
    ftemp = (temp*(9/5))+32
    print(f"Sua temperatura em Farenheit é {ftemp} Farenheit")
else:
    print("Sua temperatura precisa estar em F ou C")