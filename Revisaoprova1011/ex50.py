
def tri(n):
    i = 1
    while i * (i+1) * (i+2) < n:
         i = i+1
    if i * (i+1) * (i+2) == n:
        print ("%d eh o produto %d*%d*%d" %(n,i,i+1,i+2))
    else:
        print(f"O número {n} não é triangular")

n = int(input("Insira um número inteiro a ser verificado: "))
tri(n)
