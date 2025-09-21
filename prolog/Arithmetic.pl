%% --------------------------------------------
%% 1.a  scum(N, Res)
%% Sum of integers 1..N (N >= 1).
%% --------------------------------------------
scum(N, Res) :-
    N > 0,
   Res is N * (N + 1) // 2.

%% --------------------------------------------
%% 1.b  sumDigits(Num, Sum)
%% Sum of decimal digits of a non-negative integer.
%% --------------------------------------------

sumDigits(Num, Sum) :-
    sumDigits_helper(Num, 0, Sum).

sumDigits_helper(0, Acc, Acc).
sumDigits_helper(Num, Acc, Sum) :-
    Num > 0,
    Digit is Num mod 10,
    RestNum is Num // 10,
    NewAcc is Acc + Digit,
    sumDigits_helper(RestNum, NewAcc, Sum).

%% --------------------------------------------
%% 2.a  split(N, Res)
%% Split a non-negative integer N into its digit list.
%% --------------------------------------------
split(0, [0]).
split(N, Res) :-
    N > 0,
    split_helper(N, [], Res).

split_helper(0, Acc, Acc).
split_helper(N, Acc, Res) :-
    N > 0,
    Digit is N mod 10,
    N1 is N // 10,
    split_helper(N1, [Digit|Acc], Res).

%% --------------------------------------------
%% 2.b  create(List, N)
%% Build an integer N from a list of digits where the LEFTMOST element
%% is the UNITS digit, the next is tens, etc.
%% Example: create([1,2,3,4], N) -> N = 4321.
%% --------------------------------------------
create([], 0).
create([H|T], N) :-
    create(T, N1),
    N is H + N1 * 10.
%% --------------------------------------------
%% 2.c  reverse_number(N, R)
%% Using split/2 and create/2: R is N with its digits reversed.
%% --------------------------------------------
reverse_number(N, R) :-
    N >= 0,
    split(N, Ds),
    create(Ds, R).

%% --------------------------------------------
%% 3.a  intersection(L1, L2, Z)
%% Set-style intersection.
% we use list_to_set to avoid duplicates
%% --------------------------------------------

intersection(L1, L2, Z) :-
    findall(X, (member(X, L1), member(X, L2)), T),
    list_to_set(T,Z).


%% --------------------------------------------
%% Exercise 3b: minus(L1, L2, Z) - Using built-ins
%% Find L1 - L2 (elements in L1 but not in L2) without duplicates
%% --------------------------------------------
minus(L1, L2, Z) :-
    findall(X, (member(X, L1), \+ member(X, L2)), T),
    list_to_set(T,Z).