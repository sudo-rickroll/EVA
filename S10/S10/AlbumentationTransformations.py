import numpy as np

class AlbumentationTransforms:
    
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, img):
        img = np.array(img)
        for t in self.transforms:
            img = t(image=img)["image"]
        return img

    def __repr__(self):
        format_string = '\n'
        for t in self.transforms:            
            format_string += '    {0}'.format(t)
            format_string += '\n'
        
        return format_string
