def sbvt(vetor):
    for i in range(len(vetor)):
        valor_atual = vetor[i]
        # Se for positivo
        if valor_atual > 0:
            vetor[i] = 1
        # Se for negativo
        elif valor_atual < 0:
            vetor[i] = 0
    print(vetor)

vetor_numeros = []
posicoes = 30
print(f"Por favor, digite {posicoes} números.")
print("-" * 30)
for i in range(posicoes):
    while True:
        entrada = input(f"Digite o {i + 1}º número: ")
        try:
            numero = float(entrada)
            vetor_numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
sbvt(vetor_numeros)