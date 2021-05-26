# Template for writing MapReduce programs using mrjob
# % python mrjob-template.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

import sys
orig_stdout = sys.stdout
# print(..., file=orig_stdout) 

# change the name of the class
class MR_program(MRJob):
    
    def configure_args(self):
        super(MR_program, self).configure_args()
        self.add_passthru_arg('-M')

    def mapper(self, _, line):
        args = self.options.M
        r1, c1, r2, c2 = args.split(',')
        r1 = int(r1)
        c2 = int(c2)
        line = line.replace(' ','')
        line = list(line)
        tag = line.pop(0)
        val = line.pop(2)
        coord = line
        x = int(0 if coord[0] is None else coord[0])
        y = int(0 if coord[1] is None else coord[1])
        if tag == 'A':
            for i in range(c2):
                yield (x, i), val
        if tag == 'B':
            for i in range(r1):
                yield (i, y), val

    def reducer(self, key, values):
        yield key, values

if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
    
