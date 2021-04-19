class Sistema():     
    def __init__(self, arq= str, titulo = str, autor= str, estado= str, emprestimo= str,  assunto= str, livros_cadastrados= str):
        self.arq = arq
        self.titulo = titulo
        self.autor = autor
        self.estado = estado
        self.emprestimo = emprestimo
        self.assunto = assunto
        self.livros_cadastrados = [] 

    def buscar_livro(self, titulo= str):
        for livro in self.livros_cadastrados:
                if livro["titulo"] == titulo:
                    return livro
        return None
    
    def cadastrar_livro(self, titulo= str, autor= str, emprestimo= str, estado= str, assunto= str):
            if self.encontrar_string(titulo) is False:
                livro = {"titulo":titulo,
                        "autor": autor,
                        "emprestimo": emprestimo,
                        "estado": estado,
                        "assunto": assunto} 
                self.livros_cadastrados.append(livro)
                print('Livro cadastrado com sucesso!')
                print(self.livros_cadastrados)
                return True
            else:
                print('Livro já cadastrado!')
                return False

    def excluir_livro(self, l_num, arq= str, titulo= str):
        arq.pop(l_num)
        return arq

    def salvar_arq(self, arq= str):
        arquivo = open(arq, "a")
        letra = str(self.livros_cadastrados) + '\n'
        arquivo.write(letra)
        arquivo.close()
        return arquivo

    def buscar_autor(self, l_num, arq= str, autor= str):
        arquivo = open(arq, 'r')

        print(arquivo.readlines()[l_num])

        arquivo.close

    def encontrar_string(self, arq= str, titulo= str):
        with open(arq) as f:
            for l_num, l in enumerate(f, 1): # percorrer linhas e enumera-las a partir de 1
                if titulo in l: # ver se palavra esta na linha
                    print(l_num)
                    return l_num
            else: # caso não haja break
                print('autor não encontrado')

class Menu():
    def __init__(self):
        self.sistema = Sistema()

    def imprimir_commandos(self):
        print("1 - Cadastrar Livro")
        print("*3 - Remover Livro")
        print("*4 - Atualizar informação de livro")
        print("*5 - Buscar livros por autor")
        print("6 - Sair")

    def main(self):
        self.imprimir_commandos()
        opcao = int(input("Digite uma opção acima: "))
        while opcao != 6:
            if opcao == 1:
                arq = input('digite o nome do arquivo: ')
                titulo = input("titulo: ")
                autor = input("autor: ")
                emprestimo = input("emprestimo: ")
                estado = input("estado: ")
                assunto = input("assunto: ")
                self.sistema.cadastrar_livro(titulo, autor, emprestimo, estado, assunto)
                self.sistema.salvar_arq(arq)
                break

            elif opcao == 3:
                arq = input('digite o nome do arquivo que o livro se encontra: ')
                titulo = input("titulo: ")
                self.sistema.encontrar_string(arq, titulo)
                self.sistema.buscar_autor(arq, titulo)
            
            elif opcao == 5:
                autor = input("autor: ")
                self.sistema.buscar_autor(autor)

            self.imprimir_commandos()
            opcao = int(input("Digite uma opção acima: "))


if __name__ == "__main__":
    g = Menu()
    g.main()