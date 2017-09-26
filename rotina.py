#!/usr/bin/env python
from random import randint
import numpy as np

for i in xrange(3,11):
 filewrite=open("matriz"+str(i)+".dat", 'w')
 filewrite.write(str(i)+"\n")
 x=np.zeros((i,i), float)
 for tt in xrange(0,i):
  for t in xrange(0,i):
   filewrite.write(str(randint(0,10))+"  ")
  filewrite.write("\n") 
 filewrite.close()
