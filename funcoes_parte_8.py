
#criar uma função chamada filtrar_caras que ajude a identificar quais peças estão acima do orçamento.

precos_pecas = [120.50, 450.00, 89.90, 210.00, 35.00]


def filtrar_caras(precos_pecas, limite = 100):
    caras = []
    for preco in precos_pecas:
        if preco > limite:
            caras.append(preco)
    return caras

caras = filtrar_caras(precos_pecas)
for cara in caras:
    print(f"peça de R$: {cara} supera o orçamento")  