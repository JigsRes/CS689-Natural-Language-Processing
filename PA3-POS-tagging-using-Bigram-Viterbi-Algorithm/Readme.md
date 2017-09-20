In this project I have implemented Part of Speech Tagger using Bigram Viterbi Algorithm. The program implements forward algorithm.

* Open Terminal
* Go to the project folder 
* Use following command: python ViterbiAlgorithm.py ../data/probs.txt ../data/sents.txt
Following is the sample output for the POS tagging of the sentence: mark has fish

PROCESSING SENTENCE: mark has fish

FINAL VITERBI NETWORK <br />
P(mark=noun) = 0.0720000000 <br />
P(mark=verb) = 0.0060000000 <br />
P(mark=inf) = 0.0000000100 <br />
P(mark=prep) = 0.0000000100 <br />
P(has=noun) = 0.0000004620 <br />
P(has=verb) = 0.0014040000 <br />
P(has=inf) = 0.0000001320 <br />
P(has=prep) = 0.0000021600 <br />
P(fish=noun) = 0.0000864864 <br />
P(fish=verb) = 0.0000000210 <br />
P(fish=inf) = 0.0000000309 <br />
P(fish=prep) = 0.0000000351 <br />


FINAL BACKPTR NETWORK <br />
P(has=noun) = verb <br />
P(has=verb) = noun <br />
P(has=inf) = verb<br />
P(has=prep) = noun<br />
P(fish=noun) = verb<br />
P(fish=verb) = noun<br />
P(fish=inf) = verb<br />
P(fish=prep) = verb<br />


BEST TAG SEQUENCE HAS PROBABILITY=0.0000432432<br />
fish->noun<br />
has->verb<br />
mark->noun<br />


FORWARD ALGORITHM RESULTS<br />
P(mark=noun) = 0.0720000000<br />
P(mark=verb) = 0.0060000000<br />
P(mark=inf) = 0.0000000100<br />
P(mark=prep) = 0.0000000100<br />
P(has=noun) = 0.0000004627<br />
P(has=verb) = 0.0014040182<br />
P(has=inf) = 0.0000001327<br />
P(has=prep) = 0.0000023100<br />
P(fish=noun) = 0.0000866446<br />
P(fish=verb) = 0.0000000379<br />
P(fish=inf) = 0.0000000309<br />
P(fish=prep) = 0.0000000351<br />




