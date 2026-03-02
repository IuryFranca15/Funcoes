

#conversor de metros em cm

def conversor(metro): # a função só precisa passar o metro
    cm = metro * 100 #conversao
    return f"isso em cm é {cm} cm" #retorna o valor

metro = int(input("informe um numero em metros: "))
resultado_cm = conversor(metro) #cria uma variavel pra funcao
print(resultado_cm) #printa a variavel