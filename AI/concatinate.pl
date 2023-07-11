concatinate([],L,L).
concatinate([X|L1],L2,[X|L3]):-
concatinate(L1,L2,L3).