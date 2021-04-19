"""
informações que eu preciso do seriado:
+nome : string
+número de temporadas: int
+descrição:string
+já assisti:boolean
dicionario{"nome":, "num_temp":,"descricao":,"situacao":}
seriados_cadastrados
"""
seriados_cadastrados = []

print("O que você deseja fazer:")
print("1 - Adicionar seriado")
print("2 - Consultar lista")
print("3 - Remover")
print("4 - Alterar")
print("5 - Sair")
operacao = input("Digite a opção:")
while operacao != "5":
    if operacao == "1":
        nome = input("Qual nome do seriado?")
        num_temp = int(input("Qual número de temporadas?"))
        descricao = input("Descricao:")
        situacao = input("Você já assistiu?(s/n)")
        if situacao == "s":
            situacao = True
        else:
            situacao = False
        filme = {"nome":nome,    
                 "num_temp":num_temp,"descricao":descricao,"situacao":situacao}
        seriados_cadastrados.append(filme)
    elif operacao == "2":
        nome = input("Qual nome do seriado que você deseja procurar?")
        for seriado in seriados_cadastrados:
            if seriado["nome"] == nome:
                print("Nome:", seriado["nome"])
                print("Número temporadas:", seriado["num_temp"])
                print("Descrição:", seriado["descricao"])
                if seriado["situacao"]:
                    print("Situacao: Assistido")
                else:
                    print("Situacao: Não assistido")
    elif operacao == "3":
        nome = input("Digite o nome do seriado a ser excluido:")
        for seriado in seriados_cadastrados:
            if seriado["nome"] == nome:
                seriados_cadastrados.remove(seriado)
    elif operacao == "4":
        nome = input("Digite o nome do seriado a ser alterado:")
        seriado_a_alterar = None
        for seriado in seriados_cadastrados:
            if seriado["nome"] == nome:
                seriado_a_alterar = seriado
                break
        else:
            print("Seriado não encontrado!")
        novo_nome = input("Qual nome do seriado?")
        novo_num_temp = int(input("Qual número de temporadas?"))
        nova_descricao = input("Descricao:")
        nova_situacao = input("Você já assistiu?(s/n)")
        if nova_situacao == "s":
            nova_situacao = True
        else:
            nova_situacao = False
        seriado_a_alterar["nome"] = novo_nome
        seriado_a_alterar["num_temp"] = novo_num_temp
        seriado_a_alterar["descricao"] = nova_descricao
        seriado_a_alterar["situacao"] = nova_situacao
    else:
        print("Opção inválida!")
    print("O que você deseja fazer:")
    print("1 - Adicionar seriado")
    print("2 - Consultar lista")
    print("3 - Remover")
    print("4 - Alterar")
    print("5 - Sair")
    operacao = input("Digite a opção:")