#!/usr/local/bin/python3.6

import torch

# Uninitialized 5x3 torch.Tensor(5,3)
x_tensor = torch.Tensor(5,3)

# Initialized 5x3 torch.rand(5,3)
x_rand = torch.rand(5,3)
print("Tensor vs. Rand\n", x_tensor, x_rand)
print("Tensor vs. Rand\n", x_tensor.size(), x_rand.size())

y_rand = torch.rand(5,3)
print("Add 1\n", x_rand+y_rand, torch.add(x_rand, y_rand))

result = torch.Tensor(5,3)
torch.add(x_rand, y_rand, out=result)
print("Add 2\n", result)

y_rand.add_(x_rand)
print("y add_\n", y_rand, x_rand[:,1])

a = torch.ones(5)
print("a as torch ones", a)

b = a.numpy()
print("b as a numpy\n",b)

a.add_(1)
print("Add a add_\n", a)
print("b\n", b)
print("Torch end")

#################
import numpy as np
a = np.ones(5)
print("a np ones\n", a)
b = torch.from_numpy(a)
print("b as a torch\n", b)
np.add(a, 1, out=a)
print("a add\n", a)
print("b\n", b)

if torch.cuda.is_available():
	x = x.cuda()
	y = y.cuda()
	x+y
else:
	print("CUDA isn't available")


