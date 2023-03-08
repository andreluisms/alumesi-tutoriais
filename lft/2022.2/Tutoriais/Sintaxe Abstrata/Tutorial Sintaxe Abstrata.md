# Tutorial - Construindo um Analisador Sintático com Gramática Abstrata

Para o seguinte tutorial, iremos adotar a seguinte linguagem de programação, cuja gramática é apresentada a seguir:

```
Gramática
programa : listadecomandos
listadecomandos : comando
                | listadecomandos comando
comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA
        | ID ATRIBUICAO expressao PONTOEVIRGULA
        | IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
        | WHILE expressao DO listadecomandos ENDWHILE
expressao : expressao MAIS expressao
          | expressao MENOS expressao
          | expressao VEZES expressao
          | expressao DIVIDE expressao
          | ID
          | NUMERO
```

### Passo 1: Definindo as classes da Sintaxe Abstrata
Para definição da classe da Sintaxe Abstrata, costuma-se associar uma classe abstrata para cada variável e uma concreta para cada regra. No exemplo a seguir apresentamos as regras relativas a variável listadecomandos. E como foi feito seu mapeamento para a classe abstrata Listadecomandos e as classes concretas UmComando e MaisdeUmComando.


```
from abc import abstractmethod
from abc import ABC

# listadecomandos : comando
#                 | listadecomandos comando

class Listadecomandos(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass


class UmComando(Listadecomandos):
    def __init__(self, comando):
        self.comando = comando
    def print(self):
        pass


class MaisdeUmComando(Listadecomandos):
    def __init__(self, comando, listadecomandos):
        self.comando = comando
        self.listadecomandos = listadecomandos
    def print(self):
        pass
```

Python não apresenta o conceito de sintaxe abstrata. Por isso, usamos o módulo ABC. Ele permite a criação de classes abstratas. Com isso, podemos criar na classe abstrata métodos abstratos (@abstractmethod). Tais métodos serão codificados pelas classes derivadas. Um exemplo disso é o método print(), apresentado no exemplo acima. 


#### **QUESTÃO 1: Abra o arquivo [SintaxeAbstrata.py](https://github.com/andreluisms/alumesi-tutoriais/blob/main/lft/2022.2/Tutoriais/Sintaxe%20Abstrata/SintaxeAbstrata.py). Analise o código presente. Codifique o restante da sintaxe abstrata** 