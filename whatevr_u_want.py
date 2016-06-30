#! /usr/bin python

import sys
import re
import pprint

vertices = {} # list of vertex objects
p = re.compile("[\s,.!?'\"]+")

def usage():
    print "usage: python poem.py <input_file>"


def get_word_count(word_list):
    words = {}
    for word in word_list:
        if word not in words:
            words[word] = 0
        words[word] += 1
    return words.iteritems() '[(word, 1), (other, 4), (test, 3)]'

def main(argv):
    if len(argv) == 0:
        usage()
        return 1
    else:
        input = argv[0]
        with open(input) as fp:
            text = ' '.join(map(lambda x: x.strip(), fp.readlines()))
            words = p.split(text)
            for i in range(len(words)):
                current_word = words[i].lower()
                if (i + 1) < len(words): 
                    if current_word not in vertices:
                        vertices[current_word] = []
                    vertices[current_word].append(words[i + 1])
        for vertex in vertices:
            vertices[vertex] = { word: count for (word, count) in get_word_count(vertices[vertex])}
            
            # Literal translation of dictionary comprehension above ^^
            # ---
            # vertices[vertex] = {}
            # word_count_list = get_word_count(vertices[vertex])
            # for word, count in word_count_list:
            #     vertices[vertex][word] = count

        # Use python library to print out dictionary nicely
        pp = pprint.PrettyPrinter()
        pp.pprint(vertices)


if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else [])