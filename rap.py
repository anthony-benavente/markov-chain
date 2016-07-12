#!/usr/bin python

import sys, re

from poet import Poet

EXIT_FAILURE = 1
REGEX_PUNC = re.compile('[.!?,]')
USAGE = 'usage: python rap.py <input_file> <num_words>'


def usage_and_quit():
    """This function prints out the usage method of the program and quits."""
    print USAGE
    sys.exit(EXIT_FAILURE)


def main(argv):
    """ This is the main entry point to the program. This program generates a 
    set of rap lyrics using a markov chain generated from the passed in data
    set. 
    
        usage: python rap.py <input_file> <num_words>
    
    Arguments:
      - input_file - this is the file to create the markov chain 
    """
    if len(argv) < 2:
        usage_and_quit()
    
    poet = Poet()
    poet.feed(argv[0])
    
    out = ''
    num_words = int(argv[1])
    for i in range(num_words):
        next = poet.get_next()
        out += next + ' '
        if REGEX_PUNC.match(next):
            print out
            out = ''
        print out
    
  
if __name__ == '__main__':
    main(sys.argv[1:])