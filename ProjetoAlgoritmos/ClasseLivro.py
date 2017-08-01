import random
import string
class Livro:
    idd = 0 # VARIAVEL ESTATICA QUE FUNCIONA COMO CONTADORA DE OBJETOS DA CLASSE
            # SE FOREM CRIADOS OBJETOS DA CLASSE LIVRO, ESSA VARIAVEL VAI SER > 0
    def __init__(self,titulo="",autor="",cod_de_barras=""):
        self.__titulo = titulo
        self.__autor = autor
        Livro.idd +=1
        self.__codLivro = cod_de_barras

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getId(self):
        return Livro.idd

    def getCodBarras(self):
        return self.__codLivro

    def setTitulo(self,titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setCodLivro(self,cod):
        self.__codLivro = cod

    def __repr__(self):
        return self.__titulo.title()+" - "+self.__autor.title()+" : "+self.__codLivro

def geradorCodigo(): #FUNÇÃO QUE GERA CODIGOS UNICOS QUE PODEM SER USADOS COMO CODIGOS DO LIVRO (NÃO É COD. DE BARRAS)
    code = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for i in range(12))
    return code

livros = []
novolivro = Livro()
novolivro.setAutor("howard fast")
novolivro.setTitulo("Spartacus")
novolivro.setCodLivro(geradorCodigo())
livros.append(novolivro)
novolivro2 = Livro("Ahuela","Julio Cortazar",geradorCodigo())
livros.append(novolivro2)
print(livros)