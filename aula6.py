def total(carrinho):
    itens = carrinho[:]
    itens.append ("brinde")
    return itens

original = ["arroz", "feijao","batata"]
novo = total(original)
print(original)
print(novo)