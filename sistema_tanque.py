"""Esse módulo tem as classes que representam o problema do tanque.
"""
class Torneira:
    """Essa classe representa uma torneira do mundo real, tendo com atributos a vazão e um nome para identificar ela.
    """
    def __init__(self, vazao: float, nome: str):
        """Cria uma tornei com nome e vazão

        Args:
            vazao (float): Representa a vazão da torneira em l/s.
            nome (str): Nome da torneira, deve ser único no sistema.
        """
        self.vazao = vazao
        self.nome = nome

    def modificar_vazao(self, nova_vazao:float):
        self.vazao = nova_vazao
        self.nova_vazao = nova_vazao
        print(f'A vazão foi atualizada para {self.nova_vazao} l/s')


class Tanque:
    """Classe que representa um tanque do mundo real, ele tem como atributos: capacidade_max, capacidade_atual, historico, torneiras_saida e torneiras_entrada.
    """

    def __init__(self, capacidade_maxima: float, capacidade: float):
        """Cria uma instância de um objeto da classe Tanque.

        Args:
            capacidade (float): Capacidade atual do tanque.
            capacidade_maxima (float) Capacidade máxima do tanque.
        """
        self.capacidade_max = capacidade_maxima
        self.capacidade_atual = capacidade
        self.historioco = []
        self.torneiras_saida = []
        self.torneiras_entrada = []

    def instalar_torneira(self, nova_torneira: Torneira, saida=True)->bool:
        """Adiciona uma torneira ao tanque.

            Adiciona uma torneira ao Tanque, ela pode ser de saida ou entrada.
        Args:
            nova_torneira (Torneira): Nova torneira a ser adicionada.
            saida (bool, optional): Indica se a torneita será de entrada ou saída, por padrão e de saida.

        Returns:
            bool: True se a torneira tiver sido instalada com sucesso!
        """
        if saida:
            for torneira in self.torneiras_saida:
                if nova_torneira.nome == torneira.nome:
                    print("Torneira já instalada!")
                    return False
            self.torneiras_saida.append(nova_torneira)
            print('Nova torneira adicionada com sucesso!')
        else:
            for torneira in self.torneiras_entrada:
                if nova_torneira.nome == torneira.nome:
                    print("Torneira já instalada!")
                    return False
            self.torneiras_entrada.append(nova_torneira)
            print('Nova torneira instalada com sucesso!')
        return True

    def abrir_torneira(self, nome_torneira, tempo_segundos):
        for torneira in self.torneiras_saida:
            if torneira.nome == torneira.nome:
                if self.capacidade_atual >= torneira.vazao*tempo_segundos:
                    self.capacidade_atual -= torneira.vazao*tempo_segundos
                    print("Água retirada do reservatório :)")
                    return True
                else:
                    self.capacidade_atual = 0
                    print("A água acabou antes do tempo :(")
                    return True
        for torneira in self.torneiras_entrada:
            if torneira.nome == torneira.nome:
                if self.capacidade_atual + torneira.vazao*tempo_segundos <= self.capacidade_max:
                    self.capacidade_atual += torneira.vazao*tempo_segundos
                    print("Água adicionada ao reservatório :)")
                    return True
                else:
                    self.capacidade_atual = self.capacidade_max
                    print("A água acabou transbordando, você desperdiçou água!")
                    return True
        return False

    def imprimir_nome_torneiras(self, nome: Torneira, vazao:Torneira):
        print(f'O nome da torneira é {nome} e sua vazão é {vazao} l/s' )

    def recargar_reservatorio(self, recarga):
        if self.capacidade_atual + recarga <= self.capacidade_max:
            self.capacidade_atual += recarga
            print('Tanque recarregado com sucesso')
        else:
            print("A recarga não pode ser concluída")
            
    def remover_torneira(self, nome_torneira: str):
        self.historico = nome_torneira
        if nome_torneira is None:
          return False
        else:
          self.historico.remove(nome_torneira)
          return True

    def calcular_tempo_esvaziamento(self, vazao):
        soma_vazao = 0
        for i in self.torneiras_saida:
            soma_vazao += i.vazao
            esvaziamento = self.capacidade_atual / soma_vazao
            print(esvaziamento)
            return True

    def atualizar_torneira(self, procurar_torneira, nova_vazao: Torneira):
        try: 
            for i in self.torneiras_saida:
                if i == procurar_torneira:
                    self.vazao = nova_vazao
                    print("vazão atualizada com sucesso")
                    return True
            for i in self.torneiras_entrada:
                if i == procurar_torneira:
                    self.vazao = nova_vazao
                    print("vazão atualizada com sucesso")
                    return True
        except:
            print("torneira não encontrada")
            return False