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
        nums = line.split(' ')
        for x in nums:
            yield x, 1

    def reducer(self, key, values):
        lst = list(values)
        tot = sum(lst)
        if tot %2 == 0:
            outcome = 'Even'
        else:
            outcome = 'Odd'
        yield outcome, 1
    
    def reducer_2(self, key, values):
        lst = list(values)
        tot = sum(lst)
        if 'Odd' in key:
            outcome = bool(tot == 2 | tot == 0)
            yield 'Euler path:', outcome
        else:
            yield 'Euler path:', 'True'
        
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_2)
        ]

if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
    
