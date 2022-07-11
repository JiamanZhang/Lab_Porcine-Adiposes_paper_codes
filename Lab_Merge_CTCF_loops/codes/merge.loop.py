#wangdanyang
import scipy as sp
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
import numpy as np
import subprocess

inp=sys.argv[1]
log=[]
da=[i.strip().split() for i in open(inp)]
da=[[int(i[0]),int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5]),i[6]] for i in da]
out=sorted(da,key=itemgetter(0,1,2,4,5))
out1=[]
out2=[]
for i in range(len(out)):
	if i%2==0:
		out1.append(out[i])
	else:
		out2.append(out[i])
np.savetxt('round1.bed',out1,delimiter='\t',fmt='%s')
np.savetxt('round2.bed',out2,delimiter='\t',fmt='%s')
log.append(subprocess.getstatusoutput('bedtools pairtopair -f 0 -is -a round1.bed -b round2.bed >finish1_merge.bed'))
log.append(subprocess.getstatusoutput('bedtools pairtopair -f 0 -is -type notboth -a round1.bed -b round2.bed >finish1_retain1.bed'))
log.append(subprocess.getstatusoutput('bedtools pairtopair -f 0 -is -type notboth -b round1.bed -a round2.bed >finish1_retain2.bed'))
for n in range(1,50):
	merge=[i.strip().split() for i in open('finish%s_merge.bed'%n)]
	out=[]
	for i in merge:
		if int(i[1])<=int(i[8]):
			x1=i[1]
		else:
			x1=i[8]
		if int(i[2])>=int(i[9]):
			x2=i[2]
		else:
			x2=i[9]
		if int(i[4])<=int(i[11]):
			y1=i[4]
		else:
			y1=i[11]
		if int(i[5])>=int(i[12]):
			y2=i[5]
		else:
			y2=i[12]
		out.append([i[0],x1,x2,i[0],y1,y2,i[6]])
	np.savetxt('finish%s_merge.merge'%n,out,delimiter='\t',fmt='%s')
	log.append(subprocess.getstatusoutput('cat finish%s_merge.merge finish%s_retain1.bed finish%s_retain2.bed |sort|uniq >round%s'%(n,n,n,n+1)))
	da=[i.strip().split() for i in open('round%s'%(n+1))]
	da=[[int(i[0]),int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5]),i[6]] for i in da]
	out=sorted(da,key=itemgetter(0,1,2,4,5))
	out1=[]
	out2=[]
	for i in range(len(out)):
		if i%2==0:
			out1.append(out[i])
		else:
			out2.append(out[i])
	np.savetxt('round%s_1.bed'%(n+1),out1,delimiter='\t',fmt='%s')
	np.savetxt('round%s_2.bed'%(n+1),out2,delimiter='\t',fmt='%s')
	log.append(subprocess.getstatusoutput('bedtools pairtopair -f 0 -is -a round%s_1.bed -b round%s_2.bed >finish%s_merge.bed'%(n+1,n+1,n+1)))
	log.append(subprocess.getstatusoutput('bedtools pairtopair -f 0 -is -type notboth -a round%s_1.bed -b round%s_2.bed >finish%s_retain1.bed'%(n+1,n+1,n+1)))
	log.append(subprocess.getstatusoutput('bedtools pairtopair -f 0 -is -type notboth -b round%s_1.bed -a round%s_2.bed >finish%s_retain2.bed'%(n+1,n+1,n+1)))
log.append(subprocess.getstatusoutput('cat finish50_retain1.bed finish50_retain2.bed |sort|uniq >ctcf.merged.N50.loop.xls'))
log.append(subprocess.getstatusoutput('rm finish*'))
log.append(subprocess.getstatusoutput('rm round*'))
print(log)
