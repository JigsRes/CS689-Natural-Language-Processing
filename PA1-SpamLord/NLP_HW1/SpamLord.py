import sys
import os
import re
import pprint

#my_fourth_pat = '([\w|-]+)@([\w|-]+)*.-e-d-u'
#my_pat_small = '([\w|-]+)\s*(?:[\s][aA][tT][\s]|@|&#x40;|WHERE|where)\s*([\w|-]+)\s*(?:[\s][dD][oO][tT][\s]|\.|;|[\s][dD][oO][mM][\s])\s*-*[eE]-*[dD]-*[uU]
#my_pat_big = '([\w|-]+)\s*(?:[\s][aA][tT][\s]|@|&#x40;|WHERE|where)\s*([\w|-]+)\s*(?:[\s][dD][oO][tT]|\.|;|[\s][dD][oO][mM][\s])\s*([\w|-]+)\s*(?:[\s][dD][oO][tT]|\.|;|[\s][dD][oO][mM][\s])\s*-*[eE]-*[dD]-*[uU]'
my_pat_small='([\w|-]+)(?:(?:[\(\{\s]+(?:[aA][tT]|WHERE|where)[\)\}\s]+)|(?:[\(\{\s]*(?:@|&#x40;)[\)\}\s]*))([\w|-]+)(?:(?:[\(\{\s]+(?:[dD][oO][tT]|[dD][oO][mM])[\)\}\s]+)|(?:[\(\{\s]*(?:\.|;)[\)\}\s]*))-*[eE]-*[dD]-*[uU]'
my_pat_big="([\w|-]+)(?:(?:[\(\{\s]+(?:[aA][tT]|WHERE|where)[\)\}\s]+)|(?:[\(\{\s]*(?:@|&#x40;)[\)\}\s]*))([\w|-]+)(?:(?:[\(\{\s]+(?:[dD][oO][tT]|[dD][oO][mM])[\)\}\s]+)|(?:[\(\{\s]*(?:\.|;)[\)\}\s]*))([\w|-]+)(?:(?:[\(\{\s]+(?:[dD][oO][tT]|[dD][oO][mM])[\)\}\s]+)|(?:[\(\{\s]*(?:\.|;)[\)\}\s]*))-*[eE]-*[dD]-*[uU]"
obfuscate_pattern="obfuscate\s*[\(]\s*['](.+)[']\s*[\,]\s*['](.+)[']s*[\)]"
my_phone_pat3 = '(?:\D|^)[\(\{]*([\d][\d][\d])[\)\}]*(?:\s|-|&thinsp;)*([\d][\d][\d])(?:\s|-|&thinsp;)+([\d][\d][\d][\d])'

"""
TODO
This function takes in a filename along with the file object (actually
a StringIO object) and
scans its contents against regex patterns. It returns a list of
(filename, type, value) tuples where type is either an 'e' or a 'p'
for e-mail or phone, and value is the formatted phone number or e-mail.
The canonical formats are:
     (name, 'p', '###-###-#####')
     (name, 'e', 'someone@something')
If the numbers you submit are formatted differently they will not
match the gold answers

NOTE: ***don't change this interface***

NOTE: You shouldn't need to worry about this, but just so you know, the
'f' parameter below will be of type StringIO. So, make
sure you check the StringIO interface if you do anything really tricky,
though StringIO should support most everything.
"""


def process_file(name, f):
    # note that debug info should be printed to stderr
    # sys.stderr.write('[process_file]\tprocessing file: %s\n' % (path))
    res = []
    for line in f:
        match_small = re.findall(my_pat_small, line, re.I | re.M)
        match_big = re.findall(my_pat_big, line, re.I | re.M)
        #matches4 = re.findall(my_fourth_pat, line, re.I | re.M)
        match_obfuscate = re.findall(obfuscate_pattern,line, re.I|re.M)

        for z in match_obfuscate:
            print z
            email='%s@%s' % (z[1],z[0])
            email = email.replace("-", "")
            email = email.replace(" ", "")
            res.append((name, 'e', email))

        for m in match_small:
            if re.match('[sS][eE][rR][vV][eE][rR]',m[0]):
                break
            email = '%s@%s.edu' % m
            email = email.replace("-", "")
            email = email.replace(" ", "")
            res.append((name, 'e', email))

        '''for d in matches4:
            if re.match('[sS][eE][rR][vV][eE][rR]',d[0]):
                break
            email = '%s@%s.edu' % d
            email = email.replace("-", "")
            email=email.replace(" ","")
            res.append((name, 'e', email))'''

        for c in match_big:
            if re.match('[sS][eE][rR][vV][eE][rR]',c[0]):
                break
            email = '%s@%s.%s.edu' % c
            email = email.replace("-", "")
            email = email.replace(" ", "")
            res.append((name, 'e', email))

        phone_match3 = re.findall(my_phone_pat3, line, re.I | re.M)

        for q in phone_match3:
            phone = '%s-%s-%s' % q
            res.append((name, 'p', phone))
    return res


"""
You should not need to edit this function, nor should you alter
its interface
"""


def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path, fname)
        f = open(path, 'r')
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list


"""
You should not need to edit this function.
Given a path to a tsv file of gold e-mails and phone numbers
this function returns a list of tuples of the canonical form:
(filename, type, value)
"""


def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path, 'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list


"""
You should not need to edit this function.
Given a list of guessed contacts and gold contacts, this function
computes the intersection and set differences, to compute the true
positives, false positives and false negatives.  Importantly, it
converts all of the values to lower case before comparing
"""


def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    # print 'Guesses (%d): ' % len(guess_set)
    # pp.pprint(guess_set)
    # print 'Gold (%d): ' % len(gold_set)
    # pp.pprint(gold_set)
    print 'True Positives (%d): ' % len(tp)
    pp.pprint(tp)
    print 'False Positives (%d): ' % len(fp)
    pp.pprint(fp)
    print 'False Negatives (%d): ' % len(fn)
    pp.pprint(fn)
    print 'Summary: tp=%d, fp=%d, fn=%d' % (len(tp), len(fp), len(fn))


"""
You should not need to edit this function.
It takes in the string path to the data directory and the
gold file
"""


def main(data_path, gold_path):
    guess_list = process_dir(data_path)
    gold_list = get_gold(gold_path)
    score(guess_list, gold_list)


"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print 'usage:\tSpamLord.py <data_dir> <gold_file>'
        sys.exit(0)
    main(sys.argv[1], sys.argv[2])
