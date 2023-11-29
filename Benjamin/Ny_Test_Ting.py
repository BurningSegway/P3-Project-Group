from keras.preprocessing.image import  img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb
import matplotlib.pyplot as plt
import numpy as np

def extract_single_dim_from_LAB_convert_to_RGB(image,idim):
    '''
    image is a single lab image of shape (None,None,3)
    '''
    z = np.zeros(image.shape)
    if idim != 0 :
        z[:,:,0]=80 ## I need brightness to plot the image along 1st or 2nd axis
        z[:,:,idim] = image[:,:,idim]
        z = lab2rgb(z)
        return(z)
    
def plot_lab_spectrums():
    # Get image
    img = img_to_array(load_img("Benjamin\stenbilleder.jpeg",target_size=(400,400)))
    lab = rgb2lab(img/255.0)
    lab_l = extract_single_dim_from_LAB_convert_to_RGB(lab,0)
    lab_a = extract_single_dim_from_LAB_convert_to_RGB(lab,1)
    lab_db = extract_single_dim_from_LAB_convert_to_RGB(lab,2)
    
    # Plot the results
    fig, axes = plt.subplots(ncols=3, figsize=(12, 4))
    data = [('L: lightness', lab_l), ('a: green-magenta channel', lab_a), ('b: blue-yellow channel', lab_db)]
    
    for ax, (title, img) in zip(axes, data):
        ax.set_title(title)
        ax.imshow(img)
        ax.axis('off')
    
    fig.tight_layout()
    plt.show()
    
plot_lab_spectrums()
