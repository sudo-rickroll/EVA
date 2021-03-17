import torch
import torchvision
import torchvision.transforms as transforms

class DataProcessing():

  def __init__(self, dataset):     
    self.dataset = dataset 
    self.Transforms_Train, self.Transforms_Test = [],[]

  def Dataset(self, root, train, *Transforms):    
    if train == True:
      for item in Transforms:
        if str(item) not in list(map(str, self.Transforms_Train)) : self.Transforms_Train.append(item)
      return getattr(torchvision.datasets,self.dataset)(root=root, transform=transforms.Compose(self.Transforms_Train))
    else:
      for item in Transforms:
        if str(item) not in list(map(str, self.Transforms_Test)) : self.Transforms_Test.append(item)
      return getattr(torchvision.datasets,self.dataset)(root=root, transform=transforms.Compose(self.Transforms_Test))

  def DataLoader(self, dataset, batch_size=1, shuffle=False, num_workers=0, pin_memory=False):
    return torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers, pin_memory=pin_memory)

  def DataStats(self, dataset):
    if getattr(dataset,'train'):
      if str(getattr(transforms,'ToTensor')()) in list(map(str, self.Transforms_Train)):
        print(f'Length of Dataset : {len(dataset)} \nShape of the Dataset : {dataset.data.shape} \nMax Value: {torch.max(dataset.transform(dataset.data.numpy())).item()} \nMin Value: {torch.min(dataset.transform(dataset.data.numpy())).item()} \nMean : {torch.mean(dataset.transform(dataset.data.numpy())).item()} \nVariance : {torch.var(dataset.transform(dataset.data.numpy())).item()} \nStandard Deviation : {torch.std(dataset.transform(dataset.data.numpy())).item()}')
      else:
        print(f'Length of Dataset : {len(dataset)} \nShape of the Dataset : {dataset.data.shape} \nMax Value: {torch.max(dataset.transform(dataset.data.float())).item()} \nMin Value: {torch.min(dataset.transform(dataset.data.float())).item()} \nMean : {torch.mean(dataset.transform(dataset.data.float())).item()} \nVariance : {torch.var(dataset.transform(dataset.data.float())).item()} \nStandard Deviation : {torch.std(dataset.transform(dataset.data.float())).item()}')
    else:
      if str(getattr(transforms,'ToTensor')()) in list(map(str, self.Transforms_Test)):
        print(f'Length of Dataset : {len(dataset)} \nShape of the Dataset : {dataset.data.shape} \nMax Value: {torch.max(dataset.transform(dataset.data.numpy())).item()} \nMin Value: {torch.min(dataset.transform(dataset.data.numpy())).item()} \nMean : {torch.mean(dataset.transform(dataset.data.numpy())).item()} \nVariance : {torch.var(dataset.transform(dataset.data.numpy())).item()} \nStandard Deviation : {torch.std(dataset.transform(dataset.data.numpy())).item()}')
      else:
        print(f'Length of Dataset : {len(dataset)} \nShape of the Dataset : {dataset.data.shape} \nMax Value: {torch.max(dataset.transform(dataset.data.float())).item()} \nMin Value: {torch.min(dataset.transform(dataset.data.float())).item()} \nMean : {torch.mean(dataset.transform(dataset.data.float())).item()} \nVariance : {torch.var(dataset.transform(dataset.data.float())).item()} \nStandard Deviation : {torch.std(dataset.transform(dataset.data.float())).item()}')
    
  def Transform(self, dataset, *Transforms):
    if getattr(dataset, 'train'):
      for item in Transforms:
        if str(item) not in list(map(str, self.Transforms_Train)) : self.Transforms_Train.append(item)
      dataset.transform = transforms.Compose(self.Transforms_Train)
    else:
      for item in Transforms:
        if str(item) not in list(map(str, self.Transforms_Test)) : self.Transforms_Test.append(item)
      dataset.transform = transforms.Compose(self.Transforms_Test)