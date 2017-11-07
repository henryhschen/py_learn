#!/usr/local/bin/python3.6

# Numpy method

import numpy as np

Y = np.array([1, 0, 0])
Y_pred1 = np.array([0.7, 0.2, 0.1])
Y_pred2 = np.array([0.1, 0.3, 0.6])

print("loss1 =", np.sum(-Y*np.log(Y_pred1)))
print("loss2 =", np.sum(-Y*np.log(Y_pred2)))

# Torch method
import torch
from torch.autograd import Variable
loss = torch.nn.CrossEntropyLoss()
Y = Variable(torch.LongTensor([0]))

Y_pred1 = Variable(torch.Tensor([[2.0, 1.0, 0.1]]))
Y_pred2 = Variable(torch.Tensor([[0.5, 2.0, 0.3]]))

l1 = loss(Y_pred1, Y)
l2 = loss(Y_pred2, Y)

print("Loss1:", l1.data, "Loss2", l2.data)


# Advance matrix
loss = torch.nn.CrossEntropyLoss()
Y = Variable(torch.LongTensor([2, 0, 1]))

Y_pred1 = Variable(torch.Tensor([[0.1, 0.2, 0.9],
				[1.1, 0.1, 0.2],
				[0.2, 2.1, 0.1]]))
Y_pred2 = Variable(torch.Tensor([[0.8, 0.2, 0.3],
				[0.2, 0.3, 0.5],
				[0.2, 0.2, 0.5]]))

l1 = loss(Y_pred1, Y)
l2 = loss(Y_pred2, Y)

print("Loss1:", l1.data, "Loss2", l2.data)

