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


lambda → LAMBDA LPAREN paramlist RPAREN DO expressao END
       | LAMBDA LPAREN RPAREN DO expressao END


paramlist → ID
          | paramlist VIRGULA ID
```
