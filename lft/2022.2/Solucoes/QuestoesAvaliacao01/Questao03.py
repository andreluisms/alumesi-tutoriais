import ply.lex as lex

tokens = ['SELECT', 'FROM', 'JOIN', 'IF', 'THEN', 'PV', 'IGUAL', 'MAIS', 'TRUE', 'FALSE', 'NUM', 'ID']

t_SELECT = 'select'
t_FROM = 'from'
t_JOIN = 'join'
t_IF = 'if'
t_THEN = 'then'
t_PV = ';'
t_IGUAL = '='
t_MAIS = '\+'
t_TRUE = 'true'
t_FALSE = 'false'
t_ID = 'id_[A-Za-z0-9]+'
t_NUM = '0b[0-1]+'
def t_blank(t):
    '[ \t\n]+'
    pass

lexer = lex.lex()
input = 'select from join if then ; ; = + true false id_98 id_andre id_var 0b0101010010 0b1 0b0 0b001100'
lexer.input(input)



for l in lexer:
    print (l.type, l.value)