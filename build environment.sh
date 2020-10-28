# ~/data/hu_binwan

# install conda
$ cd Downloads
$ bash Anaconda3-2020.07-Linux-x86_64.sh

# creat environment
$ conda create --name lateral python=3.7

# install jupyterlab and brainspace
$ conda install -c conda-forge jupyterlab
$ pip install brainspace

$ jupyter-lab


"""
now we can use jupyter notebook to write script under the environment of lateral
"""
