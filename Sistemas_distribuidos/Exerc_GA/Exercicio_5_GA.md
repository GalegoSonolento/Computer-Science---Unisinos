1) Escreva o passo a passo de Alice-Bob para implementarmos o seguinte statement:
   - Bob gostaria de enviar seu documento assinado com criptografia assimétrica para Alice
(Partindo do fato que o request é o documento estar assinado e com criptografia na rede).
- Bob:
  - Cria seu par de chave;
  - Pega a chave de Alice;
  - Envia sua chave pública a Alice;
  - Monta o Hash do documento com a chave privada de Bob;
  - Lança na rede com a chave pública de Alice;
- Alice:
  - Cria seu par de chave;
  - Envia sua chave pública para Bob;
  - Recebe a cave pública de Bob;
  - Recebe o documento criptografado de Bob;
  - Decripta com sua chave privada;
  - Remonta o Hash da assinatura com a chave pública de Bob.