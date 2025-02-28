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

def p_comando_if(p):
    '''comando : IF expressao THEN listadecomandos ELSE listadecomandos ENDIF'''
    p[0] = sa.ComandoIF(p[2], p[4],p[6])

def p_comando_while(p):
    '''comando :  WHILE expressao DO listadecomandos ENDWHILE '''
    p[0] = sa.ComandoWhile(p[2], p[4])


def p_expressao_Mais_cam1(p):
    '''expressao :  expressao MAIS expressao2 '''
    p[0] = sa.ExpressaoSoma(p[1], p[3])

def p_expressao_Menos_cam1(p):
    '''expressao :  expressao MENOS expressao2 '''
    p[0] = sa.ExpressaoSubtracao(p[1], p[3])

def p_expressao_cam1_to_cam2(p):
    '''expressao :  expressao2 '''
    p[0] = p[1]


def p_expressao_Mul_cam2(p):
    '''expressao2 :  expressao2 VEZES expressao3 '''
    p[0] = sa.ExpressaoMul(p[1], p[3])


def p_expressao_Div_cam2(p):
    '''expressao2 :  expressao2 DIVIDE expressao3 '''
    p[0] = sa.ExpressaoDiv(p[1], p[3])

def p_expressao_cam2_to_cam3(p):
    '''expressao2 :  expressao3 '''
    p[0] = p[1]

def p_expressao_ID_cam3(p):
    '''expressao3 :  ID '''
    p[0] = sa.ExpressaoID(p[1])

def p_expressao_Num_cam3(p):
    '''expressao3 :  NUMERO '''
    p[0] = sa.ExpressaoNumero(p[1])


def parse_programa(input_string):
    parser = yacc.yacc()
    return parser.parse(input_string)
# Testando o parser


input_string = """
VAR x = 5;
VAR y = 3;
WHILE x + 0 DO
    x = x - y;
    IF x + 2 THEN
        y = y * 2;
    ELSE
        y = y + 1;
    ENDIF
ENDWHILE
"""
abstract_syntax_tree = parse_programa(input_string)
print(abstract_syntax_tree)
abstract_syntax_tree.print()