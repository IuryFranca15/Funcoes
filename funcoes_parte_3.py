

nomes = ""
def listar_convidados(*nomes):
    for i, nome in enumerate(nomes):
        print(f"Convidado(a) {i+1}: {nome}")
    print(f"qtd: {len(nomes)} convidados")

listar_convidados("Laura", "Clara")