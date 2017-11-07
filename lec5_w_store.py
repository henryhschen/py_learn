#!/usr/local/bin/python3.6

import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt

torch.manual_seed(8)
x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))
y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))

class Model(torch.nn.Module):
	def __init__(self):
		super(Model, self).__init__()
		self.linear = torch.nn.Linear(1, 1)
	def forward(self, x):
		y_pred = self.linear(x)
		return y_pred

model = torch.nn.Sequential(
	torch.nn.Linear(1, 1)
)
#model = Model()

criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(500):
	y_pred = model(x_data)
	loss = criterion(y_pred, y_data)
	print(epoch, loss.data[0])
	
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()

hour_var = Variable(torch.Tensor([[4.0]]))
print("predict (after training)", model.forward(hour_var).data[0][0])

plt.figure(1, figsize=(10, 3))
plt.subplot(131)
plt.title('Model1')
plt.scatter(x_data.data.numpy(), y_data.data.numpy())
plt.plot(x_data.data.numpy(), model.forward(x_data).data.numpy(), 'r-', lw=5)

torch.save(model, 'model.pkl')			# Save entire model
torch.save(model.state_dict(), 'model_params.pkl')	# Save para

def restore_model():
	model2 = torch.load('model.pkl')
	#print(model2)
	plt.subplot(132)
	plt.title('Model2')
	plt.scatter(x_data.data.numpy(), y_data.data.numpy())
	plt.plot(x_data.data.numpy(), model2(x_data).data.numpy(), 'r-', lw=5)

def restore_params():
	model3 = torch.nn.Sequential(
		torch.nn.Linear(1, 1)
	)
	#print(model3)
	#print(model3.state_dict().keys())
	model3.load_state_dict(torch.load('model_params.pkl'))
	plt.subplot(133)
	plt.title('Model3')
	plt.scatter(x_data.data.numpy(), y_data.data.numpy())
	plt.plot(x_data.data.numpy(), model3(x_data).data.numpy(), 'r-', lw=5)

#print(model)
#print(model.state_dict().keys())
restore_model()
restore_params()
plt.show()

