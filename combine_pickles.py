#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Combine all pickles in the folder into one

Expected command line arguments:
  <pickles path> <where to place the result>
"""

import sys
import os
import numpy 
import pickle
import glob

from_where = sys.argv[1]
to_where = sys.argv[2]

data = {'labels': [], 'images': []}
for pic in glob.glob(from_where + '/*.pickle'):
  with open(pic, 'r') as f:
    loaded_data = pickle.load(f)
    data['labels'] += loaded_data['labels']
    data['images'] += loaded_data['images']
with open(to_where, 'w') as f:
  pickle.dump(data,f)

