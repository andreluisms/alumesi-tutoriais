# lexico.py

import ply.lex as lex


# ==========================================================
# PALAVRAS RESERVADAS
# ==========================================================

reserved = {
    'var': 'VAR',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'endif': 'ENDIF',
    'while': 'WHILE',
    'do': 'DO',
    'endwhile': 'ENDWHILE',
    'print': 'PRINT',
    'lambda': 'LAMBDA',
    'end': 'END'
}


# ==========================================================
# TOKENS
# ==========================================================

tokens = [

    # Identificadores e literais
    'ID',
    'NUMERO',

    # Operadores
    'MAIS',
    'MENOS',
    'VEZES',
    'DIVIDE',
    'ATRIBUICAO',

    # Delimitadores
    'LPAREN',
    'RPAREN',
    'VIRGULA',
    'PONTOEVIRGULA'

] + list(reserved.values())


# ==========================================================
# TOKENS SIMPLES
# ==========================================================

t_MAIS = r'\+'
t_MENOS = r'-'
t_VEZES = r'\*'
t_DIVIDE = r'/'

t_ATRIBUICAO = r'='

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_VIRGULA = r','
t_PONTOEVIRGULA = r';'


# ==========================================================
# IGNORAR ESPAÇOS E TABULAÇÕES
# ==========================================================

t_ignore = ' \t'


# ==========================================================
# NÚMEROS
# ==========================================================

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


# ==========================================================
# IDENTIFICADORES E PALAVRAS RESERVADAS
# ==========================================================

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


# ==========================================================
# COMENTÁRIOS DE LINHA
# ==========================================================

def t_COMMENT(t):
    r'\#.*'
    pass


# ==========================================================
# NOVAS LINHAS
# ==========================================================

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# ==========================================================
# ERRO LÉXICO
# ==========================================================

def t_error(t):
    print(
        f"Erro léxico: caractere ilegal '{t.value[0]}' "
        f"na linha {t.lineno}"
    )
    t.lexer.skip(1)


# ==========================================================
# CONSTRUÇÃO DO LEXER
# ==========================================================

lexer = lex.lex()


# ==========================================================
# TESTE ISOLADO
# ==========================================================

if __name__ == "__main__":

    codigo = """
    var x = 10;

    var soma = lambda(a, b) do
        a + b
    end;

    x = soma(10, 20);

    print(x);
    """

    lexer.input(codigo)

    while True:
        token = lexer.token()

        if not token:
            break

        print(token)