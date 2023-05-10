#Questao 07 - iteam d
from abc import abstractmethod
from abc import ABC

class Exp(ABC):
    @abstractmethod
    def accept(self):
        pass

class ExpEq(Exp):
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpEq(self)


class ExpImp(Exp):
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpImp(self)

class ExpOr(Exp):
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpOr(self)


class ExpNOr(Exp):
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpNOr(self)


class ExpXOr(Exp):
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpXOr(self)

class ExpAnd(Exp):
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpAnd(self)

class ExpNAnd(Exp):
    def __init__(self, expl, expr):
        self.expl = expl
        self.expr = expr
    def accept(self, visitor):
        visitor.visitExpNAnd(self)

class ExpNot(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        visitor.visitExpNot(self)

class ExpPar(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        visitor.visitExpNot(self)


class ExpBool(Exp):
    def __init__(self, bool):
        self.bool = bool
    def accept(self, visitor):
        visitor.visitExpBool(self)