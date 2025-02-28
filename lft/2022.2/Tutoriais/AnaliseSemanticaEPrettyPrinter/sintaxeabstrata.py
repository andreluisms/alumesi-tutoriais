from abc import abstractmethod
from abc import ABC

# Gramática
# programa : listadecomandos
# listadecomandos : comando
#                | listadecomandos comando
# comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA
#         | ID ATRIBUICAO expressao PONTOEVIRGULA
#         | IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
#         | WHILE expressao DO listadecomandos ENDWHILE
# expressao : expressao MAIS expressao
#                  | expressao MENOS expressao
#                  | expressao VEZES expressao
#                  | expressao DIVIDE expressao
#                  | ID
#                  | NUMERO


#Programa
class Programa():
    def __init__(self, listadecomandos):
        self.listadecomandos = listadecomandos
    @abstractmethod
    def print(self):
        print('[Programa]', end='')
        self.listadecomandos.print()


#Listadecomandos
class Listadecomandos(ABC):
    @abstractmethod
    def print(self):
        pass

class UmComando(Listadecomandos):
    def __init__(self, comando):
        self.comando = comando
    def print(self):
        print('[UmComando]', end='')
        self.comando.print()

class MaisdeUmComando(Listadecomandos):
    def __init__(self, listadecomandos, comando):
        self.comando = comando
        self.listadecomandos = listadecomandos
    def print(self):
        print('[MaisdeUmComando]', end='')
        self.comando.print()
        self.listadecomandos.print()


#Comando
class Comando(ABC):
    @abstractmethod
    def print(self):
        pass

class DeclaracaoVariavel(Comando):
    def __init__(self, ID, expressao):
        self.ID = ID
        self.expressao = expressao
    def print(self):
        print('[DeclaracaoVariavel]', end='')
        print(self.ID)
        self.expressao.print()

class AtribuicaoVariavel(Comando):
    def __init__(self, ID, expressao):
        self.ID = ID
        self.expressao = expressao
    def print(self):
        print('[AtribuicaoVariavel]', end='')
        print(self.ID)
        self.expressao.print()

class ComandoIF(Comando):
    def __init__(self, expressao, listadecomandosif, listadecomandoselse):
        self.expressao = expressao
        self.listadecomandosif=listadecomandosif
        self.listadecomandoselse=listadecomandoselse
    def print(self):
        print('[ComandoIF]', end='')
        self.expressao.print()
        self.listadecomandosif.print()
        self.listadecomandoselse.print()


class ComandoWhile(Comando):
    def __init__(self, expressao, listadecomandos):
        self.expressao = expressao
        self.listadecomandos = listadecomandos
    def print(self):
        print('[ComandoWhile]', end='')
        self.expressao.print()
        self.listadecomandos.print()

#Expressao

class Expressao(ABC):
    @abstractmethod
    def print(self):
        pass

class ExpressaoSoma(Expressao):
    def __init__(self, expesq, expdir):
        self.expesq = expesq
        self.expdir = expdir
    def print(self):
        print('[ExpressaoSoma]', end='')
        self.expesq.print()
        self.expdir.print()

class ExpressaoSubtracao(Expressao):
    def __init__(self, expesq, expdir):
        self.expesq = expesq
        self.expdir = expdir
    def print(self):
        print('[ExpressaoSubtracao]', end='')
        self.expesq.print()
        self.expdir.print()

class ExpressaoMul(Expressao):
    def __init__(self, expesq, expdir):
        self.expesq = expesq
        self.expdir = expdir
    def print(self):
        print('[ExpressaoMul]', end='')
        self.expesq.print()
        self.expdir.print()

class ExpressaoDiv(Expressao):
    def __init__(self, expesq, expdir):
        self.expesq = expesq
        self.expdir = expdir
    def print(self):
        print('[ExpressaoDiv]', end='')
        self.expesq.print()
        self.expdir.print()

class ExpressaoNumero(Expressao):
    def __init__(self, numero):
        self.numero = numero
    def print(self):
        print('[ExpressaoNumero]', end='')
        print(self.numero)


class ExpressaoID(Expressao):
    def __init__(self, id):
        self.id = id
    def print(self):
        print('[ExpressaoID]', end='')
        print(self.id)