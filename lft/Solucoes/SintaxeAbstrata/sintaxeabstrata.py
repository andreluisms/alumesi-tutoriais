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
    def print(self):
        print("[Programa]", end='')
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
    def __init__(self, comando, listadecomandos):
        self.comando = comando
        self.listadecomandos = listadecomandos
    def print(self):
        print("[MaisdeUmComando]", end='')
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
        print("[DeclaracaoVariavel]", end='')
        print(self.ID)
        self.expressao.print()

class AtribuicaoVariavel(Comando):
    def __init__(self, ID, expressao):
        self.ID = ID
        self.expressao = expressao
    def print(self):
        print("[AtribuicaoVariavel]", end='')
        print(self.ID)
        self.expressao.print()



class Ifcmd(Comando):
    def __init__(self, expressao, lstcmd1, lstcmd2):
        self.expressao = expressao
        self.lstcmd1 = lstcmd1
        self.lstcmd2 = lstcmd2
    def print(self):
        print("[Ifcmd]", end='')
        self.expressao.print()
        self.lstcmd1.print()
        self.lstcmd2.print()


class Whilecmd(Comando):
    def __init__(self, expressao, lstcmd):
        self.expressao = expressao
        self.lstcmd = lstcmd
    def print(self):
        print("[Whilecmd]", end='')
        self.expressao.print()
        self.lstcmd.print()


#Expressao


class Expressao(ABC):
    @abstractmethod
    def print(self):
        pass

class ExpressaoSoma(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def print(self):
        print("[ExpressaoSoma]", end='')
        self.exp1.print()
        self.exp2.print()


class ExpressaoSub(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def print(self):
        print("[ExpressaoSub]", end='')
        self.exp1.print()
        self.exp2.print()

class ExpressaoMul(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def print(self):
        print("[ExpressaoMul]", end='')
        self.exp1.print()
        self.exp2.print()

class ExpressaoDiv(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def print(self):
        print("[ExpressaoDiv]", end='')
        self.exp1.print()
        self.exp2.print()

class ExpressaoID(Expressao):
    def __init__(self, id):
        self.id = id
    def print(self):
        print("[ExpressaoID]", end='')
        print(self.id)


class ExpressaoNumero(Expressao):
    def __init__(self, numero):
        self.numero = numero
    def print(self):
        print("[ExpressaoNumero]", end='')
        print(self.numero)
