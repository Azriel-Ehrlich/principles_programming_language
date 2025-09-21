/* =========================================================
   Family DB & Relations — SWI-Prolog
   NOTE: married(Male, Female) — male is 1st arg.
   ========================================================= */

% ----- Base facts -----
% Genders (grouped => no discontiguous warnings)
male(dov).
male(yaakov).
male(tzvi).
male(azriel).
male(yehuda).
male(emmanuel).
male(aryeh).
male(yehonatan).
male(yedidya).

female(rivka).
female(efrat).
female(orit).
female(avishag).
female(shira).
female(devorah).
female(yael).
female(esti).
female(hodaya).
female(elisheva).

% Marriages (Male first)
married(dov, rivka).
married(yaakov,     avishag).
married(tzvi, efrat).
married( emmanuel, devorah).
married(yehonatan,shira).

% Parent relations
parent(dov, yaakov).
parent(rivka, yaakov).
parent(dov, efrat).
parent(rivka, efrat).
parent(dov, orit).
parent(rivka, orit).

parent(yaakov, shira).
parent(avishag, shira).
parent(yaakov, azriel).
parent(avishag, azriel).

parent(efrat, devorah).
parent(tzvi, devorah).
parent(efrat, yael).
parent(tzvi, yael).
parent(efrat, yehuda).
parent(tzvi, yehuda).

parent(devorah, aryeh).
parent(emmanuel, aryeh).
parent(devorah, esti).
parent(emmanuel, esti).

parent(shira, hodaya).
parent(yehonatan, hodaya).
parent(shira, elisheva).
parent(yehonatan, elisheva).
parent(shira, yedidya).
parent(yehonatan, yedidya).

% ----- Helpers -----
spouse(X,Y) :- married(X,Y) ; married(Y,X).

% ----- Derived relations -----
father(F, C)    :- male(F),   parent(F, C).
mother(M, C)    :- female(M), parent(M, C).

son(S, P)       :- male(S),   parent(P, S).
daughter(D, P)  :- female(D), parent(P, D).

% siblings: share at least one parent, and are distinct
sibling(X, Y) :-
    X \= Y,
    parent(P, X),
    parent(P, Y).

brother(B, X)   :- male(B),   sibling(B, X).
sister(S, X)    :- female(S), sibling(S, X).

% grandparents & grandchildren
grandfather(GF, C)   :- male(GF),   parent(GF, P), parent(P, C).
grandmother(GM, C)   :- female(GM), parent(GM, P), parent(P, C).
grandson(GS, GP)     :- male(GS),   parent(P, GS), parent(GP, P).
granddaughter(GD, GP):- female(GD), parent(P, GD), parent(GP, P).

% ----- In-laws (סימטרי וחזק) -----
% Brother-in-law of X:
% (1) husband of X's sister
% (2) brother of X's spouse
% (3) husband of X's spouse's sister
brother_in_law(BIL, X) :-
    BIL \= X, male(BIL),
    spouse(BIL, Sis),
    sibling(Sis, X), female(Sis).
brother_in_law(BIL, X) :-
    BIL \= X,
    spouse(X, S),
    brother(BIL, S).
brother_in_law(BIL, X) :-
    BIL \= X, male(BIL),
    spouse(X, S),
    sibling(Sis, S), female(Sis),
    spouse(BIL, Sis).


% ----- Uncle by marriage (exclude any blood parent) -----
uncle_by_marriage(U, N) :-
    parent(P, N),
    brother_in_law(U, P),
    forall(parent(P2, N), \+ sibling(U, P2)).

% ----- Nieces & nephews -----
niece(Niece, X)  :- female(Niece), parent(Sib, Niece) , sibling(Sib, X).
nephew(Nephew, X):- male(Nephew), parent(Sib, Nephew),  sibling(Sib, X).

% ----- Cousins -----
cousins(X, Y) :-
    X \= Y,
    parent(PX, X),
    parent(PY, Y),
    sibling(PX, PY).

second_cousins(X, Y) :-
    X \= Y,
    parent(PX, X),
    parent(PY, Y),
    cousins(PX, PY).

% ----- ben_doda -----
ben_doda(X, Y) :-
    X \= Y,
    male(X),
    parent(PX, X),
    parent(PY, Y),
    sister(PX, PY).
