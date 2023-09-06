import random
import pytest
from atividade02 import gerar_valores_aleatorios


# Teste para verificar se a função gera 20.000 valores inteiros
def test_gerar_ordenar_numeros_tamanho():
  numeros = gerar_valores_aleatorios()
  assert len(numeros) == 20000


# Teste para verificar se todos os valores estão dentro da faixa correta
def test_gerar_ordenar_numeros_faixa():
  numeros = gerar_valores_aleatorios()
  for valor in numeros:
    assert -999999 <= valor <= 999999


# Teste para verificar se a lista está ordenada corretamente
def test_gerar_ordenar_numeros_ordenacao():
  numeros = gerar_valores_aleatorios()
  assert numeros == sorted(numeros)
