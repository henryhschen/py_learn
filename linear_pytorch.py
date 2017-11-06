#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable

x_data = [1, 2, 3]
y_data = [2, 4, 6]

w = Variable(torch.Tensor([1.0]), requires_grad=True)

def forward(x):
	return x*w

def loss(x, y):
	y_pred = forward(x)
	return (y_pred - y) * (y_pred - y)

for epoch in range(1):
	for x_val, y_val in zip(x_data, y_data):
		l = loss(x_val, y_val)
	
	#print("progress:", epoch, "w=", w, "loss=", l)



print("predict (before training)", 4, forward(4).data[0])
#print("predict (after training)", "4 hours", forward(4))
