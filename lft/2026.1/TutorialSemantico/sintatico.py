# sintatico.py

import ply.yacc as yacc

from lexico import tokens

from sintaxeabstrata import *


# ==========================================================
# PRECEDÊNCIA
# ==========================================================

precedence = (
    ('left', 'MAIS', 'MENOS'),
    ('left', 'VEZES', 'DIVIDE'),
)


# ==========================================================
# PROGRAMA
# ==========================================================

def p_programa(p):
    '''
    programa : listadecomandos
    '''
    p[0] = ProgramaListaComandos(p[1])


# ==========================================================
# LISTA DE COMANDOS
# ==========================================================

def p_listadecomandos_comando(p):
    '''
    listadecomandos : comando
    '''
    p[0] = ListaDeComandosComando(p[1])


def p_listadecomandos_lista(p):
    '''
    listadecomandos : listadecomandos comando
    '''
    p[0] = ListaDeComandosLista(p[1], p[2])


# ==========================================================
# COMANDOS
# ==========================================================

def p_comando_declaracao(p):
    '''
    comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA
    '''
    p[0] = ComandoDeclaracao(
        p[2],
        p[4]
    )


def p_comando_atribuicao(p):
    '''
    comando : ID ATRIBUICAO expressao PONTOEVIRGULA
    '''
    p[0] = ComandoAtribuicao(
        p[1],
        p[3]
    )


def p_comando_if(p):
    '''
    comando : IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
    '''
    p[0] = ComandoIf(
        p[2],
        p[4],
        p[6]
    )


def p_comando_while(p):
    '''
    comando : WHILE expressao DO listadecomandos ENDWHILE
    '''
    p[0] = ComandoWhile(
        p[2],
        p[4]
    )


def p_comando_print(p):
    '''
    comando : PRINT LPAREN expressao RPAREN PONTOEVIRGULA
    '''
    p[0] = ComandoPrint(
        p[3]
    )


def p_comando_vazio(p):
    '''
    comando : PONTOEVIRGULA
    '''
    p[0] = ComandoVazio()


# ==========================================================
# EXPRESSÕES BINÁRIAS
# ==========================================================

def p_expressao_soma(p):
    '''
    expressao : expressao MAIS expressao
    '''
    p[0] = ExpressaoSoma(
        p[1],
        p[3]
    )


def p_expressao_subtracao(p):
    '''
    expressao : expressao MENOS expressao
    '''
    p[0] = ExpressaoSubtracao(
        p[1],
        p[3]
    )


def p_expressao_multiplicacao(p):
    '''
    expressao : expressao VEZES expressao
    '''
    p[0] = ExpressaoMultiplicacao(
        p[1],
        p[3]
    )


def p_expressao_divisao(p):
    '''
    expressao : expressao DIVIDE expressao
    '''
    p[0] = ExpressaoDivisao(
        p[1],
        p[3]
    )


# ==========================================================
# EXPRESSÕES ATÔMICAS
# ==========================================================

def p_expressao_parenteses(p):
    '''
    expressao : LPAREN expressao RPAREN
    '''
    p[0] = p[2]


def p_expressao_identificador(p):
    '''
    expressao : ID
    '''
    p[0] = ExpressaoIdentificador(
        p[1]
    )


def p_expressao_numero(p):
    '''
    expressao : NUMERO
    '''
    p[0] = ExpressaoNumero(
        p[1]
    )


def p_expressao_lambda(p):
    '''
    expressao : lambda
    '''
    p[0] = ExpressaoLambda(
        p[1]
    )


def p_expressao_chamada_funcao(p):
    '''
    expressao : chamadadefuncao
    '''
    p[0] = ExpressaoChamadaFuncao(
        p[1]
    )


# ==========================================================
# LAMBDA
# ==========================================================

def p_lambda_com_parametros(p):
    '''
    lambda : LAMBDA LPAREN paramlist RPAREN DO expressao END
    '''
    p[0] = LambdaComParametros(
        p[3],
        p[6]
    )


def p_lambda_sem_parametros(p):
    '''
    lambda : LAMBDA LPAREN RPAREN DO expressao END
    '''
    p[0] = LambdaSemParametros(
        p[5]
    )


# ==========================================================
# PARAMLIST
# ==========================================================

def p_paramlist_unico(p):
    '''
    paramlist : ID
    '''
    p[0] = ParamListUnico(
        p[1]
    )


def p_paramlist_lista(p):
    '''
    paramlist : paramlist VIRGULA ID
    '''
    p[0] = ParamListLista(
        p[1],
        p[3]
    )


# ==========================================================
# CHAMADA DE FUNÇÃO
# ==========================================================

def p_chamadadefuncao(p):
    '''
    chamadadefuncao : ID LPAREN listaargumentos RPAREN
    '''
    p[0] = ChamadaDeFuncaoConcreta(
        p[1],
        p[3]
    )


# ==========================================================
# LISTA DE ARGUMENTOS
# ==========================================================

def p_listaargumentos_unico(p):
    '''
    listaargumentos : expressao
    '''
    p[0] = ListaArgumentosUnico(
        p[1]
    )


def p_listaargumentos_lista(p):
    '''
    listaargumentos : listaargumentos VIRGULA expressao
    '''
    p[0] = ListaArgumentosLista(
        p[1],
        p[3]
    )


def p_listaargumentos_vazia(p):
    '''
    listaargumentos :
    '''
    p[0] = ListaArgumentosVazia()


# ==========================================================
# ERRO SINTÁTICO
# ==========================================================

def p_error(p):

    if p:
        print(
            f"Erro sintático próximo ao token "
            f"'{p.value}' (tipo={p.type}) "
            f"na linha {p.lineno}"
        )
    else:
        print("Erro sintático: fim de arquivo inesperado")


# ==========================================================
# CONSTRUÇÃO DO PARSER
# ==========================================================

parser = yacc.yacc(
    start='programa'
)


# ==========================================================
# FUNÇÃO AUXILIAR
# ==========================================================

def parse(codigo):
    return parser.parse(codigo)


# ==========================================================
# TESTE
# ==========================================================

if __name__ == "__main__":

    codigo = """
    var soma = lambda(a, b) do
        a + b
    end;

    var x = soma(10, 20);

    print(x);
    """

    arvore = parse(codigo)

    print(arvore)