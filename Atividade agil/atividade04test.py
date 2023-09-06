import pytest
from atividade04 import BibliotecaFiccaoCientifica


def biblioteca():
  return BibliotecaFiccaoCientifica()


def test_adicionar_livro(biblioteca):
  biblioteca.adicionar_livro("Duna")
  assert "Duna" in biblioteca.listar_livros()


def test_listar_livros(biblioteca):
  biblioteca.adicionar_livro("Duna")
  biblioteca.adicionar_livro("Fundação")
  assert biblioteca.listar_livros() == ["Duna", "Fundação"]


def test_remover_livro(biblioteca):
  biblioteca.adicionar_livro("Duna")
  biblioteca.remover_livro("Duna")
  assert "Duna" not in biblioteca.listar_livros()
