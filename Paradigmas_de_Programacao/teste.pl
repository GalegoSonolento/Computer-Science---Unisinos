% Predicado que verifica se um elemento está presente em uma lista.
estaNaLista(X, [X|_]).
estaNaLista(X, [_|L]) :- estaNaLista(X, L).

% Predicado que inverte uma lista.
inverter([], []).
inverter([X|L], R) :- inverter(L, Y), append(Y, [X], R).

% Predicado que remove duplicatas de uma lista.
removerDuplicatas([], []).
removerDuplicatas([X|L], R) :- estaNaLista(X, L), removerDuplicatas(L, R).
removerDuplicatas([X|L], [X|R]) :- \+ estaNaLista(X, L), removerDuplicatas(L, R).

s