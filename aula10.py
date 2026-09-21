# def saudar(nome):
#     return 'ola, ' + nome + '!'
# print(saudar('Ana'))

# msg = saudar('edilson')
# print(msg.upper())



# def media(a, b, casas=2):
#     m = (a + b)/ 2
#     return round(m, casas)

# print(media(8,6))
# #7.0

# print(media(8, 5, 1))
# #6.5



# def total(*precos, desc=0):
#     s = sum(precos)
#     return s * (1 - desc / 100)

# print(total(10, 25.5, 7))
# #42.5

# print(total(10, 25.5, 7, desc=10))
# #38.25



# def reg(nota, boletim=None):
#     """nao altera a lista original"""
#     if boletim is None:
#         boletim = []
#     novo = boletim[:]     #copia
#     novo.append(nota)
#     return novo
# notas = [7]
# print(reg(9, notas))     #[7,9]
# print(notas)             #[7]



import calculadora as c

def orc(qtd, preco, frete=0):

    s = c.multiplicar(qtd, preco)
    return c.somar(s, frete)

print(orc(3, 49.9, 15))