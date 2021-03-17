import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch.optim.lr_scheduler import OneCycleLR

class Regularizations:

  @staticmethod
  def dropout(dropout_value):
    return nn.Dropout(int(dropout_value))

  def __init__(self, optim_type, model, lr, momentum, max_lr, len_loader, weight_decay=0):
    self.optimizer = getattr(optim, optim_type)(getattr(model, 'parameters')(), lr = lr, momentum = momentum, weight_decay = weight_decay)
    self.scheduler = OneCycleLR(self.optimizer, max_lr=max_lr, steps_per_epoch=len_loader,
                       epochs=24, div_factor=10, final_div_factor=1,
                       pct_start=5/24)
    
  def loss_function(self, loss_type, preds, targets):
    return getattr(F,loss_type)(preds, targets)

  def optimizer_step(self, loss=False, step=0):
    if step == 0:
      self.optimizer.zero_grad()
      loss.backward()
      self.optimizer.step()
    elif step != 0:
      self.scheduler.step()
    
