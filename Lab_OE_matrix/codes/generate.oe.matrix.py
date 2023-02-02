import sys
import gzip
mat=sys.argv[1]
chr=sys.argv[2]
fai=sys.argv[3]
res=int(sys.argv[4])
oup1=sys.argv[5]
oup2=sys.argv[6]

CID={}
FAI=open(fai,"r")
for line in FAI:
	line=line.strip()
	lis=line.split("\t")
	CID[lis[0]]=int(lis[1])
FAI.close()

NR=CID[chr]/res+1
#print(NR)

if mat.endswith(".gz"):
	MAT=gzip.open(mat,"r")
else:
	MAT=open(mat,'r')
NF=0

sdis={}
ndis={}
for line in MAT:
	NF+=1
	line=line.strip()
	lis=line.split("\t")
	num=len(lis)
	#print(num)
	if(num!=NR):
		exit("Matrix is not in correct format!")
	for i in range(num):
		if i+1>=NF:
			dis=i+1-NF
			ndis.setdefault(dis,0.0)
			sdis.setdefault(dis,0.0)
			if(lis[i]!="NaN"):
				ndis[dis]+=1
				sdis[dis]+=float(lis[i])
		else:
			continue
MAT.close()
#print(NF)
if (NF!=NR):
	exit("Matrix is not in correct format!")
##############generate_expected_value
EP={}
OUP=open(oup1,'w')
for key in sorted(sdis.keys()):
	EP[key]=sdis[key]/ndis[key]
	OUP.writelines(str(key)+'\t'+str(sdis[key]/ndis[key])+'\t'+chr+'\t'+str(key*res)+"\n")
OUP.close()
###############generate_oe_matrix
#OUP=gzip.open(oup2,'wt',compresslevel=1)
OUP=open(oup2,'w')
if mat.endswith(".gz"):
        MAT=gzip.open(mat,"r")
else:
        MAT=open(mat,'r')
NF=0
for line in MAT:
	NF+=1
	line=line.strip()
	lis=line.split("\t")
	num=len(lis)
	lout=[]
	for i in xrange(num):
		dis=abs(i+1-NF)
		#if sdis[dis]/ndis[dis]==0:
		if EP[dis]==0:
			lout.append(str(0))
		else:
			#exp=sdis[dis]/ndis[dis]
			lout.append(str(float(lis[i])/EP[dis]))
	OUP.writelines("\t".join(lout)+"\n")
OUP.close()
