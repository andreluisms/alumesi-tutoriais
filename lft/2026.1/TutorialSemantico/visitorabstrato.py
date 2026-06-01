# visitorabstrato.py

from abc import ABC, abstractmethod


class VisitorAbstrato(ABC):

    @abstractmethod
    def visit(self, no):
        pass

    # ==========================================================
    # PROGRAMA
    # ==========================================================

    @abstractmethod
    def visitProgramaListaComandos(self, programa):
        pass


    # ==========================================================
    # LISTA DE COMANDOS
    # ==========================================================

    @abstractmethod
    def visitListaDeComandosComando(self, lista_comandos):
        pass

    @abstractmethod
    def visitListaDeComandosLista(self, lista_comandos):
        pass


    # ==========================================================
    # COMANDOS
    # ==========================================================

    @abstractmethod
    def visitComandoDeclaracao(self, comando):
        pass

    @abstractmethod
    def visitComandoAtribuicao(self, comando):
        pass

    @abstractmethod
    def visitComandoIf(self, comando):
        pass

    @abstractmethod
    def visitComandoWhile(self, comando):
        pass

    @abstractmethod
    def visitComandoPrint(self, comando):
        pass

    @abstractmethod
    def visitComandoVazio(self, comando):
        pass


    # ==========================================================
    # EXPRESSÕES
    # ==========================================================

    @abstractmethod
    def visitExpressaoSoma(self, expressao):
        pass

    @abstractmethod
    def visitExpressaoSubtracao(self, expressao):
        pass

    @abstractmethod
    def visitExpressaoMultiplicacao(self, expressao):
        pass

    @abstractmethod
    def visitExpressaoDivisao(self, expressao):
        pass

    @abstractmethod
    def visitExpressaoIdentificador(self, expressao):
        pass

    @abstractmethod
    def visitExpressaoNumero(self, expressao):
        pass

    @abstractmethod
    def visitExpressaoLambda(self, expressao):
        pass

    @abstractmethod
    def visitExpressaoChamadaFuncao(self, expressao):
        pass


    # ==========================================================
    # LAMBDA
    # ==========================================================

    @abstractmethod
    def visitLambdaComParametros(self, lambda_expr):
        pass

    @abstractmethod
    def visitLambdaSemParametros(self, lambda_expr):
        pass


    # ==========================================================
    # PARAMLIST
    # ==========================================================

    @abstractmethod
    def visitParamListUnico(self, paramlist):
        pass

    @abstractmethod
    def visitParamListLista(self, paramlist):
        pass


    # ==========================================================
    # CHAMADA DE FUNÇÃO
    # ==========================================================

    @abstractmethod
    def visitChamadaDeFuncaoConcreta(self, chamada):
        pass


    # ==========================================================
    # LISTA DE ARGUMENTOS
    # ==========================================================

    @abstractmethod
    def visitListaArgumentosUnico(self, argumentos):
        pass

    @abstractmethod
    def visitListaArgumentosLista(self, argumentos):
        pass

    @abstractmethod
    def visitListaArgumentosVazia(self, argumentos):
        pass