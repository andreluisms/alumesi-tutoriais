# sintaxeabstrata.py

from abc import ABC, abstractmethod


# ==========================================================
# CLASSES ABSTRATAS
# ==========================================================

class Programa(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class ListaDeComandos(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Comando(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Expressao(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Lambda(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class ParamList(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class ChamadaDeFuncao(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class ListaArgumentos(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


# ==========================================================
# PROGRAMA
# ==========================================================

class ProgramaListaComandos(Programa):

    def __init__(self, lista_comandos):
        self.lista_comandos = lista_comandos

    def accept(self, visitor):
        return visitor.visitProgramaListaComandos(self)


# ==========================================================
# LISTA DE COMANDOS
# ==========================================================

class ListaDeComandosComando(ListaDeComandos):

    def __init__(self, comando):
        self.comando = comando

    def accept(self, visitor):
        return visitor.visitListaDeComandosComando(self)


class ListaDeComandosLista(ListaDeComandos):

    def __init__(self, lista_comandos, comando):
        self.lista_comandos = lista_comandos
        self.comando = comando

    def accept(self, visitor):
        return visitor.visitListaDeComandosLista(self)


# ==========================================================
# COMANDOS
# ==========================================================

class ComandoDeclaracao(Comando):

    def __init__(self, identificador, expressao):
        self.identificador = identificador
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitComandoDeclaracao(self)


class ComandoAtribuicao(Comando):

    def __init__(self, identificador, expressao):
        self.identificador = identificador
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitComandoAtribuicao(self)


class ComandoIf(Comando):

    def __init__(self, condicao, comandos_then, comandos_else):
        self.condicao = condicao
        self.comandos_then = comandos_then
        self.comandos_else = comandos_else

    def accept(self, visitor):
        return visitor.visitComandoIf(self)


class ComandoWhile(Comando):

    def __init__(self, condicao, comandos):
        self.condicao = condicao
        self.comandos = comandos

    def accept(self, visitor):
        return visitor.visitComandoWhile(self)


class ComandoPrint(Comando):

    def __init__(self, expressao):
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitComandoPrint(self)


class ComandoVazio(Comando):

    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitComandoVazio(self)


# ==========================================================
# EXPRESSÕES
# ==========================================================

class ExpressaoSoma(Expressao):

    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoSoma(self)


class ExpressaoSubtracao(Expressao):

    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoSubtracao(self)


class ExpressaoMultiplicacao(Expressao):

    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoMultiplicacao(self)


class ExpressaoDivisao(Expressao):

    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoDivisao(self)


class ExpressaoIdentificador(Expressao):

    def __init__(self, nome):
        self.nome = nome

    def accept(self, visitor):
        return visitor.visitExpressaoIdentificador(self)


class ExpressaoNumero(Expressao):

    def __init__(self, valor):
        self.valor = valor

    def accept(self, visitor):
        return visitor.visitExpressaoNumero(self)


class ExpressaoLambda(Expressao):

    def __init__(self, lambda_expr):
        self.lambda_expr = lambda_expr

    def accept(self, visitor):
        return visitor.visitExpressaoLambda(self)


class ExpressaoChamadaFuncao(Expressao):

    def __init__(self, chamada):
        self.chamada = chamada

    def accept(self, visitor):
        return visitor.visitExpressaoChamadaFuncao(self)


# ==========================================================
# LAMBDA
# ==========================================================

class LambdaComParametros(Lambda):

    def __init__(self, parametros, expressao):
        self.parametros = parametros
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitLambdaComParametros(self)


class LambdaSemParametros(Lambda):

    def __init__(self, expressao):
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitLambdaSemParametros(self)


# ==========================================================
# PARAMLIST
# ==========================================================

class ParamListUnico(ParamList):

    def __init__(self, identificador):
        self.identificador = identificador

    def accept(self, visitor):
        return visitor.visitParamListUnico(self)


class ParamListLista(ParamList):

    def __init__(self, paramlist, identificador):
        self.paramlist = paramlist
        self.identificador = identificador

    def accept(self, visitor):
        return visitor.visitParamListLista(self)


# ==========================================================
# CHAMADA DE FUNÇÃO
# ==========================================================

class ChamadaDeFuncaoConcreta(ChamadaDeFuncao):

    def __init__(self, identificador, argumentos):
        self.identificador = identificador
        self.argumentos = argumentos

    def accept(self, visitor):
        return visitor.visitChamadaDeFuncaoConcreta(self)


# ==========================================================
# LISTA DE ARGUMENTOS
# ==========================================================

class ListaArgumentosUnico(ListaArgumentos):

    def __init__(self, expressao):
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitListaArgumentosUnico(self)


class ListaArgumentosLista(ListaArgumentos):

    def __init__(self, lista_argumentos, expressao):
        self.lista_argumentos = lista_argumentos
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitListaArgumentosLista(self)


class ListaArgumentosVazia(ListaArgumentos):

    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitListaArgumentosVazia(self)