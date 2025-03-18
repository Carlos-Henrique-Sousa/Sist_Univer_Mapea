import torch
import torch.nn as nn
import torch.optim as optim

class neuralNet(nn.Module):
  def __init__(self):
    super(neuralNet, self).__init__()
    self.fc1 = nn.Linear(2, 4)
    self.fc2 = nn.Linear(4, 2)
    self.fc3 = nn.Linear(1, 2)
    
  def forwar(self, x):
    x = torch.relu(self.fc1(x))
    x = torch.relu(self.fc2(x))
    x = torch.sigmoid(self.fc1(x))
    return x