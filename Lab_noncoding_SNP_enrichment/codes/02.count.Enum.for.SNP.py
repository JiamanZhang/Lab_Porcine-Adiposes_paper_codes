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
sta=[['group','inactive.num','RE.num','SE.num','inactive.gwas.num','RE.gwas.num','SE.gwas.num','inactive.gwas.ratio','RE.gwas.ratio','SE.gwas.ratio','SE.RE.Pvalue','RE.inactiveE.Pvalue']]
da1=[i.strip().split() for i in open('%s'%inp)]
da1=["_".join(i[:3]+[i[-1]]) for i in da1]
da1=[i for i in set([j for j in da1])]
in1=[i for i in da1 if i.split('_')[-1]=='inactive']
re1=[i for i in da1 if i.split('_')[-1]=='RE']
se1=[i for i in da1 if i.split('_')[-1]=='SE']
da2=[i.strip().split() for i in open('%s.overlap.with.noncoding.gwas.xls'%inp.split('.')[0])]
da2=["_".join(i[3:6]+[i[-2]]) for i in da2]
da2=[i for i in set([j for j in da2])]
in2=[i for i in da2 if i.split('_')[-1]=='inactive']
re2=[i for i in da2 if i.split('_')[-1]=='RE']
se2=[i for i in da2 if i.split('_')[-1]=='SE']
testout1=stats.chi2_contingency([[len(re1)-len(re2),len(re2)],[len(se1)-len(se2),len(se2)]],False)
testout2=stats.chi2_contingency([[len(in1)-len(in2),len(in2)],[len(re1)-len(re2),len(re2)]],False)
sta.append([inp.split('.')[0],len(in1),len(re1),len(se1),len(in2),len(re2),len(se2),float(len(in2))/len(in1),float(len(re2))/len(re1),float(len(se2))/len(se1),testout1[1],testout2[1]])
np.savetxt('sta.gwas.num.xls',sta,delimiter='\t',fmt='%s')
