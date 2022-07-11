#wangdanyang
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import os
import random
import sklearn
import pandas as pd
from scipy import stats
from matplotlib.colors import LinearSegmentedColormap
from operator import itemgetter
import sys
import seaborn as sns
import subprocess

inp=sys.argv[1]
log=[]
log.append(subprocess.getstatusoutput('bedtools intersect -a obesity.trait.SNP-noncoding -b %s -wo >%s.overlap.with.noncoding.gwas.xls'%(inp,inp.split('.')[0])))
print(log)
