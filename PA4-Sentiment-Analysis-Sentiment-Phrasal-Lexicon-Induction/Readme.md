In this project I have implemented sentiment analyzer using Sentiment-Phrasal-Lexicon-Induction.
This is based on Turney, Peter D. 2002. “Thumbs Up or Thumbs Down? Semantic Orientation Applied to Unsupervised Classification of Reviews.” Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics (ACL).
It can classify documents based on the sentiments ‘positive’ or ‘negative’. I could achieve following results.

* Nearness limit: 10, Phrase Polarity Count Threshold: 4
    * Accuracy: 0.523000
* Nearness limit: 15, Phrase Polarity Count Threshold: 4
    * Accuracy: 0.531500
    
 To run the project:
 * Go to project folder
    * For 10-cross validation use: python SetimentAnalyzer..py ..\tagged_data
    * For testing use: python SetimentAnalyzer..py ..\tagged_data ..\tagged_data_test
