
def calcular_imc(peso, altura):
    valor_imc = (peso/altura **2)
    return valor_imc

def classificar_imc(valor_imc):
    if valor_imc < 18.5:
        return "Abaixo do peso"
    elif valor_imc >= 18.5 and valor_imc <= 24.9:
        return "Peso normal"
    else:
        return "Sobrepeso"

valor_imc = calcular_imc(70, 1.63)
classificacao = classificar_imc(valor_imc)
print(f"imc é {round(valor_imc)} e classficicacao é {classificacao}")