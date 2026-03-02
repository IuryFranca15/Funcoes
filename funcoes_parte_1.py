

def calcular_preco_final(preco_original, percentual_desconto = 10): #recebe preco_original e percentual como parametros
    desconto = (preco_original * percentual_desconto)/100 #aplica o desconto
    valor_final = preco_original - desconto #calcula o valor final
    print(valor_final)

produto1 = calcular_preco_final(100, 20) #chamando a primeira vez vez com 20%
print(f"Produto 1: R$ {produto1}")
produto2 = calcular_preco_final(50) #chamando a segunda com o valor padrão
print(f"Produto 2: R$ {produto2}")