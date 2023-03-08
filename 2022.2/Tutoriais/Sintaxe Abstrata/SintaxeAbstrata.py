from abc import abstractmethod
from abc import ABCMeta

'''
Declaracao de funcao
FuncDecl
'''
class FuncDecl(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class FuncDeclConcrete(FuncDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body
    def print(self):
        return visitor.visitFuncDeclConcrete(self)

'''
Assinatura de funcao
Signature
'''
class Signature(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass


class SignatureConcrete(Signature):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams
    def print(self):
        return visitor.visitSignatureConcrete(self)
'''
Parametros de assinatura de funcao
SigParams
'''

class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class SingleSigParams(SigParams):
    def __init__(self, type, id):
        self.type = type
        self.id = id
    def print(self):
        return visitor.visitSingleSigParams(self)


class CompoundSigParams(SigParams):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams
    def print(self):
        return visitor.visitCompoundSigParams(self)

'''
Corpo de uma funcao
Body
'''

class Body(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass


class BodyConcrete(Body):
    def __init__(self, stms):
        self.stms = stms
    def print(self):
        return visitor.visitBodyConcrete(self)

'''
Comandos
Stms
'''

class Stms(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class SingleStm(Stms):
    def __init__(self, stm):
        self.stm = stm
    def print(self):
        return visitor.visitSingleStm(self)

class CompoundStm(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def print(self):
        return visitor.visitCompoundStm(self)

'''
Comando
Stm
'''

class Stm(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class StmExp(Stm):
    def __init__(self, exp):
        self.exp = exp
    def print(self):
        return visitor.visitStmExp(self)

class StmWhile(Stm):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block
    def print(self):
        return visitor.visitStmWhile(self)

class StmReturn(Stm):
    def __init__(self, exp):
        self.exp = exp
    def print(self):
        return visitor.visitStmReturn(self)

'''
Expressoes
Exp
'''

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class AssignExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def print(self):
        return visitor.visitAssignExp(self)

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def print(self):
        return visitor.visitSomaExp(self)


class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def print(self):
        return visitor.visitMulExp(self)


class PotExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def print(self):
        return visitor.visitPotExp(self)


class CallExp(Exp, Stm):
    def __init__(self, call):
        self.call = call

    def print(self):
        return visitor.visitCallExp(self)

class NumExp(Exp):
    def __init__(self, num):
        self.num = num
    def print(self):
        return visitor.visitNumExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def print(self):
        return visitor.visitIdExp(self)

class BooleanExp(Exp):
    def __init__(self, boolValue):
        self.boolValue = boolValue
    def print(self):
        return visitor.visitBooleanExp(self)

'''
Chamada de funcao
Call
'''
class Call(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class ParamsCall(Call):
    def __init__ (self, id, params):
        self.id = id
        self.params = params
    def print(self):
        return visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id
    def print(self):
        return visitor.visitNoParamsCall(self)


'''
Parametros de uma chamada de funcao
Params
'''
class Params(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def print(self):
        return visitor.visitCompoundParams(self)

class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp
    def print(self):
        return visitor.visitSingleParam(self)
