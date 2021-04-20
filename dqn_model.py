import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, layers):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"

        # defining fully connected layers of network
        self.fc1 = nn.Linear(state_size, layers)
        self.bn1 = nn.BatchNorm2d(layers)
        self.fc2 = nn.Linear(layers, layers)
        self.bn2 = nn.BatchNorm2d(layers)
        self.fc3 = nn.Linear(layers, action_size)

        # defining dropout with 20% propability
        self.dropout = nn.Dropout(p=0.2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        # x = self.batchnorm1(x)
        # x = self.dropout(x)
        x = F.relu(self.fc2(x))
        # x = self.batchnorm2(x)
        # x = self.dropout(x)
        x = self.fc3(x)
       
        return x