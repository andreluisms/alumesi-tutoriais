import ply.lex as lex

tokens = ['BEGIN', 'PONTO_E_VIRGULA', 'END', 
          'EXCLAMACAO', 'FUNC', 'ID', 
          'ABRE_PARENTESIS', 'FOR', 'STRING', 
          'FECHA_PARENTESIS', 'IGUAL', 'VIRGULA', 
          'ZERO', 'UM', 'B']

t_BEGIN = 'begin'
t_PONTO_E_VIRGULA = ';'
t_END = 'end'
t_EXCLAMACAO = '!'
t_FUNC  = 'func'
t_ID =  '&[a-zA-Z0-9]+'
t_ABRE_PARENTESIS = '\('
t_FOR = 'for'
t_STRING = '\#[^#]*\#' 
t_FECHA_PARENTESIS = '\)' 
t_IGUAL = '='
t_VIRGULA = ','
t_ZERO = '0'
t_UM = '1'
t_B = 'b'

def t_blank(t):
    '[ \t\n]+'
    pass

lexer = lex.lex()
input = 'begin ; end ! func &98 &andre &var  ( for #asdasdas\ndsdfsdfsdfsddddddsa### ) = , 0 1 b'
lexer.input(input)



for l in lexer:
    print (l.type, l.value)
