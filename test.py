#!/usr/local/bin/python3.6

import numpy as np

a = np.arange(6)
print(a, a.dtype, a.shape, a.dtype.itemsize)

b = np.array([[1,2], [3,4]])
print(b, b.dtype, b.shape, b.dtype.itemsize)

import torch
from torch.autograd import Variable

x = torch.randn(4, 4)
print(x.size())
y = x.view(16)
print(y.size())
z = x.view(-1,8)
print(z.size())

