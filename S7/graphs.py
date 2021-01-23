class Graphs:
  

  def __init__(self, *graph_titles):
    self.graph_title = list(range(len(graph_titles)))
    for index in range(len(graph_titles)):
      self.graph_title[index] = graph_titles[index]

  def line_graph(self, figsize, *params):
    fig, axs = plt.subplots(len(params),figsize=figsize)
    for index, param in enumerate(params):      
      axs[index].plot(param,label=self.graph_title[index])
      axs[index].legend(loc='upper right',bbox_to_anchor=(1.25,1))
      axs[index].set_title(self.graph_title[index])
      axs[index].set_xlabel('Epochs')
      axs[index].set_ylabel(self.graph_title[index].split(' ')[1])
    plt.show()

  def image_graph(self, rows, columns, predicted, actual, image):
    fig, ax = plt.subplots(rows, columns,figsize=(10,15))
    for i in range(rows):
      for j in range(columns):
        ax[i,j].imshow(np.transpose(image[(columns*i)+j].cpu()/2 + 0.5, (1,2,0)))
        ax[i,j].set_title(f'Actual : {actual[(5*i)+j]}\nPredicted : {predicted[(5*i)+j]}')
        ax[i,j].axis('off')
    plt.show()

