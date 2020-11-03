$ from nilearn import datasets
$ template = datasets.fetch_atlas_schaefer_2018()
$ atlas = template.map
$ labels = template.labels

$ from nilearn.input_data import NiftiLabelsMasker
# standardize is z-score processing
$ masker = NiftiLabelsMasker(labels_img=atlas, standardize=True)
$ time_series = masker.fit_transform('/data/pt_02378/rsfmri/100307/rfMRI_REST1_LR_hp2000_clean.nii.gz', confounds=None)

$ from nilearn.connectome import ConnectivityMeasure
$ correlation_measure = ConnectivityMeasure(kind='correlation')
$ correlation_matrix = correlation_measure.fit_transform([time_series])[0]
# save .csv file
$ import numpy as np
$ np.savetxt('/data/pt_02378/fc.csv', correlation_matrix, delimiter = ',')

$ from nilearn import plotting
# Make a large figure
# Mask the main diagonal for visualization:
$ np.fill_diagonal(correlation_matrix,0)
$ fig = plotting.plot_matrix(correlation_matrix,figure = (60,60), labels = labels[0:],
                             vmax = 0.8, vmin=-0.8, reorder = False)
                            
# caculate gradient accroding to the fc matrix
$ from brainspace.gradient import GradientMaps
$ gm = GradientMaps(n_components=10, random_state=0)
$ gm.fit(correlation_matrix)
$ gradient = gm.gradients_
# save .csv file
$ np.savetxt('/data/pt_02378/gradient_100307.csv', gradient, delimiter = ',')

# using Schaefer 400 parcellation as the template
$ from brainspace.datasets import load_parcellation, load_conte69
$ labeling = load_parcellation('schaefer', scale=400, join=True)
$ surf_lh, surf_rh = load_conte69()
$ from brainspace.utils.parcellation import map_to_labels

# build and plot G1 and G2
$ mask = labeling != 0
$ grad = [None] * 2
$ for i in range(2):
    grad[i] = map_to_labels(gradient[:, i], labeling, mask=mask, fill=np.nan)

$ from brainspace.plotting import plot_hemispheres
$ plot_hemispheres(surf_lh, surf_rh, array_name=grad, size=(1200, 400), cmap='viridis_r',
                 color_bar=True, label_text=['G1', 'G2'], zoom=1.4, embed_nb=True)
