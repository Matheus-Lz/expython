class BibliotecaFiccaoCientifica:

  def __init__(self):
    self.livros = []

  def adicionar_livro(self, titulo):
    self.livros.append(titulo)

  def listar_livros(self):
    return self.livros

  def remover_livro(self, titulo):
    if titulo in self.livros:
      self.livros.remove(titulo)
