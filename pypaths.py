# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 22:36:14 2018

@author: Dell
"""

import sys
import os

class Pypath:
    def __init__(self):
        pass # nothing, really
    
    def to_native(self, in_path):
        if "\\" in in_path: # if is a windows-style path
            split_path = in_path.split('\\')
        elif '/' in in_path: # if is a linux/mac/other style path
            split_path = in_path.split('/')
        else:
            return os.path.join(in_path) # is already a path, has no delimiters
        
        out_path = ''
        
#        if 'C:' in split_path:
#            split_path[:] = [('C:' + os.sep) if elem == 'C:' for elem in split_path]
        
        for elem in split_path:
            if elem == 'C:':
                elem = 'C:' + os.sep
                
            out_path = os.path.join(out_path, elem) # will work with '' as initial val
        
        return out_path
            
            