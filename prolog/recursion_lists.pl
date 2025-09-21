%% --------------------------------------------
%% Exercise 1: reverse(L, Z)
%% Tail-recursive reverse using an accumulator.
%% --------------------------------------------
rev([],Z,Z).
rev([H|T],Acc,Z):-
    rev(T,[H|Acc],Z).
reverse(L,Z):- rev(L,[],Z).
    
%% --------------------------------------------
%% Exercise 2: member(X, L)
%% True iff X is an element of list L.
%% ---------------------------------------------
    
member(X,[X|_]).
member(X,[_|T]):-
    member(X,T).

%% --------------------------------------------
%% Exercise 3: palindrome(L)
%% A list is a palindrome if it equals its reverse.
%% --------------------------------------------
palindrome(L):-
    reverse(L, R),
    L=R.

%% --------------------------------------------
%% Exercise 4: sorted(L)
%% check if a list is sorted in Non-decreasing order
%% --------------------------------------------
sorted(_, []).
sorted(X, [Y|T]):-
    X=<Y,
    sorted(Y,T).
sorted([X|T]):-
    sorted(X,T).

%% --------------------------------------------
%% Exercise 5: permutation(L, P)
%% Generate all permutations P of list L by selecting
%% one element as head and permuting the rest.
%% --------------------------------------------
permutation([], []).
permutation(L, [H|T]) :-
    select_one(H, L, R),
    permutation(R, T).

% helper: remove one occurrence of X from a list
select_one(X, [X|T], T).
select_one(X, [H|T], [H|R]) :-
    select_one(X, T, R).