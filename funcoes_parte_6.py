
#converter de real para dolar

def converter (real):
    dolar = real/5.27
    return dolar #retornar a variavel pura porque se retornar f string da erro no print

real = float(input("informe um valor em real: \n"))
resultado = converter(real)
print(f"O valor em dólar é: ${resultado:.2f}")