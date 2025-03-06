package br.ufs.lft.u1prova20242;

public class u1prova20242{
    private Lexico lexico;
    public void erro(){
        System.out.print("Erro Sintático");
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

    public void cmds(){
        switch (tok) {
            case BEGIN: proxToken(); cmd(); reconhece(PONTO_E_VIRGULA); cmds(); reconhece(END); break;
            case EXCLAMACAO: proxToken(); cmd(); reconhece(PONTO_E_VIRGULA); break;
            default: erro();
        }
    }

    public void cmd(){
        switch (tok) {
            case FUNC: proxToken(); reconhece(ID); reconhece(ABRE_PARENTESIS); parami(); break;
            case FOR: proxToken(); reconhece(ABRE_PARENTESIS); reconhece(STRING); reconhece(FECHA_PARENTESIS); cmds(); break;
            case ID: proxToken(); reconhece(IGUAL); binum(); break;
            default: erro();
        }
    }
    public void parami(){
        switch (tok) {
            case ID: proxToken(); reconhece(ID); paramf(); break;
            default: erro();
        }
    }
   /** Também válido
   
    public void parami(){
            reconhece(ID); reconhece(ID); paramf(); break;
    }
    
    **/
    public void paramf(){
        switch (tok) {
            case VIRGULA: proxToken(); reconhece(ID); reconhece(ID); paramf(); break;
            case FECHA_PARENTESIS: proxToken(); break;
            default: erro();
        }
    }

    public void binum(){
        switch (tok) {
            case ZERO: proxToken(); binum(); break;
            case UM: proxToken(); binum(); break;
            case B: proxToken(); break;
            default: erro();
        }
    }
}
