```links
- https://asavbrm-my.sharepoint.com/my?id=%2Fpersonal%2Fhaaghenrique%5Fedu%5Funisinos%5Fbr%2FDocuments%2FDocumentos%20unisinos%2FArtigos%5FTCC%2FDas%5Fondas%5Fmilimetricas&viewid=572a3bd2%2D4a5b%2D445f%2D897a%2D155cd725a999
- https://www.overleaf.com/project/6a29e2b5bd3997bf4852632f
- https://grok.com/c/9b7c46ca-c6e6-4872-a8ba-163ba3dba3a3?rid=aa7eca8f-2825-4420-a0dd-9bf12caf624e
- https://claude.ai/chat/f6cfe233-2f5d-488b-9bce-482aa2cd6076
- https://notebook.google.com/notebook/131067bc-a503-4304-96b7-f4c99acee15d
```

Negócio é o seguinte, preciso de alguma ajuda aqui pra encontrar bons chipsets ao invés dos da Texas INstruments

No momento temos essas opções:
https://www.ti.com/product/IWR6843ISK/part-details/IWR6843ISK
![[Pasted image 20260808120755.png]]
https://www.ti.com/tool/IWR1642BOOST
![[Pasted image 20260808120807.png]]

Lembrar dessa reply do Claude aqui:
```
**Um ponto de arquitetura que vale explorar como diferencial do seu TCC:** nem o IWR6843ISK nem o IWR1642BOOST são "um único transceptor" como no MMWCSAR original de 2017 — eles já trazem um array MIMO (3 Tx × 4 Rx) embarcado. Isso significa que, ao montar a placa numa plataforma giratória, você ganha **dois mecanismos de resolução ao mesmo tempo**: a abertura sintética do movimento circular (como no MMWCSAR) _e_ a resolução angular do array físico via MUSIC (como no mmID) — algo que nenhum dos dois papers testou isoladamente. Isso é um argumento de originalidade genuíno para a introdução do seu TCC, não só "juntei os dois papers".
```
Isso aqui vai ser bastante útil mais pra frente.

Os dois papers mais usados serão os mmID-High-Resolution_mmWave_Imaging_for_Human_Identification.pdf e 3D_Imaging_Milimeter_Wave_Circular_Synthetic_Aperture_Radar.pdf (que não posso colocar no repo por motivos óbvios).

