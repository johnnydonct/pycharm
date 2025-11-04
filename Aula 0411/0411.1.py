x = int(input("Entre um x: "))
y = int(input("Entre um y: "))
def mdc(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x
print("O MDC é:", mdc(x, y))