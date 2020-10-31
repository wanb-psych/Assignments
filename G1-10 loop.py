$ import pandas as pd
$ filename = '/data/hu_binwan/Desktop/covariance_gradients.csv'
$ dataframe = pd.read_csv(filename, header=None)

$ import numpy as np
$ from brainspace.datasets import load_group_fc, load_parcellation, load_conte69
$ from brainspace.utils.parcellation import map_to_labels

$ surf_lh, surf_rh = load_conte69()
$ labeling = load_parcellation('schaefer', scale=400, join=True)
$ mask = labeling != 0

$ grad_labelled = [None] * 10
$ for i in range (10):
    grad_labelled[i] = map_to_labels(np.array(dataframe[i]), labeling, mask=mask, fill=np.nan)
    
$ from brainspace.plotting import plot_hemispheres
$ plot_hemispheres(surf_lh, surf_rh, array_name=grad_labelled, size=(1600, 2800), cmap='viridis_r',
                 color_bar=True, label_text=['Grad 1','Grad 2','Grad 3','Grad 4','Grad 5','Grad 6','Grad 7','Grad 8','Grad 9','Grad 10'], zoom=1.2, embed_nb=True)


