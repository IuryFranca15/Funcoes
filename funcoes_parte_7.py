#Imagine que você está criando um site de vendas. 
#O valor do frete depende do valor da compra.

def calcula_frete(compra):
    if compra >= 150:
        frete = 0
    else:
        frete = 20
    return frete

compra = float(input("informe o valor da compra: "))
frete = calcula_frete(compra)
total = compra + frete
print(f"total R$: {total:.2f}")