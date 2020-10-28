# this is the visualization of G1 in condition of G1 matrix existed already

# load your own .csv data
$ import pandas as pd
$ filename = '/data/hu_binwan/Desktop/covariance_gradients.csv'
$ dataframe = pd.read_csv(filename, header=None)

# read the first column of the data 'first gradient G1'
$ G1 = np.array(dataframe[0])

# register our own data to the brainspace
$ from brainspace.datasets import load_group_fc, load_parcellation, load_conte69
$ from brainspace.utils.parcellation import map_to_labels
$ surf_lh, surf_rh = load_conte69()
$ labeling = load_parcellation('schaefer', scale=400, join=True)
$ mask = labeling != 0
$ G1_labelled = map_to_labels(G1, labeling, mask=mask, fill=np.nan)

# plot the brain gradient map (G1 visualization)
$ plot_hemispheres(surf_lh, surf_rh, array_name=G1_labelled, size=(1600, 400), cmap='viridis_r',
                 color_bar=True, label_text=['Grad1'], zoom=1., embed_nb=True)
