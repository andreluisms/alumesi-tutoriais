# Tutorial Visitor
1. Adicionar método def accept(self, visitor) às classes da sintaxe abstrata. Como foi feito com o print(). Classes abstratas não implementam o método (pass), já as concretas, chamam o método correspondente de visita no visitor. 
Por exemplo para **UmComando** temos:
```
class UmComando(Listadecomandos):
    def __init__(self, comando):
        self.comando = comando
    def print(self):
        print('[UmComando]', end='')
        self.comando.print()
    def accept(self, visitor):
        visitor.visitUmComando(self)
```

2. Criar a classe abstrata Visitor. A classe **Visitor** deve ter métodos de visitas para todas as classes concretas da sintaxe abstrata.
Esboço inicial:
```
from abc import abstractmethod
from abc import ABCMeta

class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visitUmComando(self, umComando):
        pass
    @abstractmethod
    def visitMaisdeUmComando(self, maisdeUmComando):
        pass
 ...
```

3. Criar a classe VisitorPrettyPrinter. A classe VisitorPrettyPrinter extende Visitor. A seguir, um esboço inicial:
```
import Visitor
class VisitorPrettyPrinter(Visitor):
    def visitExpressaoSoma(self, expressaoSoma):
        expressaoSoma.expesq.accept(self)
        print(' + ', end='')
        expressaoSoma.expdir.accept(self)
    def visitExpressaoSubtracao(self, expressaoSubtracao):
        expressaoSubtracao.expesq.accept(self)
        print(' - ', end='')
        expressaoSubtracao.expdir.accept(self)
...
```

4. Criar a classe VisitorSemantico. Neste primeiro exemplo, o VisitorSemantico deve lançar erro sempre que em uma expressao aparecer alguma operação de multiplicação. 
