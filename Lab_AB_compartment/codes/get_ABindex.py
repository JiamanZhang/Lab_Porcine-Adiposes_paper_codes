
import sys
import re
from optparse import OptionParser
import subprocess
import os
import time
import gzip
import numpy as np

#export PATH=/lustre2/home/songyang/software/anaconda2/bin/:$PATH

#excluding the 100kb bin covering the 20kb bin

class generate:

	def __init__ (self,res='',largeres='100000',mychr='',fai="",oe="",pc100kb="",oup=""):

		#self.path = '/Lustre01/tangqianzi/data/HiCmerge/results/'+mytissue
		#self.path2 = '/Lustre01/tangqianzi/data/HiCmerge/results/ABindex/'
		self.input0 = open(fai,'r')
		self.input1 = open(oe,'rb')
		self.input2 = open(pc100kb,'r')
		self.output = open(oup,'w')

		#self.output = open(self.path+'/expected_values.txt','w')
		self.res = res
		#self.name = name
		self.mychr = mychr
		#self.folder = folder
		
		self.largeres = largeres
		
	def generate (self):
	    
	        chr2len={}
	        for line in self.input0:
	               line=line.rstrip()
	               parts=line.split('\t')
	               chr2len[str(parts[0])]=int(parts[1])
	        
	        if chr2len[self.mychr]%int(self.res)==0:
	               mybinnum=chr2len[self.mychr]/int(self.res)
	        else:
	               mybinnum=chr2len[self.mychr]/int(self.res)+1
	               
	        #excluding the last bin smaller than 100kb
	        
	        mybinnum_l=chr2len[self.mychr]/int(self.largeres)
	        
	        count=1
	        Evalues={}
	        for line in self.input2:
	               line=line.rstrip()
	               parts=line.split('\t')
	               if float(parts[3])>0:
	                       Evalues[str(count)]='A'
	               elif float(parts[3])<0:
	                       Evalues[str(count)]='B'
	               else:
	                       Evalues[str(count)]='NA'
	                
	               count+=1
	               
	        myfold=int(self.largeres)/int(self.res)
	        
	        i=0
	        for line in self.input1:
	               line=line.rstrip()
	               parts=line.split('\t')
		       #print(mybinnum)
	               if i<mybinnum:
	                       rowi=i+1	                       
	                       myvalues=[]
	                       for j in range(0,mybinnum):
	                               k=j	                               
	                               coli=k+1
	                               myvalues.append(float(parts[j]))
	                               
	                       if rowi%myfold==0:
	                           
	                               Avalues=[]
	                               Bvalues=[]
	                              
	                               end1=(rowi/myfold-1)
	                               start2=rowi/myfold+1
	                               
	                               for h in range(1,end1+1):
	                                       mystart=(h-1)*myfold+1
	                                       myend=h*myfold
	                                       eachdata=0
	                                       for m in range(mystart-1,myend):
	                                               eachdata+=float(myvalues[m])
	                                       if Evalues[str(h)]=='A':
	                                               Avalues.append(eachdata)
	                                       elif Evalues[str(h)]=='B':
	                                               Bvalues.append(eachdata)
	                                               
	                               for h in range(start2,mybinnum_l+1):
	                                       mystart=(h-1)*myfold+1
	                                       myend=h*myfold
	                                       eachdata=0
	                                       for m in range(mystart-1,myend):
	                                               eachdata+=float(myvalues[m])
	                                       if Evalues[str(h)]=='A':
	                                               Avalues.append(eachdata)
	                                       elif Evalues[str(h)]=='B':
	                                               Bvalues.append(eachdata)	                                       

	                       elif rowi%myfold!=0:
	                               Avalues=[]
	                               Bvalues=[]
	                              
	                               end1=rowi/myfold
	                               start2=rowi/myfold+2
	                               
	                               for h in range(1,end1+1):
	                                       mystart=(h-1)*myfold+1
	                                       myend=h*myfold
	                                       eachdata=0
	                                       for m in range(mystart-1,myend):
	                                               eachdata+=float(myvalues[m])
	                                       if Evalues[str(h)]=='A':
	                                               Avalues.append(eachdata)
	                                       elif Evalues[str(h)]=='B':
	                                               Bvalues.append(eachdata)
	                                               
	                               for h in range(start2,mybinnum_l+1):
	                                       mystart=(h-1)*myfold+1
	                                       myend=h*myfold
	                                       eachdata=0
	                                       for m in range(mystart-1,myend):
	                                               eachdata+=float(myvalues[m])
	                                       if Evalues[str(h)]=='A':
	                                               Avalues.append(eachdata)
	                                       elif Evalues[str(h)]=='B':
	                                               Bvalues.append(eachdata)	                               
	                               
	               #if i<mybinnum:
	                       #rowi=i+1
	                       Aindex=np.mean(Avalues)
	                       Bindex=np.mean(Bvalues)                       
	                       print>>self.output,self.mychr+'\t'+str(i*int(self.res))+'\t'+str((i+1)*int(self.res))+'\t'+str(Aindex-Bindex)                     	                                                      	                               

	                   
	               i+=1
	        
	        
	        
	    
		self.input0.close()
		self.input1.close()
		self.input2.close()
		self.output.close()
			    
	    
def main():

	usage = "usage: %prog [options] <pathandfiles>"
	description = "Generate jobs."

	optparser = OptionParser(version="%prog 0.1",description=description,usage=usage,add_help_option=False)
	optparser.add_option("-h","--help",action="help",help="Show this help message and exit.")

	(options,pathandfiles) = optparser.parse_args()
	
	generate(res=pathandfiles[0],largeres=pathandfiles[1],mychr=pathandfiles[2],fai=pathandfiles[3],oe=pathandfiles[4],pc100kb=pathandfiles[5],oup=pathandfiles[6]).generate()
	
	#generate().generate()


if __name__ == '__main__':

	try:
		main()
	except KeyboardInterrupt:
		sys.stderr.write("User interrupt me! ;-) See you!\n")
		sys.exit(0)
