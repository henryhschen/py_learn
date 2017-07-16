#!/usr/local/bin/python3.6

import torch
x= torch.Tensor(5,3)
print(x)

x=torch.rand(5,3)
print(x)
print(x.size())

y=torch.rand(5,3)
print(x+y)

print(torch.add(x,y))


result = torch.Tensor(5,3)
torch.add(x, y, out=result)
print(result)

y.add_(x)
print(y)

print(x[:,1])

a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

a.add_(1)
print(a)
print(b)
print("end")

#################
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)

if torch.cuda.is_available():
	x = x.cuda()
	y = y.cuda()
	x+y





