%option noyywrap yylineno
%%
"char"|"int"|"float"	{ printf("TIPO(%s) ", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*	{ printf("ID(%s) ", yytext); }
[0-9]+	{ printf("NUM(%s) ", yytext); }
","	{ printf("VIRG "); }
";"	{ printf("PV\n"); }

[ \t\n]	;

.	{ printf("\n[linha %d] ERRO LEXICO", yylineno); }

%%
int main(void) { yylex(); return 0; }
