def test_model(model, device, test_set, test_loader, regularizer, wrong_preds, correct_labels, wrong_pred_images, last_epoch):
  test_loss, test_accuracy, total_test_correct, total_test_processed = 0, 0, 0, 0    
  model.eval()
  for batch in test_loader: 
    images, labels = batch
    images, labels = images.to(device), labels.to(device) 
    
    pred = model(images)
    pred_values = pred.argmax(dim=1, keepdim=True)
    loss = regularizer.loss_function('cross_entropy', pred, labels)
    test_loss += loss.item() 
    if last_epoch:
      misclassified_images(test_set, pred_values, labels, images, wrong_preds, correct_labels, wrong_pred_images)

    total_test_correct += pred_values.eq(labels.view_as(pred_values)).sum().item()
    total_test_processed += len(images)
    
  test_accuracy = 100*(total_test_correct/total_test_processed)
  test_loss /= len(test_loader.dataset) 
  return test_loss, test_accuracy