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
path_to_data='F:/TESTING/DATASET TESTING'
path_to_test_data='F:/TESTING/TRAIN'
def get_files_from_folder(path):
    for r, d, f in os.walk(path):
      for file in f:
          if ".jpg" in file:
              if(file.startswith('c-', 0, 2)):
      
                  files = file
                 # print(files)
  
    return files
# get dirs
#for r, d, f in os.walk(path_to_data):
 #for dirs in d:
 #  print(dirs) 
#for file in f:   
  #  if ".jpg" in file:
   #   if(file.startswith('c-', 0, 2)):
   #     shutil.copy(os.path.join(r, file), os.path.join( 'F:/TESTING', file))
    

       
_, dirs, _ = next(os.walk(path_to_data))


#for r, d, f in os.walk(path_to_data):
  #    for file in f:
     #     if ".jpg" in file:
          #    if(file.startswith('c-', 0, 2)):
      
                  #files = [file]
                 # print(files)
# calculates how many train data per class
data_counter_per_class = np.zeros((len(dirs)))
print(len(dirs))
for i in range(len(dirs)):
  path = os.path.join(path_to_data, dirs[i])
  print(path)
  
  files = os.listdir(path)
  files=files[0:24]
 # print(files)
 # print(len(files))
  data_counter_per_class[i] = len(files)
  print(data_counter_per_class[i])
  test_counter = np.round(data_counter_per_class * (1 - 0.0))
  print(test_counter)
# transfers files
for i in range(len(dirs)):
  path_to_original = os.path.join(path_to_data, dirs[i])
  path_to_save = os.path.join(path_to_test_data, dirs[i])
  print(path_to_original)
  print(path_to_save)
  if not os.path.exists(path_to_save):
    os.makedirs(path_to_save)
  files = os.listdir(path_to_original)
  print(files)
  #files = get_files_from_folder(path_to_original)
 
  for j in range(int(test_counter[i])):
    dst = os.path.join(path_to_save, files[j])
    #for file in f:
       # if ".jpg" in file:
          #  if(file.startswith('c-', 0, 2)):
    src = os.path.join(path_to_original, files[j])
  
    shutil.copy(src, dst)