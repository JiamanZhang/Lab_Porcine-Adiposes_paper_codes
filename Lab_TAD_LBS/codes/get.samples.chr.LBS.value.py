import sys
import os
import gzip 
import numpy as np
import math
def main():
	faifile = sys.argv[1]
	contactfile = sys.argv[2]
	chr = sys.argv[3]
	oup = sys.argv[4]

	f1 = open(faifile,'r')
	fai_dict = {}
	for line1 in f1:
		info1 = line1.strip().split('\t')
		fai_dict[info1[0]] = int(info1[1])
	f1.close()

	chr_len = fai_dict[chr]

	if chr_len%20000 == 0:
		bin_num = chr_len / 20000
	else:
		bin_num = chr_len / 20000 + 1

	bin1 = 0
	f2 = gzip.open(contactfile,'r')
	contact_dict ={}
	for line2 in f2:
		info2 = line2.strip().split('\t')

		for bin2 in range(0,len(info2),1):
			if bin1 > bin2:
				continue
			contact_dict[(bin1,bin2)] = float(info2[bin2])
		bin1+=1
	f2.close()

	out = open(oup,'w')
	for bin_s in range(0,bin_num,1):
		start = bin_s - 15
		end = bin_s+1 + 15

		if start < 0:
			lbs = 'NA'
			info_list = [chr,bin_s*20000,bin_s*20000+20000,lbs]
			out.write('{0}\n'.format('\t'.join([str(i) for i in info_list])))
			continue

		if end > bin_num:
			lbs = 'NA'
			info_list = [chr,bin_s*20000,bin_s*20000+20000,lbs]
			out.write('{0}\n'.format('\t'.join([str(i) for i in info_list])))
			continue

		Aleft_list = []
		Aright_list = []
		B_list = []

		for bin1 in range(start,end,1):
			for bin2 in range(start,end,1):
				if bin1 > bin2:
					continue
				try:
					contact = contact_dict[(bin1,bin2)]
				except KeyError as reason:
					continue

				if (bin1 >= start and bin1 < bin_s) and (bin2>= start and bin2 < bin_s):
					Aleft_list.append(contact)
				elif (bin1 >=bin_s+1 and bin1 < end) and (bin2 >=bin_s+1 and bin2 < end):
					Aright_list.append(contact)
				else:
					B_list.append(contact)
		
		lbs=math.log((sum(Aleft_list)+sum(Aright_list))/(sum(B_list)),2)
		info_list = [chr,bin_s*20000,bin_s*20000+20000,lbs]

		out.write('{0}\n'.format('\t'.join([str(i) for i in info_list])))
	out.close()

if __name__ == '__main__':
	main()