import sys
from nltk.tokenize import sent_tokenize
import string
from collections import defaultdict


def to_pair(sent, pairs):
    words = [word.strip(string.punctuation) for word in sent.split()]
    idx_pair = {}
    for idx, word in enumerate(words):
        for idx2, word2 in enumerate(words):
            idx_key = tuple(sorted([idx, idx2]))
            if idx != idx2 and idx_key not in idx_pair:
                idx_pair[idx_key] = 1
                pairs[' '.join(sorted([word.lower(), word2.lower()]))] += 1


def main():
    text = sys.stdin.read()
    sent_tokenize_list = sent_tokenize(text)
    pairs = defaultdict(int)
    for sent in sent_tokenize_list:
        to_pair(sent, pairs)
    for pair, val in pairs.items():
        print('{}\t{}'.format(pair, val))


if __name__ == '__main__':
    main()

