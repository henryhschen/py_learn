#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt

w = 1.0
x_data = [1, 2, 3]
y_data = [2, 4, 6]

def forward(x):
	return x*w

def loss(x, y):
	y_pred = forward(x)
	return (y_pred - y) * (y_pred - y)

w_list = []
mse_list = []
for w in np.arange(0.0, 4.1, 0.1):
	print("w=", w)
	l_sum = 0
	for x_val, y_val in zip(x_data, y_data):
		y_pred_val = forward(x_val)
		l = loss(x_val, y_val)
		l_sum += l
		print("\t", x_val, y_val, y_pred_val, l)

	#print("MSE=", l_sum/len(x_data))
	w_list.append(w)
	mse_list.append(l_sum/len(x_data))

#plt.plot(w_list, mse_list)
#plt.ylabel('Loss')
#plt.xlabel('w')
#plt.show()
print("predict (before traning)", 4, forward(4))

def gradient(x, y):
	return 2*x*(x*w-y)

for epoch in range(100):
	for x_val, y_val in zip(x_data, y_data):
		grad = gradient(x_val, y_val)
		w = w - 0.01 * grad
		print("\tgrad:", x_val, y_val, grad)
		l = loss(x_val, y_val)
	
	print("progress:", epoch, "w=", w, "loss=", l)
print("predict (after training)", "4 hours", forward(4))
