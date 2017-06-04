In this project I have implemented sentiment analyzer using term frequency based Naïve Bayes classifier, binarized Naïve Bayes and Perceptron.
It can classify documents based on the sentiments ‘positive’ or ‘negative’. I could achieve following results.

* Naïve Bayes:
  * Frequency Based(With Stop Words): Average Accuracy:0.8165
  * Frequency Based(Without Stop Words): Average Accuracy:0.8110

* Binarized Naïve Bayes: Average Accuracy:0.7385

* Perceptron
  * #of Iterations 1: Average Accuracy:0.6265
  * #of iterations 50: Average Accuracy:0.823
  
 
To run the project:
 
* Open Terminal
*	Go to the project folder
*	   Use following commands: 
  * For Naive Bayes
    * python NaiveBayes.py ../data/imdb1
  * For Naive Bayes without using stop words
    * python NaiveBayes.py -f ../data/imdb1
  * For Binarized Naive Bayes 
    * python NaiveBayes.py -b ../data/imdb1
  * For Perceptron
    * python Perceptron.py ../data/imdb1/ 50


