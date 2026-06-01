# Tutorial de Análise Semântica com Visitor e Tabela de Símbolos

## Objetivo

Neste tutorial, iremos implementar a análise semântica da linguagem desenvolvida nas etapas anteriores.

Ao final, o compilador será capaz de detectar:

* variáveis não declaradas;
* variáveis redeclaradas;
* parâmetros duplicados em funções lambda;
* chamadas para identificadores que não são funções;
* chamadas com quantidade incorreta de argumentos.

A análise será implementada utilizando o padrão Visitor.

Arquivos a serem desenvolvidos:

```txt
TabelaSimbolos.py
VisitorSemantico.py
```

---

A GLC base é apresentada a seguir:
```
programa → listadecomandos

listadecomandos → comando
                | listadecomandos comando

comando → VAR ID ATRIBUICAO expressao PONTOEVIRGULA
        | ID ATRIBUICAO expressao PONTOEVIRGULA
        | IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
        | WHILE expressao DO listadecomandos ENDWHILE
        | PRINT LPAREN expressao RPAREN PONTOEVIRGULA
        | PONTOEVIRGULA

expressao → expressao MAIS expressao
          | expressao MENOS expressao
          | expressao VEZES expressao
          | expressao DIVIDE expressao
          | LPAREN expressao RPAREN
          | ID
          | NUMERO
          | lambda
          | chamadadefuncao

lambda → LAMBDA LPAREN paramlist RPAREN DO expressao END
       | LAMBDA LPAREN RPAREN DO expressao END

paramlist → ID
          | paramlist VIRGULA ID


chamadadefuncao → ID LPAREN listaargumentos RPAREN

listaargumentos → expressao
                | listaargumentos VIRGULA expressao
                | ε
```


# Parte 1 – O que é análise semântica?

O analisador sintático garante que o programa está estruturalmente correto.

Por exemplo:

```txt
var x = 10;
print(x);
```

e

```txt
print(y);
```

são sintaticamente válidos.

Entretanto:

```txt
print(y);
```

utiliza uma variável que nunca foi declarada.

Detectar esse tipo de problema é responsabilidade da análise semântica.

---

# Parte 2 – A tabela de símbolos

A tabela de símbolos armazenará informações sobre identificadores encontrados durante a análise.

Inicialmente armazenaremos:

```txt
nome
categoria
```

onde categoria pode ser:

```txt
variavel
funcao
```

---

# Exercício 1 – Criando a classe Símbolo

Crie a classe abaixo.

```python
class Simbolo:

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
```

---

# Exercício 2 – Estrutura inicial da tabela

Crie a classe:

```python
class TabelaSimbolos:

    def __init__(self):
        self.tabela = {}
```

---

# Exercício 3 – Inserindo símbolos

Complete o método:

```python
def inserir(self, simbolo):
    pass
```

Regras:

* se o símbolo ainda não existir:

  * inserir normalmente

* caso contrário:

  * lançar exceção

Exemplo:

```python
ts.inserir(Simbolo("x", "variavel"))
```

---

# Exercício 4 – Procurando símbolos

Complete:

```python
def buscar(self, nome):
    pass
```

Exemplos:

```python
ts.buscar("x")
```

retorna:

```txt
Simbolo("x","variavel")
```

---

# Exercício 5 – Verificando existência

Implemente:

```python
def existe(self, nome):
    pass
```

Exemplos:

```python
ts.existe("x")
```

retorna:

```txt
True
```

---

# Parte 3 – Estrutura do Visitor Semântico

O Visitor Semântico percorrerá a AST e utilizará a tabela de símbolos.

Estrutura inicial:

```python
class VisitorSemantico(VisitorAbstrato):

    def __init__(self):
        self.tabela = TabelaSimbolos()
```

---

# Exercício 6 – Visitando o programa

Implemente:

```python
def visitProgramaListaComandos(self, programa):
    pass
```

Objetivo:

visitar:

```python
programa.lista_comandos
```

---

# Exercício 7 – Visitando listas de comandos

Implemente:

```python
visitListaDeComandosComando
visitListaDeComandosLista
```

Objetivo:

percorrer toda a árvore.

