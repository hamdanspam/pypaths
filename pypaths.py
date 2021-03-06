# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 22:36:14 2018

@author: Dell
"""

import sys
import os
import pwd

class Pypath:
    def __init__(self):
        pass
    
    def to_native(self, in_path):
        if "\\" in in_path: # if is a windows-style path
            if sys.platform == 'win32':
                return in_path
            else:
                split_path = in_path.split('\\')
        elif '/' in in_path: # if is a linux/mac/other style path
            if sys.platform == 'win32':
                split_path = in_path.split('/')
            else:
                return in_path
        else:
            return os.path.join(in_path) # is already a path, has no delimiters
        
        out_path = ''
        for elem in split_path:
            firstletters = ['C:','E:','D:','F:','G:','H:','I:','J:', 'K:']
            if elem in firstletters and sys.platform == 'win32':
                elem = elem + os.sep
            elif elem in firstletters:
                if elem == 'C:':
                    elem = '~/'
                else:
                    elem = '/media/' + pwd.getpwuid(os.getuid()).pw_name + '/Local Disk/'                
            out_path = os.path.join(out_path, elem) # will work with '' as initial val
        
        return out_path
    
    def join(self, in_list, win=False):
        out_string = ''
        for elem in in_list:
            out_string = os.path.join(out_string, elem)
        
        if win == True:
            out_string = out_string.replace('/', '\\')
            
        return out_string
        
        