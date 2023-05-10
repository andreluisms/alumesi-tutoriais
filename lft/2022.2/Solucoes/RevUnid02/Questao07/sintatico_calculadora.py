#Questao 07 - iteam c

from lexico import *
import ply.yacc as yacc

precedence = (('left', 'EQUIVALENT', 'IMPLIES'),
             ('left', 'OR', 'NOR'),
             ('left', 'XOR'),
             ('left', 'AND', 'NAND'),
             ('right', 'NOT'))

def p_exp_1(p):
    '''exp : exp EQUIVALENT exp'''
    p[0] = (p[1] == p[3])

def p_exp_2(p):
    '''exp : exp IMPLIES exp'''
    p[0] = p[1] or (not p[3])

def p_exp_3(p):
    '''exp : exp OR exp'''
    p[0] = p[1] or p[3]

def p_exp_4(p):
    '''exp : exp NOR exp'''
    p[0] = not (p[1] or p[3])

def p_exp_5(p):
    '''exp : exp XOR exp'''
    p[0] = not(p[1] ^ p[3])

def p_exp_6(p):
    '''exp : exp AND exp'''
    p[0] = p[1] and p[3]

def p_exp_7(p):
    '''exp : exp NAND exp'''
    p[0] = not(p[1] and p[3])

def p_exp_8(p):
    '''exp : NOT exp'''
    p[0] = not p[1]

def p_exp_9(p):
    '''exp : LPAR exp RPAR'''
    p[0]= p[1]

def p_exp_10(p):
    '''exp : TRUE'''
    p[0]= p[1]

def p_exp_11(p):
    '''exp : FALSE'''
    p[0]= p[1]

def p_error(p):
    print('Erro sintático', p)

if __name__ == '__main__':
    lexico = lex.lex()
    lexico.input('true equivalent true or false and true implies false and not true xor false nor false nand true and (true or false)')
    parser = yacc.yacc()
    print(parser.parse())