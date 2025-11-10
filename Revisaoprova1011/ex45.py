x = int(input("Entre um x: "))
y = int(input("Entre um y: "))
def mdc(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x
def mmc(x, y):
    m = (x*y)/mdc(x, y)
    return m
print("o mmc é:", mmc(x, y))