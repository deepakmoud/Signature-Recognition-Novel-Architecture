# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 13:35:53 2022

@author: deepak
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:58:11 2022

@author: deepak
"""
import pandas as pd
import numpy as np
import os
import cv2


        
import shutil
import os
import numpy as np
import argparse
path='F:/TESTING'
path_to_data='F:/TESTING/TRAIN'
path_to_test_data='F:/TESTING/TEST'
def get_files_from_folder(path):
  files = os.listdir(path)
  return np.asarray(files)
# get dirs
for r, d, f in os.walk(path_to_data):
  for dirs in d:
    print(dirs) 


_, dirs, _ = next(os.walk(path_to_data))

# calculates how many train data per class
data_counter_per_class = np.zeros((len(dirs)))
print(len(dirs))
for i in range(len(dirs)):
  path = os.path.join(path_to_data, dirs[i])
  print(path)
  
  files = get_files_from_folder(path)
  print(len(files))
  data_counter_per_class[i] = len(files)
  print(data_counter_per_class[i])
  test_counter = np.round(data_counter_per_class * (1 - 0.2))
  print(test_counter)
# transfers files
for i in range(len(dirs)):
  path_to_original = os.path.join(path_to_data, dirs[i])
  path_to_save = os.path.join(path_to_test_data, dirs[i])
  print(path_to_original)
  print(path_to_save)
  if not os.path.exists(path_to_save):
    os.makedirs(path_to_save)
  files = get_files_from_folder(path_to_original)
  for j in range(int(test_counter[i])):
    dst = os.path.join(path_to_save, files[j])
    src = os.path.join(path_to_original, files[j])
    shutil.move(src, dst)