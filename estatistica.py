import statistics

def media(lista):
    """Calcula a média aritmética dos valores."""
    if not lista:
        return 0
    return statistics.mean(lista)

def mediana(lista):
    """Calcula a mediana (valor central) dos valores."""
    if not lista:
        return 0
    return statistics.median(lista)

def moda(lista):
    """Calcula a moda (valor mais frequente) dos valores."""
    if not lista:
        return None
    try:
        return statistics.mode(lista)
    except statistics.StatisticsError:
        # Tratamento caso haja múltiplos valores com a mesma frequência máxima
        return "Sem moda única"