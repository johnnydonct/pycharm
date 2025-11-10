def contagem(x, y):
    palavras = x
    quant = palavras.count(y)
    posicao = []

    for i in range(len(palavras)):
        if palavras[i] == y:
            posicao.append(i)
    print(posicao)

frase = str(input("Digite um texto: ")).lower().strip()
caractere = str(input("Digite uma palavra: ")).lower()
contagem(frase, caractere)