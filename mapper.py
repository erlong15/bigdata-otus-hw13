# -*- coding: utf-8 -*-
import sys
#from nltk.tokenize import sent_tokenize
import string
from collections import defaultdict

import re
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

def to_pair(sent, pairs):
    words = [word.strip(string.punctuation) for word in sent.split()]
    idx_pair = {}
    for idx, word in enumerate(words):
        for idx2, word2 in enumerate(words):
            idx_key = tuple(sorted([idx, idx2]))
            if idx != idx2 and idx_key not in idx_pair \
                and bool(re.match('^[a-zA-Z0-9]+$', word)) \
                and bool(re.match('^[a-zA-Z0-9]+$', word2)):
                    idx_pair[idx_key] = 1
                    pairs[' '.join(sorted([word.lower(), word2.lower()]))] += 1


def main():
    text = sys.stdin.read()
    sent_tokenize_list = split_into_sentences(text)
    pairs = defaultdict(int)
    for sent in sent_tokenize_list:
        to_pair(sent, pairs)
    for pair, val in pairs.items():
        print('{}\t{}'.format(pair, val))


if __name__ == '__main__':
    main()

