%option noyywrap yylineno

%{
#include <stdio.h>
#include <string.h>

/* Estrutura simples para a Tabela de Símbolos */
typedef struct {
    char nome[100];
    char tipo[20];
} Simbolo;

Simbolo tabela[1000];
int num_simbolos = 0;
char tipo_atual[20] = ""; /* Armazena o tipo mais recente lido (int, char, float) */

/* Função para adicionar um identificador na tabela usando o tipo atual */
void adicionar_simbolo(char* nome) {
    strcpy(tabela[num_simbolos].nome, nome);
    strcpy(tabela[num_simbolos].tipo, tipo_atual);
    num_simbolos++;
}
%}

%%

"char"|"int"|"float"    {
                            strcpy(tipo_atual, yytext);
                            printf("TIPO(%s) ", yytext);
                        }

[a-zA-Z_][a-zA-Z0-9_]*  {
                            adicionar_simbolo(yytext);
                            printf("ID(%s) ", yytext);
                        }

","                     { printf("VIRG "); }
";"                     { printf("PV\n"); }

"//".*                  ; // Ignora o case até a quebra de linha

[ \t\n]                 ; /* Espaços, tabulações e quebras de linha são ignorados */

.                       { printf("\n[linha %d] ERRO LEXICO: '%s'\n", yylineno, yytext); }


%%

int main(void) {
    /* Inicia a análise léxica */
    yylex();

    /* Após ler todo o arquivo, imprime a Tabela de Símbolos */
    printf("\n\n--- TABELA DE SIMBOLOS ---\n");
    printf("%-20s | %-10s\n", "IDENTIFICADOR", "TIPO");
    printf("-----------------------------------\n");
    for(int i = 0; i < num_simbolos; i++) {
        printf("%-20s | %-10s\n", tabela[i].nome, tabela[i].tipo);
    }

    return 0;
}
