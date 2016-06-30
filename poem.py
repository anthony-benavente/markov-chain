#! /usr/bin python

import sys
import re
import pprint
import random

vertices = {} # list of vertex objects
totals = {}
p = re.compile("[\w']+|[,.!?]")
pp = pprint.PrettyPrinter()
punc = re.compile('[.!?]')

def usage():
    print "usage: python poem.py <input_file>"

def get_word_count(word_list):
    words = {}
    for word in word_list:
        if word not in words:
            words[word] = 0
        words[word] += 1
    return words.iteritems() 

def weighted_choice(choices):
    choices = [(i, j) for i, j in choices.iteritems()]
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w

def main(argv):
    if len(argv) == 0:
        usage()
        return 1
    else:
        input = argv[0]
        with open(input) as fp:
            text = ' '.join(map(lambda x: x.strip(), fp.readlines()))
            words = p.findall(text)
            for i in range(len(words)):
                current_word = words[i].lower()
                if (i + 1) < len(words): 
                    if current_word not in vertices:
                        vertices[current_word] = []
                    vertices[current_word].append(words[i + 1].lower())

        for vertex in vertices:
            vertices[vertex] = { word: count for (word, count) in get_word_count(vertices[vertex])}

        for vertex in vertices:
            current_count = 0
            for word, count in vertices[vertex].iteritems():
                current_count = current_count + count
            totals[vertex] = current_count

        for vertex in vertices:
            for word in vertices[vertex]:
                vertices[vertex][word] = vertices[vertex][word] / float(totals[vertex])

        start = random.choice(vertices.keys())
        result = start
        printed = False
        for i in range(150):
            next = weighted_choice(vertices[start])
            start = next
            result += ' ' + next
            printed = False
            if punc.findall(next):
                print result.title()
                result = ''
                printed = True
        if not printed:
            print result.title()

if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else [])