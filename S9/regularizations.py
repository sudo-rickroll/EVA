import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR

class Regularizations:

  @staticmethod
  def dropout(dropout_value):
    return nn.Dropout(int(dropout_value))

  def __init__(self, optim_type, model, lr, momentum, step_size, gamma):
    self.optimizer = getattr(optim, optim_type)(getattr(model, 'parameters')(), lr = lr, momentum = momentum)
    self.scheduler = StepLR(self.optimizer, step_size=step_size, gamma=gamma)

  def loss_function(self, loss_type, preds, targets):
    return getattr(F,loss_type)(preds, targets)

  def optimizer_step(self, loss=False, step=False):
    if not step:
      self.optimizer.zero_grad()
      loss.backward()
      self.optimizer.step()
    else:
      self.scheduler.step() 
    
