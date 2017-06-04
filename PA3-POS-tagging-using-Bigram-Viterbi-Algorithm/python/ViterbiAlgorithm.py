import sys
import getopt
import os
import math
import operator
import collections


def tree():
    return collections.defaultdict(tree)


class ViterbiAlgorithm:
    def __init__(self):
        """ViterbiAlgorithm initialization"""
    q = tree()
    e = tree()


def tagSentences(self, sentences_path):
    f = open(sentences_path, 'r')
    tags= ["noun", "verb", "inf", "prep"]
    for line in f:

        print("\n")
        print("PROCESSING SENTENCE: "+line)
        line = line.lower()
        pi=tree()
        forwardPi=tree()
        tempPi=tree()

        backpntr=tree()
        words= line.split()
        pi[0]["phi"]=1
        for tag in tags:
            if words[0] not in self.e.keys():
                self.e[words[0]][tag]=0.0001
            if tag not in self.e[words[0]].keys():
                    self.e[words[0]][tag] = 0.0001
            if "phi" not in self.q[tag].keys():
                self.q[tag]["phi"]=0.0001
            pi[1][tag]=pi[0]["phi"]*float(self.q[tag]["phi"])*float(self.e[words[0]][tag])
            forwardPi[1][tag]=pi[1][tag]
            backpntr[1][tag] =["phi", pi[1][tag]]

        for k in range(2,len(words)+1):
            for tag in tags:
                listPi = []
                listForwardPi=[]
                for tag2 in tags:

                    if words[k-1] not in self.e.keys():
                        self.e[words[k-1]][tag] = 0.0001
                    if tag not in self.e[words[k-1]].keys():
                        self.e[words[k-1]][tag] = 0.0001
                    if tag not in self.q.keys():
                        self.q[tag][tag2] = 0.0001
                    if tag2 not in self.q[tag].keys():
                        self.q[tag][tag2]=0.0001
                    tempPi = pi[k-1][tag2] * self.q[tag][tag2] * self.e[words[k-1]][tag]
                    tempPiForward= forwardPi[k-1][tag2] * self.q[tag][tag2] * self.e[words[k-1]][tag]
                    listPi.append((tag2,tempPi))
                    listForwardPi.append((tag2,tempPiForward))
                sum=0
                for pi_value in listForwardPi:
                    sum += float(pi_value[1])
                forwardPi[k][tag] = sum

                piMax=float('-inf')
                for pi_value in listPi:
                    if pi_value[1]>piMax:
                        piMax = float(pi_value[1])
                        pi[k][tag] = piMax
                        backpntr[k][tag]= [pi_value[0], pi_value[1]]


        listPi = []
        tempPi=0.0
        for tag in tags:
            if "fin" not in self.q.keys():
                self.q["fin"][tag] = 0.0001
            if tag not in self.q["fin"].keys():
                    self.q["fin"][tag] = 0.0001
            tempPi= pi[len(words)][tag] * float(self.q["fin"][tag])
            listPi.append((tag, tempPi))
        piMax = float('-inf')
        for pi_value in listPi:
            if pi_value[1] > piMax:
                piMax=float(pi_value[1])
                pi[len(words)]["fin"] = float(pi_value[1])
                backpntr[len(words)+1]["fin"] = [pi_value[0], pi_value[1]]

        printValues(words,pi,backpntr, forwardPi)






def printValues(words,pi, backpntr, forwardPi):
    tags = ["noun", "verb", "inf", "prep"]
    print("FINAL VITERBI NETWORK")
    for  k, v in pi.items():
        values=v.items()
        for tag in tags:
            for value in v.items():
                if k==0 or tag[0]=="fin":
                    continue
                if tag==value[0]:
                    print("P(" + words[k-1] + "=" + value[0] + ") = "+ "%0.10f" %value[1])
                    break
    print("\n")
    print("FINAL BACKPTR NETWORK")
    for  k, v in backpntr.items():
        if k==len(words)+1 or k==1:
            continue
        for tag in tags:
            for value in v.items():
                if value[0]==tag:
                    print("P(" + words[k-1] + "=" + value[0] + ") = "+ value[1][0] )
                    break
    print("\n")
    print("BEST TAG SEQUENCE HAS PROBABILITY="+ "%0.10f" %backpntr[len(words)+1]["fin"][1])
    prev = "fin"
    final_prob = 1
    for k in range(len(words)+1, 1, -1):
        print (words[k-2]+"->"+backpntr[k][prev][0])
        prev = backpntr[k][prev][0]

    print("\n")
    print("FORWARD ALGORITHM RESULTS")
    tags = ["noun", "verb", "inf", "prep"]
    for  k, v in forwardPi.items():
        if k==0:
            continue
        for tag in tags:
            for value in v.items():
                if tag==value[0]:
                    print("P(" + words[k-1] + "=" + value[0] + ") = "+ "%0.10f" %value[1])
                    break
    print("\n")


def prepareProbabilities(self,probabilty_data_path):
    f = open(probabilty_data_path, 'r')
    for line in f:
        line= line.lower()
        words=line.split()
        if words[0] in ["noun", "phi", "verb", "fin", "prep", "inf"]:
            self.q[words[0]][words[1]]=float(words[2])
        else:
            self.e[words[0]][words[1]] = float(words[2])






def main(self,probabilty_data_path, sentences_path):
    prepareProbabilities(self,probabilty_data_path)
    tagSentences(self,sentences_path)


if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print 'usage:\tViterbiAlgorithm <probabilities file> <sentences file>'
        sys.exit(0)
    object = ViterbiAlgorithm()
    main(object, sys.argv[1], sys.argv[2])
