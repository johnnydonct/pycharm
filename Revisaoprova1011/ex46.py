def cvtmp(s):
    #calcular horas restantes
    horas = s //3600
    #calcular minutos restantes
    minutos = (s%3600)//60
    #segundos restantes
    segundos = s%60
    print(f"O valor desses segundos em horas é {horas:02d}:{minutos:02d}:{segundos:02d}")
s = int(input("Digite a quantidade de segundos: "))
cvtmp(s)