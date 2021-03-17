import torch.nn as nn
import torch.nn.functional as F

class CustomModel(nn.Module):

  def __init__(self):
    super().__init__()
    self.layer_prep = nn.Sequential(
        nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1),
        nn.BatchNorm2d(64),
        nn.ReLU()
    ) # Input -> 32*32*3 || Output -> 32*32*64 || RF -> 

    self.layer_1a = nn.Sequential(
        nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1),
        nn.MaxPool2d(kernel_size=2),
        nn.BatchNorm2d(128),
        nn.ReLU()  
    ) # Input -> 32*32*64 || Output -> 16*16*128 || RF ->
    self.layer_1b = nn.Sequential(
        nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU(),

        nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU()
    ) # Input -> 16*16*128 || Output -> 16*16*128 || RF -> 

    self.layer_2 = nn.Sequential(
        nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding=1),
        nn.MaxPool2d(kernel_size=2),
        nn.BatchNorm2d(256),
        nn.ReLU()
    ) # Input -> 16*16*128 || Output -> 8*8*256 || RF -> 

    self.layer_3a = nn.Sequential(
        nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, stride=1, padding=1),
        nn.MaxPool2d(kernel_size=2),
        nn.BatchNorm2d(512),
        nn.ReLU()
    ) # Input -> 8*8*256 || Output -> 4*4*512 || RF -> 
    self.layer_3b = nn.Sequential(
        nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
        nn.BatchNorm2d(512),
        nn.ReLU(),

        nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding=1),
        nn.BatchNorm2d(512),
        nn.ReLU()
    ) # Input -> 4*4*512 || Output -> 4*4*512 || RF ->
    self.pool = nn.MaxPool2d(kernel_size=4)  # Input -> 4*4*512 || Output -> 1*1*512 || RF ->
    self.fc = nn.Linear(in_features=1*1*512, out_features=10)
    
  def forward(self, image):      
      image = self.layer_prep(image)
      x = self.layer_1a(image)
      r1 = self.layer_1b(x)
      image = x + r1
      image = self.layer_2(image)
      x = self.layer_3a(image)
      r2 = self.layer_3b(x)
      image = x + r2
      image = self.pool(image)      
      image = image.view(-1,512)
      image = self.fc(image)

      return F.log_softmax(image, dim=-1)   

