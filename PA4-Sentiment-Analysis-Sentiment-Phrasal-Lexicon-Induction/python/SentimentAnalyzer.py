import sys
import os
import math
import re

class SentimentAnalyzer:
    class TrainSplit:
        """Represents a set of training/testing data. self.train is a list of Examples, as is self.test.
        """

        def __init__(self):
            self.train = []
            self.test = []

    class Example:
        """Represents a document with a label. klass is 'pos' or 'neg' by convention.
           words is a list of strings.
        """

        def __init__(self):
            self.klass = ''
            self.words = []

    def __init__(self):
        """SentimentAnalyzer initialization"""
        self.stopList = set(self.readFile('../data/english.stop'))
        self.numFolds = 10
        self.pos_phrase_hit={}
        self.neg_phrase_hit={}
        self.great_count=0.0
        self.poor_count=0.0
        self.pattern1 = re.compile("JJ\d* NN[S]?\d* ")
        self.pattern2 = re.compile("RB[S]?[R]?\d* JJ\d* (?![NN][S]?)")
        self.pattern3 = re.compile("JJ\d* JJ\d* (?![NN][S]?)")
        self.pattern4 = re.compile("NN[S]?\d* JJ\d* (?![NN][S]?)")
        self.pattern5 = re.compile("RB[R]?[S]?\d* VB[D]?[N]?[G]?\d* ")
        self.index_pattern= re.compile("(\d+)")
        self.great="great"
        self.poor="poor"
        self.phrase_polarity={}


    #############################################################################
    # TODO TODO TODO TODO TODO
    # Implement the Multinomial Naive Bayes classifier and the Naive Bayes Classifier with
    # Boolean (Binarized) features.
    # If the BOOLEAN_NB flag is true, your methods must implement Boolean (Binarized)
    # Naive Bayes (that relies on feature presence/absence) instead of the usual algorithm
    # that relies on feature counts.
    #
    ###


    def classify(self, words):
        word_list = []
        pos_tag_list = []
        i = 0
        for word in words:
            word_split = word.split('_')
            org_word = word_split[0]
            word_list.append(org_word)
            pos_tag_list.append(word_split[1] + str(i))
            i += 1

        pos_tag_string = ' '.join(pos_tag_list)
        matched_patterns = []
        matched_patterns.extend(self.pattern1.findall(pos_tag_string))
        matched_patterns.extend(self.pattern2.findall(pos_tag_string))
        matched_patterns.extend(self.pattern3.findall(pos_tag_string))
        matched_patterns.extend(self.pattern4.findall(pos_tag_string))
        matched_patterns.extend(self.pattern5.findall(pos_tag_string))

        pol=0
        for match in matched_patterns:
            pattern_parts=match.split(' ')
            index=self.index_pattern.findall(pattern_parts[0])
            phrase_index=int(index[0])
            phrase=word_list[phrase_index]+" "+word_list[phrase_index+1]
            pol+=self.phrase_polarity.get(phrase,0)

        guess = 'pos' if pol > 0 else 'neg'
        return guess

    def processPhrasePolarity(self):
        for phrase in self.pos_phrase_hit.keys():
            if self.pos_phrase_hit[phrase]<4 and self.neg_phrase_hit[phrase]<4:
                continue
            self.phrase_polarity[phrase]= math.log(self.pos_phrase_hit[phrase]*self.poor_count,2)-math.log(self.neg_phrase_hit[phrase]*self.great_count,2)




    def addExample(self, klass, words):
        def getNear(limit, i, phrase_type):
            count=0.01
            length=len(word_list)
            extreme_left=0 if i-limit <0 else i-limit
            extreme_right=length if i+limit+2>length else i+limit+2
            start_right=length-1 if i+2>length-1 else i+2
            for j in range(extreme_left, i):
                if word_list[j]==phrase_type:
                    count+=1.0
            for j in range(start_right,extreme_right):
                if word_list[j]==phrase_type:
                    count += 1.0
            return count

        word_list=[]
        pos_tag_list=[]
        i=0
        for word in words:
            word_split=word.split('_')
            org_word=word_split[0]
            word_list.append(org_word)
            if org_word==self.great:
                self.great_count+=1
            elif org_word==self.poor:
                self.poor_count+=1
            pos_tag_list.append(word_split[1]+str(i))
            i+=1
        pos_tag_string= ' '.join(pos_tag_list)
        #print pos_tag_string
        matched_patterns=[]
        matched_patterns.extend(self.pattern1.findall(pos_tag_string))
        matched_patterns.extend(self.pattern2.findall(pos_tag_string))
        matched_patterns.extend(self.pattern3.findall(pos_tag_string))
        matched_patterns.extend(self.pattern4.findall(pos_tag_string))
        matched_patterns.extend(self.pattern5.findall(pos_tag_string))


        for match in matched_patterns:
            pattern_parts=match.split(' ')
            index=self.index_pattern.findall(pattern_parts[0])
            phrase_index=int(index[0])
            phrase=word_list[phrase_index]+" "+word_list[phrase_index+1]
            self.pos_phrase_hit[phrase]= self.pos_phrase_hit.get(phrase, 0.0)+ getNear(12,phrase_index,self.great)
            self.neg_phrase_hit[phrase] = self.neg_phrase_hit.get(phrase, 0.0) + getNear(12,phrase_index, self.poor)






    # END TODO (Modify code beyond here with caution)
    #############################################################################


    def readFile(self, fileName):
        """
         * Code for reading a file.  you probably don't want to modify anything here,
         * unless you don't like the way we segment files.
        """
        contents = []
        f = open(fileName)
        for line in f:
            contents.append(line)
        f.close()
        result = self.segmentWords('\n'.join(contents))
        return result

    def segmentWords(self, s):
        """
         * Splits lines on whitespace for file reading
        """
        return s.split()

    def trainSplit(self, trainDir):
        """Takes in a trainDir, returns one TrainSplit with train set."""
        split = self.TrainSplit()
        posTrainFileNames = os.listdir('%s/pos/' % trainDir)
        negTrainFileNames = os.listdir('%s/neg/' % trainDir)
        for fileName in posTrainFileNames:
            example = self.Example()
            example.words = self.readFile('%s/pos/%s' % (trainDir, fileName))
            example.klass = 'pos'
            split.train.append(example)
        for fileName in negTrainFileNames:
            example = self.Example()
            example.words = self.readFile('%s/neg/%s' % (trainDir, fileName))
            example.klass = 'neg'
            split.train.append(example)
        return split

    def train(self, split):
        for example in split.train:
            words = example.words
            self.addExample(example.klass, words)

    def crossValidationSplits(self, trainDir):
        """Returns a lsit of TrainSplits corresponding to the cross validation splits."""
        splits = []
        posTrainFileNames = os.listdir('%s/pos/' % trainDir)
        negTrainFileNames = os.listdir('%s/neg/' % trainDir)
        # for fileName in trainFileNames:
        for fold in range(0, self.numFolds):
            split = self.TrainSplit()
            for fileName in posTrainFileNames:
                example = self.Example()
                example.words = self.readFile('%s/pos/%s' % (trainDir, fileName))
                example.klass = 'pos'
                if fileName[2] == str(fold):
                    split.test.append(example)
                else:
                    split.train.append(example)
            for fileName in negTrainFileNames:
                example = self.Example()
                example.words = self.readFile('%s/neg/%s' % (trainDir, fileName))
                example.klass = 'neg'
                if fileName[2] == str(fold):
                    split.test.append(example)
                else:
                    split.train.append(example)
            splits.append(split)
        return splits

    def filterStopWords(self, words):
        """Filters stop words."""
        filtered = []
        for word in words:
            if not word in self.stopList and word.strip() != '':
                filtered.append(word)
        return filtered


