#Questao 07 - iteam f
class PrettyPrinter:
    def visitExpEq(self, expeq):
        expeq.expl.accept(self)
        print (' equivalent ', end='')
        expeq.expr.accept(self)

    def visitExpImp(self, expimp):
        expimp.expl.accept(self)
        print (' implies ', end='')
        expimp.expr.accept(self)

    def visitExpOr(self, expor):
        expor.expl.accept(self)
        print (' or ', end='')
        expor.expr.accept(self)

    def visitExpNOr(self, expnor):
        expnor.expl.accept(self)
        print (' nor ', end='')
        expnor.expr.accept(self)

    def visitExpXOr(self, expxor):
        expxor.expl.accept(self)
        print (' xor ', end='')
        expxor.expr.accept(self)

    def visitExpAnd(self, expand):
        expand.expl.accept(self)
        print (' and ', end='')
        expand.expr.accept(self)

    def visitExpNAnd(self, expnand):
        expnand.expl.accept(self)
        print (' nand ', end='')
        expnand.expr.accept(self)

    def visitExpNot(self, expnot):
        print (' not ', end='')
        expnot.exp.accept(self)

    def visitExpBool(self, expbool):
        print(expbool.bool, end='')
