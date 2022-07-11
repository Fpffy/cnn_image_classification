
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg




def join_path(path_1='', path_2=''):
    return os.path.join(path_1, path_2).replace('\\', '/')



def join_path_list(path='', list_of_paths=[]):
    return [join_path(path, photo) for photo in list_of_paths]



def rotate_image(image_path=False, image_array=np.array, rotations=3):
    
    if image_path:
        im = mpimg.imread(image_path)
    else:
        im = image_array
        
    rgb = []
    
    for channel in range(im.shape[2]):
        im_channel = im[:, :, channel]
        im_channel = np.rot90(im_channel, rotations)
        rgb.append(im_channel)
 
    rotated_im = np.dstack((rgb[0], rgb[1], rgb[2]))
    rotated_im = np.array(rotated_im, dtype=np.uint8)
    
    return rotated_im



def plot_transforms(generators=list, img=np.array,
                       figsize=(12.5, 12.5), ncols=4):
    
    fig, axs = plt.subplots(nrows=len(generators), ncols=ncols, figsize=figsize) 

    for row, gen in zip(range(len(generators)), generators):
        for col in range(ncols):
            transformed_img = np.array(gen.random_transform(img), dtype=np.uint8)
            axs[row, col].imshow(transformed_img)
            axs[row, col].axis('off')

    plt.tight_layout()
    plt.show()