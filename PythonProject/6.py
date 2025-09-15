a = int(input("Insira um ano: "))
if a%400==0 or a%4==0 and a%100!=0:
    print(f"{a} é um ano bissexto")
else:
    print(f"{a} não é um ano bissexto")
