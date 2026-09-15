def perfil(**dados):
    for chave, valor in dados.items():
        print(chave, ":", valor)
perfil(nome="Ana", idade=25)