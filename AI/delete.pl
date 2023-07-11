delete(X,[X|Tail],Tail).
delete(X,[Y|Tail],[Y|Tail1]):-
delete(X,Tail,Tail1).