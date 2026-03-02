


def verificar_seguranca(senha):
    #aqui verifico se tem numero na senha
    tem_numero = False
    for x in senha:
        if x.isdigit():
            tem_numero = True
    
    #agora se nao tiver numero, retorno uma mensagem
    if not tem_numero:
        return "senha deve ter pelo menos um numero!"
    
    if len(senha) < 8:
        return "senha curta demais!"
    else:
        return "senha segura!"

print("===== Verificador de senha segura =====")
senha = input("informe a senha: ")
verificador = verificar_seguranca(senha)
print(verificador)