import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import glob
import binvox_rw
import os
import shutil


with open('specimen_00_2.binvox', 'rb') as f:
	model = binvox_rw.read_as_3d_array(f)
	voxel = np.array(model.data).astype(int)
	np.save('y_64.npy', voxel)

