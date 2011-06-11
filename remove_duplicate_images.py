#!/usr/bin/python

import hashlib
import os
from glob import glob
from PIL import Image

filelist = glob('*')

shabefore = {}
histbefore = []

for file in filelist:
    myfh = open(file, 'r')
    myhash = hashlib.sha256(myfh.read()).hexdigest()

    #remove files that have the same hash
    if shabefore.has_key(myhash):
        print("Duplicate detected, deleteing: %s" % (file))
        os.unlink(file)
    else:
        shabefore[myhash] = file
    
    #remove files that have the same histogram
    try:
        myhist = Image.open(file).histogram()
    except IOError:
        print("Error Reading %s" % (file))

    if myhash in histbefore:
        print("Duplicate Detected: %s" % file)
        try:
            os.unlink(file)
        except OSError:
            print("Unable to remove file: %s" % file)
    else:
        histbefore.append(myhash)
