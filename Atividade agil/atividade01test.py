import pytest
from atividade01 import gerar_valores_aleatorios


def test_gerar_valores_aleatorios_tamanho():
  valores = gerar_valores_aleatorios()
  assert len(valores) == 20000


def test_gerar_valores_aleatorios_faixa():
  valores = gerar_valores_aleatorios()
  for valor in valores:
    assert -999999 <= valor <= 999999
