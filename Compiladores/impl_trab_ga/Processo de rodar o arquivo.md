Tenha todos os arquivos desse zip numa mesma pasta.

Tenha o flex instalado dentro da máquina - à depender o sistema operacional o processo pode ser diferente - grosso modo, o comando de instalação do CachyOS é:
sudo pacman -Syu flex

Rode, nessa sequência:

flex -o lexico.c lexico.l
gcc lexico.c -o lexico
./lexico < teste1.txt
./lexico < text2.txt
...