# Construindo um Analisador Sintático com Gramática Abstrata

Para o seguinte tutorial, iremos adotar a seguinte linguagem de programação, cuja gramática é apresentada a seguir:

```
programa → listadecomandos
listadecomandos → comando
                | listadecomandos comando
comando → VAR ID ATRIBUICAO expressao PONTOEVIRGULA
        | ID ATRIBUICAO expressao PONTOEVIRGULA
        | IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
        | WHILE expressao DO listadecomandos ENDWHILE
expressao → expressao MAIS expressao
          | expressao MENOS expressao
          | expressao VEZES expressao
          | expressao DIVIDE expressao
          | ID
          | NUMERO
```

Adicionalmente, façam o download dos seguintes arquivos:

- [lexico.py](https://github.com/andreluisms/alumesi-tutoriais/blob/main/lft/2022.2/Tutoriais/Sintaxe%20Abstrata/lexico.py)

- [sintatico.py](https://github.com/andreluisms/alumesi-tutoriais/blob/main/lft/2022.2/Tutoriais/Sintaxe%20Abstrata/sintatico.py)

- [sintaxeabstrata.py](https://github.com/andreluisms/alumesi-tutoriais/blob/main/lft/2022.2/Tutoriais/Sintaxe%20Abstrata/sintaxeabstrata.py)

# Passo 1: Definindo as classes da Sintaxe Abstrata
Para definição das classes da Sintaxe Abstrata, costuma-se associar uma classe abstrata para cada variável e uma concreta para cada regra. No exemplo a seguir, apresentamos as regras relativas a variável **listadecomandos** e como foi feito seu mapeamento para a classe abstrata **Listadecomandos** e as classes concretas **UmComando** e **MaisdeUmComando**.


```
from abc import abstractmethod
from abc import ABC

# listadecomandos → comando
#                 | listadecomandos comando

class Listadecomandos(ABC):
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

Python não apresenta o conceito de sintaxe abstrata. Por isso, usamos o **módulo ABC**. **ABC** permite a criação de classes abstratas. Com isso, podemos criar na classe abstrata métodos abstratos (@abstractmethod). Tais métodos serão codificados pelas classes derivadas. Um exemplo disso é o método **print()**, apresentado no exemplo acima. 


> *Qestão 01: Abra o arquivo [sintaxeabstrata.py](https://github.com/andreluisms/alumesi-tutoriais/blob/main/lft/2022.2/Tutoriais/Sintaxe%20Abstrata/sintaxeabstrata.py). Analise o código presente. Codifique o restante da sintaxe abstrata* 



# Passo 2: Implementando a gramática no PLY e instanciando classes da sintaxe abstrata.

A implementação de regras no PLY é bastante simples. Ela é feita através de funções. A função deve começar com o prefixo **p_**, seguido por um nome que a identifique. Adicionalmente, recebe o parâmetro **p** que representa a regra implementada. 

Feita a declaração da função, precisamos informar a regra a qual a função se refere. A declaração da regra é feita através de **docstring**. A **docstring** é uma string literal presente na primeira linha da definição de uma função. Ela é declarada através de aspas triplas ('''). O operador seta (→), usado em gramáticas livre de contexto, deve ser substituído por dois pontos (:)

A seguir, um exemplo:

```
# listadecomandos → comando
#                 | listadecomandos comando

def p_listadecomandos(p):
    '''listadecomandos : comando
                      | listadecomandos comando'''
        pass
```


A seguir, devemos implementar o comportamento da função. Esse comportamento será realizado no momento que o analisador sintático aplicar a regra em questão. Nessa atividade, queremos que o analisador sintático gere um objeto que represente a regra aplicada, ou seja, um objeto de uma das classes concretas codificadas na *Questão 01*. O próximo trecho de código apresenta esse comportamento:


```
def p_listadecomandos(p):
    '''listadecomandos : comando
                      | listadecomandos comando'''
    if len(p) == 2:
        p[0] = sa.UmComando(p[1])
    else:
        p[0] = sa.MaisdeUmComando(p[1], p[2])
```

No exemplo, testamos o tamanho do parâmetro **p**. O parâmetro **p** representa as duas regras relativas a variável **listadecomandos**. Se o tamanho de **p** é 2, significa que o analisador sintático reconheceu a primeira regra, visto que **listadecomandos : comando** é composto de dois elementos. Para acessar esses elementos, basta seguirmos a ordem de suas ocorrências. Assim, p[0] representa **listadecomandos** e p[1] representa **comando**. Por fim, instanciamos a classe **UmComando**, passando como parâmetro (p[1]). 

Percebam que a instância gerada é passada para p[0] que representa a variável **listadecomandos** presente no lado esquerdo da regra (antes dos dois pontos : ). É assim que geramos um nó na árvore que representa a sintaxe abstrata.

No caso do *else*, instanciamos a classe **MaisdeUmComando**, passando como parâmetros p[1] e p[2], que representam, respectivamente, **listadecomandos** e **comando**. 

> *Qestão 02: Abra o arquivo [sintatico.py](https://github.com/andreluisms/alumesi-tutoriais/blob/main/lft/2022.2/Tutoriais/Sintaxe%20Abstrata/sintatico.py). Analise o código presente. Codifique as regras restantes, incluindo o comportamento para instanciação das classes da sintaxe abstrata* 



# Passo 3: Avaliando a Sintaxe Abstrata

Para validar que deu tudo certo, podemos adicionar o seguinte código ao **sintatico.py

```
# Gerando a árvore sintática abstrata
def parse_programa(input_string):
    parser = yacc.yacc()
    return parser.parse(input_string)
# Testando o parser
input_string = """
VAR x = 5;
VAR y = 3;
WHILE x + 0 DO
    x = x - y;
    IF x + 2 THEN
        y = y * 2;
    ELSE
        y = y + 1;
    ENDIF
ENDWHILE
"""
abstract_syntax_tree = parse_programa(input_string)
```

A árvore foi gerada, porém o resultado não foi exibido. Para podermos visualizar seu conteúdo, é necessário implementarmos o comportamento do método print para cada uma das classes concretas presentes na sintaxe abstrata, conforme o exemplo abaixo:


```
class UmComando(Listadecomandos):
    def __init__(self, comando):
        self.comando = comando
    def print(self):
        print('[UmComando]', end='')
        self.comando.print()
```


> *Qestão 04: Abra o arquivo [sintaxeabstrata.py](https://github.com/andreluisms/alumesi-tutoriais/blob/main/lft/2022.2/Tutoriais/Sintaxe%20Abstrata/sintaxeabstrata.py). Analise o código presente. Codifique o comando print para todas as classes concretas do arquivo sintaxeabstrata.py* 

Finalizado esse passo, adicione no arquivo sintatico.py a seguinte linha de código.

```
abstract_syntax_tree.print()
```
