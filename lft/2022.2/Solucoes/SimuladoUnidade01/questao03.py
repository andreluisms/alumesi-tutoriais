import ply.lex as lex
RESERVADAS = ['FOR', 'RETURN', 'IF', 'ELSE', 'TRUE', 'FALSE']
tokens = ['PONTOEVIRGULA', 'ID', 'IGUAL', 'MAIS', 'NUM', 'MENOS', 'CERQUILHA'] + RESERVADAS

t_FOR = 'for'
t_RETURN = 'return'
t_IF = 'if'
t_ELSE = 'else'
t_TRUE = 'true'
t_FALSE = 'false'
t_PONTOEVIRGULA = ';'
t_IGUAL = '='
t_MAIS = r'\+'
t_NUM = '0x[A-F0-9]{5}'
t_MENOS = '-'
t_CERQUILHA = r'\#'
t_ID = r'\#[a-zA-Z0-9]+\#'

def t_blank(t):
    r'[ \t\n]'
    pass
    
lexer = lex.lex()
input = 'for return 0x35838 \t - + = if else true false ; # #asdsad83198ASDASDhjash8319# 0x34334'
lexer.input(input)



for l in lexer:
    print (l.type, l.value)