import ply.yacc as yacc
from lexico import tokens
import sintaxeabstrata as sa

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



# Definindo as regras da gramática
def p_programa(p):
    '''programa : listadecomandos'''
    p[0] = sa.Programa(p[1])

def p_listadecomandos(p):
    '''listadecomandos : comando
                      | listadecomandos comando'''
    if len(p) == 2:
        p[0] = sa.UmComando(p[1])
    else:
        p[0] = sa.MaisdeUmComando(p[1], p[2])

def p_comando_declaracaovariavel(p):
    '''comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA'''
    p[0] = sa.DeclaracaoVariavel(p[2], p[4])

def p_comando_atribuicao(p):
    '''comando : ID ATRIBUICAO expressao PONTOEVIRGULA'''
    p[0] = sa.AtribuicaoVariavel(p[1], p[3])
