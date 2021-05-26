# Template for writing MapReduce programs using mrjob
# % python mrjob-template.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

import copy 
import sys
orig_stdout = sys.stdout
# print(..., file=orig_stdout) 

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        tmp = line.replace(' ', '')
        tmp = tmp.split(':')
        poi, frds = tmp
        pairs = [(poi, x) for x in frds]
        frds = list(frds)
        lst = []
        for x in frds:
            a = copy.copy(frds)
            a.remove(x)
            lst.append(a)
        ans = list(zip(pairs, lst))
        for x in ans:
            pair, combin = x
            pair = sorted(pair)
            yield pair, combin
        
    def reducer(self, key, values):
        a, b = list(values)
        ans = list(set(a) & set(b))
        ans = sorted(ans)
        yield key, ans
        
if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
    
