In this project I have implemented Part of Speech Tagger using Bigram Viterbi Algorithm. The program implements forward algorithm.

* Open Terminal
* Go to the project folder 
* Use following command: python ViterbiAlgorithm.py ../data/probs.txt ../data/sents.txt
Following is the sample output for the POS tagging of the sentence: mark has fish

PROCESSING SENTENCE: mark has fish

FINAL VITERBI NETWORK
P(mark=noun) = 0.0720000000
P(mark=verb) = 0.0060000000
P(mark=inf) = 0.0000000100
P(mark=prep) = 0.0000000100
P(has=noun) = 0.0000004620
P(has=verb) = 0.0014040000
P(has=inf) = 0.0000001320
P(has=prep) = 0.0000021600
P(fish=noun) = 0.0000864864
P(fish=verb) = 0.0000000210
P(fish=inf) = 0.0000000309
P(fish=prep) = 0.0000000351


FINAL BACKPTR NETWORK
P(has=noun) = verb
P(has=verb) = noun
P(has=inf) = verb
P(has=prep) = noun
P(fish=noun) = verb
P(fish=verb) = noun
P(fish=inf) = verb
P(fish=prep) = verb


BEST TAG SEQUENCE HAS PROBABILITY=0.0000432432
fish->noun
has->verb
mark->noun


FORWARD ALGORITHM RESULTS
P(mark=noun) = 0.0720000000
P(mark=verb) = 0.0060000000
P(mark=inf) = 0.0000000100
P(mark=prep) = 0.0000000100
P(has=noun) = 0.0000004627
P(has=verb) = 0.0014040182
P(has=inf) = 0.0000001327
P(has=prep) = 0.0000023100
P(fish=noun) = 0.0000866446
P(fish=verb) = 0.0000000379
P(fish=inf) = 0.0000000309
P(fish=prep) = 0.0000000351




