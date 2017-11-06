#!/usr/local/bin/python3.6

import sys;

# 1
#x = 'foo';
#sys.stdout.write(x + '\n');

# 2
#print('# ', len(sys.argv));
#print('Arg: ', str(sys.argv));


import numpy as np
filename = "text"
raw_data = open(filename, "rt")
dataset = np.loadtxt(raw_data, delimiter=",")
print(dataset)
