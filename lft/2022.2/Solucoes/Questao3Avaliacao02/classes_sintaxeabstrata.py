class ExpMais:
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpMais(self)

class ExpDiv:
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpDiv(self)

class ExpVezes:
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpVezes(self)

class ExpExp:
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpExp(self)


class ExpPar:
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        visitor.visitExpPar(self)


class ExpNum:
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        visitor.visitExpNum(self)
