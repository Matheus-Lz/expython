import random

def gerar_valores_aleatorios():
    return [random.randint(-999999, 999999) for _ in range(20000)]

valores = gerar_valores_aleatorios()
valores_ordenados = sorted(valores)