import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import ReduceLROnPlateau

class Regularizations:

  @staticmethod
  def dropout(dropout_value):
    return nn.Dropout(int(dropout_value))

  def __init__(self, optim_type, model, lr, momentum):
    self.optimizer = getattr(optim, optim_type)(getattr(model, 'parameters')(), lr = lr, momentum = momentum)
    self.scheduler = ReduceLROnPlateau(self.optimizer)
    
  def loss_function(self, loss_type, preds, targets):
    return getattr(F,loss_type)(preds, targets)

  def optimizer_step(self, loss=False, step=0):
    if step == 0:
      self.optimizer.zero_grad()
      loss.backward()
      self.optimizer.step()
    elif step != 0:
      self.scheduler.step(step) 
    
