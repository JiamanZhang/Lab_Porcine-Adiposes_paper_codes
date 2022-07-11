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

##total number of SNPs
snp_num=2710.0
##base number of genome
genome_size=2265774640.0

inp=sys.argv[1]
sta=[['group','nAE.SNP.ratio','RE.SNP.ratio','SE.SNP.ratio','nAE.genome.ratio','RE.genome.ratio','SE.genome.ratio','nAE.enrichment','RE.enrichment','SE.enrichment']]
allnum=[i.strip().split() for i in open('sta.gwas.num.xls')]
allnum={i[0]:i[1:] for i in allnum[1:]}
da2=[i.strip().split() for i in open('%s.overlap.with.noncoding.gwas.xls'%inp.split('.')[0])]
da2=["_".join(i[:3])+'-'+"_".join(i[3:6]+[i[-2]]) for i in da2]
da2=[i for i in set([j for j in da2])]
tmp1=[k for k in da2 if k.split('_')[-1]=='inactive']
tmp2=[k for k in da2 if k.split('_')[-1]=='RE']
tmp3=[k for k in da2 if k.split('_')[-1]=='SE']
sta.append([inp.split('.')[0],len(tmp1)/snp_num,len(tmp2)/snp_num,len(tmp3)/snp_num,float(allnum[inp.split('.')[0]][0])*5000/genome_size,float(allnum[inp.split('.')[0]][1])*5000/genome_size,float(allnum[inp.split('.')[0]][2])*5000/genome_size,len(tmp1)/snp_num/(float(allnum[inp.split('.')[0]][0])*5000/genome_size),len(tmp2)/snp_num/(float(allnum[inp.split('.')[0]][1])*5000/genome_size),len(tmp3)/snp_num/(float(allnum[inp.split('.')[0]][2])*5000/genome_size)])
np.savetxt('sta.gwas.enrichment.per.E.xls',sta,delimiter='\t',fmt='%s')
