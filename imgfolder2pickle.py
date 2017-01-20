#!/usr/bin/env python

from scipy import misc
import glob
import sys
import os
import numpy as np
import pickle

"""Convert all images in the folder into pickle and save

Assumption is that all of the images in the same folder have the same label.

Expected command line arguments:
  <folder path> <label to use>
"""

folder_path = sys.argv[1]
label_to_use = sys.argv[2]
pickle_name = folder_path + '/' + os.path.realpath(folder_path).split('/')[-1] + '.pickle'

data = {'labels': [], 'images': []}
for image_path in glob.glob(folder_path + "/*.png"):
  image = misc.imread(image_path)
  data['images'].append(image)
  data['labels'].append(label_to_use)

with open(pickle_name, 'wb') as f:
  pickle.dump(data, f)
