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
        pass


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
        pass


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
        pass

class AtribuicaoVariavel(Comando):
    def __init__(self, ID, expressao):
        self.ID = ID
        self.expressao = expressao
    def print(self):
        pass


#Expressao
