import torch

def train_model(model, device, train_loader, regularizer):
  train_loss, train_accuracy, total_train_correct, total_train_processed = 0, 0, 0, 0    
  model.train()
  for batch in train_loader: 
    images, labels = batch
    images, labels = images.to(device), labels.to(device)   

    pred = model(images)
    pred_values = pred.argmax(dim=1, keepdim=True)
    loss = regularizer.loss_function('cross_entropy', pred, labels)
    train_loss += loss.item()

    regularizer.optimizer_step(loss=loss)     
    
    total_train_correct += pred_values.eq(labels.view_as(pred_values)).sum().item()
    total_train_processed += len(images)
    regularizer.optimizer_step(step=1)
    
  train_accuracy = 100*(total_train_correct/total_train_processed)
  train_loss /= len(train_loader.dataset) 
  return train_loss, train_accuracy  