Teste:

```txt
var x = 10;
var y = 20;
print(x);
```

Todos os comandos devem ser visitados.

---

# Parte 4 – Declaração de variáveis

Considere:

```txt
var x = 10;
```

Quando uma declaração é encontrada devemos inserir:

```txt
x
```

na tabela.

---

# Exercício 8 – Implementando declaração

Complete:

```python
def visitComandoDeclaracao(self, comando):
    pass
```

Passos:

1. visitar expressão da direita
2. criar símbolo
3. inserir símbolo

---

# Exercício 9 – Detectando redeclaração

Considere:

```txt
var x = 10;
var x = 20;
```

Resultado esperado:

```txt
Erro semântico:
Variável x já declarada.
```

Ajuste:

```python
TabelaSimbolos.inserir()
```

---

# Parte 5 – Uso de identificadores

Considere:

```txt
print(x);
```

Para utilizar um identificador ele precisa existir.

---

# Exercício 10 – Identificador declarado?

Implemente:

```python
def visitExpressaoIdentificador(self, expressao):
    pass
```

Regra:

```python
x
```

deve existir na tabela.

Caso contrário:

```txt
Erro semântico:
Variável x não declarada.
```

---

# Exercício 11 – Atribuição

Implemente:

```python
visitComandoAtribuicao
```

Regra:

```txt
x = 10;
```

somente é válido se:

```txt
x
```

já existir.

Teste:

```txt
x = 10;
```

Resultado:

```txt
Erro semântico:
Variável x não declarada.
```

---

# Parte 6 – Lambdas

Agora analisaremos:

```txt
var soma =
    lambda(a,b) do
        a+b
    end;
```

---

# Exercício 12 – Registrando funções

Modifique:

```python
class Simbolo
```

para armazenar:

```python
parametros
```

Exemplo:

```python
Simbolo(
    "soma",
    "funcao",
    2
)
```

---

# Exercício 13 – Reconhecendo lambdas

Em:

```python
visitComandoDeclaracao
```

identifique quando a expressão é:

```python
ExpressaoLambda
```

Neste caso inserir:

```txt
categoria = funcao
```

---

# Exercício 14 – Parâmetros duplicados

Considere:

```txt
lambda(a,a) do
    a
end
```

Resultado esperado:

```txt
Erro semântico:
Parâmetro duplicado: a
```

Implemente:

```python
visitLambdaComParametros
```

---

# Parte 7 – Escopos

Até agora existe apenas escopo global.

Vamos criar escopos para lambdas.

---

# Exercício 15 – Pilha de escopos

Altere:

```python
self.tabela
```

para:

```python
self.escopos = []
```

Crie:

```python
pushEscopo()
popEscopo()
```

---

# Exercício 16 – Inserindo parâmetros no escopo local

Considere:

```txt
lambda(a,b) do
    a+b
end
```

Durante a visita da lambda:

1. criar novo escopo
2. inserir parâmetros
3. visitar expressão
4. remover escopo

---

# Parte 8 – Chamadas de função

Considere:

```txt
soma(10,20)
```

---

# Exercício 17 – Função existe?

Implemente:

```python
visitChamadaDeFuncaoConcreta
```

Verifique:

```txt
soma
```

foi declarada.

---

# Exercício 18 – É realmente uma função?

Considere:

```txt
var x = 10;

x(5);
```

Resultado esperado:

```txt
Erro semântico:
x não é uma função.
```

---

# Exercício 19 – Quantidade de argumentos

Considere:

```txt
var soma =
    lambda(a,b) do
        a+b
    end;

soma(10);
```

Resultado esperado:

```txt
Erro semântico:
Quantidade incorreta de argumentos.
```

---

# Exercício 20 – Projeto Final

O analisador deve aceitar:

```txt
var soma =
    lambda(a,b) do
        a+b
    end;

var x = soma(10,20);

print(x);
```

e rejeitar:

```txt
print(y);
```

```txt
var x = 10;
var x = 20;
```

```txt
x = 10;
```

```txt
var x = 10;
x(5);
```

```txt
var soma =
    lambda(a,b) do
        a+b
    end;

soma(10);
```