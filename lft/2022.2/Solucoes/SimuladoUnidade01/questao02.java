package br.ufs.lft.simulado01
// Codigo é somente um esboço. Para sua execução, se faz necessário fazer algumas adequações.



public class sintatico{

    private Lexico lexico;

    public void erro(){
        System.print.out("Erro Sintatico");
    }

    public void proxToken(){
        tok = this.lexico.proxToken();
    }

    public void reconhece (int token){
        if (token == tok)
           tok = proxToken();
        else
           erro();
    }


// <statement> →  for <exp> <statement> 
//              | return ; 
//              |  if <exp> <statement> else 
//              | id = <lstExp>
// <exp> →  <exp_term> + <exp2>

// <exp2>  →  + <exp_term><exp2> | - <exp_term><exp2> 
// <lstExp> → # <exp> <lstExp> |  # <exp> 

    public void statement()
        switch (tok){
            case FOR: proxToken(); exp(); statement(); break;
            case RETURN: proxToken(); reconhece(PONTOEVIRGULA); break;
            case IF: proxToken(); exp(); statement(); reconhece(ELSE); break;
            case ID: proxToken(); reconhece(IGUAL); lstExp(); break;
            default: erro();
        } 


    public void exp(){
        exp_term(); reconhece (MAIS); exp2();
    }
// <exp_term> → id | true | false | num
    public void exp_term(){
        switch (tok){
            case ID: proxToken(); break;
            case TRUE: proxToken(); break;
            case FALSE: proxToken(); break;
            case NUM: proxToken(); break;
            default: erro();
        } 
    }

    public void exp2(){
        switch (tok){
            case MAIS: proxToken(); exp_term(); exp2();
            case MENOS: proxToken(); exp_term(); exp2();
            default: erro();
        }
    }

    public void lstExp(){
        // A regra não é LL(1)
        // <lstExp> → # <exp> <lstExp> |  # <exp>
        // P(lstExp) = {#}
        // Conflito de aplicação de regra
    }
}

