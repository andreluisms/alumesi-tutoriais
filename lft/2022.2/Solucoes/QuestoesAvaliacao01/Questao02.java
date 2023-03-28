package br.ufs.lft.prova01;

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

    public void stat(){
        switch (tok) {
            case SELECT: proxToken(); stat(); reconhece(FROM); pel(); break;
            case JOIN: proxToken(); lexp(); reconhece(PV); break;
            case IF: proxToken(); pel(); reconhece(THEN); stat(); break;
            case ID: proxToken(); reconhece(IGUAL); reconhece(NUM); break;
            default: erro();
        }
    }

    public void pel(){
        switch (tok) {
            case MAIS: proxToken(); pel(); pel(); break;
            case TRUE: proxToken();  break;
            case NUM: proxToken(); break;
            default: erro();
        }
    }

    public void lexp(){
            // A regra não é LL(1) -> Recursao a esquerda.
    }
}