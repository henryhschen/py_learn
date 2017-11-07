#!/usr/local/bin/python3.6

import numpy as np
import torch

# Transfer
np_data = np.arange(6).reshape(2, 3)
torch_data = torch.from_numpy(np_data)
torch2np_data = torch_data.numpy()

print("numpy\n", np_data)
print("torch\n", torch_data)
print("numpy\n", torch2np_data)

# Function
data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)

print("numpy abs\n", np.abs(data))
print("torch abs\n", torch.abs(tensor))

# Matrix
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)

print("numpy matrix multiply\n", np.matmul(data, data))
print("torch matrix multiply\n", torch.mm(tensor, tensor))

data = np.array(data)
print("numpy matrix dot\n", data.dot(data))
print("torch matrix dot\n", tensor.dot(tensor))



