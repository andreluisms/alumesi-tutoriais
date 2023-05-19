import ply.lex as lex

tokens = ['NUM', 'MAIS', 'MENOS', 'VEZES', 'DIV','EXP', 'APAR', 'FPAR']

t_MAIS = '\+'
t_MENOS = '\-'
t_VEZES = '\*'
t_DIV = '/'
t_EXP = '\*\*'
t_APAR = '\('
t_FPAR = '\)'

def t_branco(t):
    '[ \t\n]+'
    pass

def t_NUM(t):
    '[1-9][0-9]*'
    t.value = int(t.value)
    return t


if __name__ == '__main__':
    lex = lex.lex()
    lex.input('1213123 + - * / ** ( )')
    for token in lex:
        print(token.type, token.value)