
def calcular_imc(peso, altura):
    valor_imc = (peso/altura **2) #define valor_imc
    return valor_imc #retorna valor_imc

def classificar_imc(valor_imc):
    if valor_imc < 18.5:
        return "Abaixo do peso"
    elif valor_imc >= 18.5 and valor_imc <= 24.9:
        return "Peso normal"
    else:
        return "Sobrepeso"

valor_imc = calcular_imc(70, 1.63) #atribui a valor_imc a funcao de calcular_imc
classificacao = classificar_imc(valor_imc) #atribui a classificacao a funcao de calcular imc, passando de argumento valor_imc
print(f"imc é {round(valor_imc)} e classficicacao é {classificacao}")