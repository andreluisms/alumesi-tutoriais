from sintatico_sintaxeabstrata import *

class PrettyPrinter:
    def visitExpMais(self, expMais):
        expMais.expl.accept(self)
        print(' + ', end = '')
        expMais.expr.accept(self)
    def visitExpDiv(self, expDiv):
        expDiv.expl.accept(self)
        print(' / ', end = '')
        expDiv.expr.accept(self)
    def visitExpVezes(self, expVezes):
        expVezes.expl.accept(self)
        print(' * ', end = '')
        expVezes.expr.accept(self)
    def visitExpExp(self, expExp):
        expExp.expl.accept(self)
        print(' ** ', end = '')
        expExp.expr.accept(self)
    def visitExpPar(self, expPar):
        print('(', end = '')
        expPar.exp.accept(self)
        print(')', end = '')
    def visitExpNum(self, expNum):
        print (expNum.exp, end = '')

if __name__ == '__main__':
    lex = lex.lex()
    lex.input('3 + 3 * 3 / 2 ** 4 * ( 48 * 35 )')
    parser = yacc.yacc()
    parser.parse().accept(PrettyPrinter())
    print()