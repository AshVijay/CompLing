:- ['bigram_ashwinvi.pl'].
:- ['unigram_ashwinvi.pl'].

value=18524 .

calc_prob(ListOfWords,SmoothedLog10Probability):-
  calc_prob(ListOfWords,0,SmoothedLog10Probability).


calc_prob([_],N,N).
calc_prob([W1,W2|L], P  , Result ) :-
  bigram(X,W1,W2),
  unigram(Y,W1),
  P is log10((X+1)/(Y+value)),  calc_prob( [W2|L], P , Result ).