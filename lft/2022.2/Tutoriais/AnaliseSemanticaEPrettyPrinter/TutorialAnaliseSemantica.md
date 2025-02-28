# Tutorial Visitor
1. Usar os arquivos lexico, sintatico e sintaxe abstrata presentes em: https://github.com/andreluisms/alumesi-tutoriais/tree/main/lft/2022.2/Tutoriais/AnaliseSemanticaEPrettyPrinter

2. Adicionar método def accept(self, visitor) às classes da sintaxe abstrata. Classes abstratas não implementam o método accept, já as concretas, chamam o método correspondente de visita no visitor. 

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

3. Criar a classe abstrata Visitor. A classe **Visitor** deve ter métodos de visitas para todas as classes concretas da sintaxe abstrata.
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

4. Criar a classe VisitorPrettyPrinter. A classe **VisitorPrettyPrinter** extende **Visitor**. A seguir, um esboço inicial:
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

5. Criar a classe VisitorSemantico. Neste primeiro exemplo, o **VisitorSemantico** deve lançar erro sempre que em uma expressao aparecer alguma operação de multiplicação. 
