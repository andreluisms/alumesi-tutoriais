import ply.yacc as yacc
from lexico import *

# tokens = ['NUM', 'MAIS', 'MENOS', 'VEZES', 'DIV','EXP', 'APAR', 'FPAR']

precedence = (('left', 'DIV', 'VEZES'),
              ('left', 'MAIS'),
              ('left', 'EXP'))

def p_expMAIS(p):
    '''exp : exp MAIS exp '''
    p[0] = int((p[1] + p[3]) % 10)

def p_expDIV(p):
    '''exp : exp DIV exp '''
    p[0] = int((p[1] / p[3]) % 10)
 

def p_expVEZES(p):
    '''exp : exp VEZES exp '''
    p[0] = int((p[1] * p[3]) % 10)


def p_expEXP(p):
    '''exp : exp EXP exp '''
    p[0] = int((p[1] ** p[3]) % 10)


def p_expPAR(p):
    '''exp : APAR exp FPAR '''
    p[0] = int(p[2] % 10)


def p_expNUM(p):
    '''exp : NUM '''
    p[0] = int(p[1] % 10)


if __name__ == '__main__':
    lex = lex.lex()
    lex.input('3 + 3 * 3 / 2 ** 4 * ( 48 * 35 )')
    parser = yacc.yacc()
    parser.parse(debug=True)