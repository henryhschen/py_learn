#!/usr/local/bin/python3.6

import torch
from torch.autograd import Variable

x = Variable(torch.ones(2, 2), requires_grad=True)
print("X Variable with requires_grad=True", x)

y = x+2
print("y=x+2\n", y)

print("y creator\n", y.creator)

z = y * y * 3
out = z.mean()
print("z = y*y*3\n", z, "Mean of z", out)

out.backward()
print(x.grad)

x = torch.randn(3)
x = Variable(x, requires_grad=True)

y = x * 2
print(y)
while y.data.norm() < 1000:
	y = y*2

print(y)

gradients = torch.FloatTensor([0.1, 1.0, 0.0001])
print(gradients)
y.backward(gradients)
print(x.grad)


