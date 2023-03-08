import ply.yacc as yacc
from lexico import tokens
import sintaxeabstrata as sa

# Gramática
# programa : listadecomandos
# listadecomandos : comando
#                | listadecomandos comando
# comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA
# comando : ID ATRIBUICAO expressao PONTOEVIRGULA
# comando : IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
# comando : WHILE expressao DO listadecomandos ENDWHILE
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
        p[0] = sa.MaisdeUmComando(p[1], p[2])
    else:
        p[0] = sa.UmComando(p[1])

def p_comando_var_decl(p):
    '''comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA'''
    p[0] = sa.DeclaracaoVariavel(p[2], p[4])

def p_comando_ATRIBUICAOment(p):
    '''comando : ID ATRIBUICAO expressao PONTOEVIRGULA'''
    p[0] = sa.DeclaracaoVariavel(p[1], p[3])

def p_comando_conditional(p):
    '''comando : IF expressao THEN listadecomandos ELSE listadecomandos ENDIF'''
    pass

def p_comando_loop(p):
    '''comando : WHILE expressao DO listadecomandos ENDWHILE'''
    pass

def p_expressao_binop(p):
    '''expressao : expressao MAIS expressao
                  | expressao MENOS expressao
                  | expressao VEZES expressao
                  | expressao DIVIDE expressao'''
    pass

def p_expressao_ID(p):
    'expressao : ID'
    pass

def p_expressao_NUMERO(p):
    'expressao : NUMERO'
    pass

# Gerando a árvore sintática abstrata
def parse_programa(input_string):
    parser = yacc.yacc()
    return parser.parse(input_string)

# Testando o parser
input_string = """
VAR x = 5;
VAR y = 3;
WHILE x > 0 DO
    x = x - y;
    IF x == 2 THEN
        y = y * 2;
    ELSE
        y = y + 1;
    ENDIF
ENDWHILE
"""
abstract_syntax_tree = parse_programa(input_string)
print(abstract_syntax_tree)