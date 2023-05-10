#Questao 07 - iteam a

import ply.lex as lex

tokens = ['LPAR', 'RPAR', 'TRUE', 'FALSE', 'NOT', 'AND', 'NAND', 'XOR', 'OR',
          'NOR', 'EQUIVALENT', 'IMPLIES']

t_LPAR = '\('
t_RPAR = '\)'
t_NOT = 'not'
t_AND = 'and'
t_NAND = 'nand'
t_XOR = 'xor'
t_OR = 'or'
t_NOR = 'nor'
t_EQUIVALENT = 'equivalent'
t_IMPLIES = 'implies'

def t_branco(t):
    '[\t\n ]'
    pass

def t_TRUE(t):
    'true'
    t.value = True
    return t

def t_FALSE(t):
    'false'
    t.value = False
    return t

def t_error(t):
    print('Erro léxico', t.value)

if __name__ == '__main__':
    lexico = lex.lex()
    lexico.input('true equivalent true')
    for token in lexico:
        print ("[{}]: {}".format(token.type, token.value))