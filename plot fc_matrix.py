# use pandas to read data (.csv file)
$ file = '/data/pt_02378/fc_100307.csv'
$ import pandas as pd
$ fc_matrix = pd.read_csv(file,header = None)

# read array
$ import numpy as np
$ fc = np.array(fc_matrix)

# template/parcellation, in my case, Scheafer 400
$ from nilearn import datasets
$ template = datasets.fetch_atlas_schaefer_2018()
$ atlas = template.maps
$ labels = template.labels

# plotting
$ from nilearn import plotting
$ np.fill_diagonal(fc,0)
$ fig = plotting.plot_matrix(fc,figure = (60,60), labels = labels[0:],
                             vmax = 0.8, vmin=-0.8, reorder = False)
