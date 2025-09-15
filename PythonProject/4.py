print("Digite um número: ")
a = int (input ())
if a % 2 == 0 and a < 100:
    print ("O número é par e menor do que 100")
else :
    if a% 2 == 0 and a >= 100:
        print ("O número é par e maior ou igual que 100")
if a % 2 != 0 and a < 100:
    print ("O número é ímpar e menor do que 100")
else:
    if a % 2 !=0 and a > 100:
        print ("0 número é impar e maior ou igual que 100")