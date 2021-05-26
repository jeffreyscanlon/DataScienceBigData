# Template for writing MapReduce programs using mrjob
# % python mrjob-template.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

import sys
orig_stdout = sys.stdout
# print(..., file=orig_stdout) 

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        orig= line.replace(' ','') 
        tmp = ''.join((sorted(orig)))
        if '?' in tmp:
            sort_word = tmp[1:]
        else:
            sort_word = tmp
        yield sort_word, orig
        
    def reducer(self, key, values):
        for x in values:
            if '?' in x:
                yield x, values
        
if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
    
