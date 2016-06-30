#! /usr/bin python

import sys


class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = {}
    
    def __str__(self):
        return 'Vertex{key=%s}' % self.key

    def __utf8__(self):
        return self.__str__()


vertices = {}


def usage():
    print "usage: python poem.py <input_file>"


def main(argv):
    if len(argv) == 0:
        usage()
        return 1
    else:
        input = argv[0]
        with open(input) as fp:
            text = ' '.join(map(lambda x: x.strip(), fp.readlines()))
            words = text.split()
            for i in range(len(words)):
                current_word = words[i]
                print 'Current: %s | After: %s' % (current_word, words[i + 1])


if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else [])