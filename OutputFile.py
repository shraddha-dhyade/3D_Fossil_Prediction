import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import glob
import binvox_rw
import os
import shutil


for view in glob.iglob('species_2/specimen_*/*.binvox'):
    print(view)
    with open(view, 'rb') as f:
        model = binvox_rw.read_as_3d_array(f)
    head,tail = os.path.split(view)
    tail = os.path.splitext(tail)
    print (tail[0])
    #print(model.data)
    #voxel = np.array(model.data).astype(int)
    #np.save(head+'/'+tail[0], voxel)
    os.remove(head +'/' + tail[0] + '.obj')
    #shutil.rmtree(head +'/Views')