def test10Fold(args):
    nb = SentimentAnalyzer()
    splits = nb.crossValidationSplits(args[0])
    avgAccuracy = 0.0
    fold = 0
    for split in splits:
        classifier = SentimentAnalyzer()
        accuracy = 0.0
        for example in split.train:
            words = example.words
            classifier.addExample(example.klass, words)

        classifier.processPhrasePolarity()

        for example in split.test:
            words = example.words
            guess = classifier.classify(words)
            if example.klass == guess:
                accuracy += 1.0

        #print(accuracy, len(split.test))

        accuracy = accuracy / len(split.test)
        avgAccuracy += accuracy
        print '[INFO]\tFold %d Accuracy: %f' % (fold, accuracy)
        fold += 1
    avgAccuracy = avgAccuracy / fold
    print '[INFO]\tAccuracy: %f' % avgAccuracy


def classifyDir( trainDir, testDir):
    classifier = SentimentAnalyzer()
    trainSplit = classifier.trainSplit(trainDir)
    classifier.train(trainSplit)
    testSplit = classifier.trainSplit(testDir)
    accuracy = 0.0

    classifier.processPhrasePolarity()

    for example in testSplit.train:
        words = example.words
        guess = classifier.classify(words)
        if example.klass == guess:
            accuracy += 1.0
    accuracy = accuracy / len(testSplit.train)
    print '[INFO]\tAccuracy: %f' % accuracy


def main():
    args=sys.argv[1:]

    if len(args) == 2:
        classifyDir( args[0], args[1])
    elif len(args) == 1:
        test10Fold(args)


if __name__ == "__main__":
    main()
