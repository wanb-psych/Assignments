$ import pandas as pd
$ filename = '/data/hu_binwan/Desktop/covariance_gradients.csv'
$ dataframe = pd.read_csv(filename, header=N

$ import numpy as np
$ grad = [None] * 10
$ for i in range (10):
    grad[i] = np.array(dataframe[i])

$ from brainspace.datasets import load_group_fc, load_parcellation, load_conte69
$ from brainspace.utils.parcellation import map_to_labels
$ surf_lh, surf_rh = load_conte69()
$ labeling = load_parcellation('schaefer', scale=400, join=True)
$ mask = labeling != 0

# G1 = grad [0]
$ G1_labelled = map_to_labels(grad[0], labeling, mask=mask, fill=np.nan)

$ from brainspace.plotting import plot_hemispheres
$ plot_hemispheres(surf_lh, surf_rh, array_name=G1_labelled, size=(1600, 400), cmap='viridis_r',
                 color_bar=True, label_text=['Grad1'], zoom=1., embed_nb=True)
