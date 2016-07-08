import re
import random

p = re.compile("[\w']+|[,.!?]")

def get_word_count(word_list):
    """This is a helper function that creates a dictionary where the keys are
    each unique word in the iterable parameter passed into the function and the
    values are the number of times each word appears in the list.__add__
    
    Args:
      - word_list: an iterable list of words
      
    Returns: a dictionary that contains the information described in the 
    description aboves
    """
    words = {}
    for word in word_list:
        if word not in words:
            words[word] = 0
        words[word] += 1
    return words.iteritems() 

def weighted_choice(choices):
    """Selects a random key from the parameter passed into the function.
    
    Args:
      - choices: a dictionary where the keys are possible choices and the 
                 values are the weights used when randomly selecting a choice
                 
    Returns: one of the keys in the dictionary passed in  
    """
    choices = [(i, j) for i, j in choices.iteritems()]
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w

class Poet:
    """This class is a utility class which wraps a markov-chain generated from
    text and allows for inifinite generation of sentences. 
    """
    
    def __init__(self):
        self.vertices = {}
        self.totals = {}
        self.current = self.next = self.prev = ""
        
    def feed(self, input_file):
        """This method creates the markov chain used for sentence generation.
        This method must be called before start or get_next().
        
        Args:
            - input_file: the text file to create the markov-chain from
        """
        with open(input_file) as fp:
            text = ' '.join(map(lambda x: x.strip(), fp.readlines()))
            words = p.findall(text)
            
            for i in range(len(words)):
                current_word = words[i].lower()
                if (i + 1) < len(words): 
                    if current_word not in self.vertices:
                        self.vertices[current_word] = []
                    self.vertices[current_word].append(words[i + 1].lower())
            
            for vertex in self.vertices:
                self.vertices[vertex] = { word: count for (word, count) in get_word_count(self.vertices[vertex])}
            
            for vertex in self.vertices:
                current_count = 0
                for word, count in self.vertices[vertex].iteritems():
                    current_count = current_count + count
                self.totals[vertex] = current_count

            for vertex in self.vertices:
                for word in self.vertices[vertex]:
                    self.vertices[vertex][word] = self.vertices[vertex][word] / float(self.totals[vertex])
        self.current = random.choice(self.vertices.keys())
        
    def get_next(self):
        """Gets the next word using a weighted choice where the weights are 
        stored in the markov chain.
        """
        self.prev = self.current
        self.current = weighted_choice(self.vertices[self.current])
        return self.current
        