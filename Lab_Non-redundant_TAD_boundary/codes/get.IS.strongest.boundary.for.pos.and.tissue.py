import sys
import os
import numpy as np
def main():
	tissue = sys.argv[1]
	chr = sys.argv[2]
	pos = sys.argv[3]

	inp = 'whole.ULB.samples.txt'
	f1 = open(inp,'r')
	sample_list = []
	for line1 in f1:
		sample = line1.strip()
		sample_list.append(sample)
	f1.close()
	print pos,tissue,len(sample_list)

	IS_dict = {}
	difpos_dict = {}
	for i in [tissue]:
		difpos_dict[i] = {}

	for sample in sample_list:
		inp = sample+'.chr'+chr+'.IS.value.txt'
		f1 = open(inp,'r')
		name = sample.split('_')[0]
		for line1 in f1:
			info1 = line1.strip().split('\t')
			if info1[0] != chr:
				# print info1
				continue
			if info1[0] != chr:
				print 'this is wrong@@'
				sys.exit(0)

			start = int(info1[1])
			try:
				IS_dict[start].append(info1[-1])
			except KeyError as reason:
				IS_dict[start] = []
				IS_dict[start].append(info1[-1])

			if info1[-1] != 'NA':
				try:
					difpos_dict[name][start].append(float(info1[-1]))
				except KeyError as reason:
					difpos_dict[name][start] = []
					difpos_dict[name][start].append(float(info1[-1]))

		f1.close()

	inp = 'whole.'+pos+'.'+tissue+'.uniq.booundary.txt'
	f1 = open(inp,'r')
	ISvalue_dict = {}
	ISvalue_list = []
	for line1 in f1:
		info1 = line1.strip().split('\t')
		if chr != info1[0]:
			continue
		start = int(info1[1])

		if len(IS_dict[start]) != len(sample_list):
			print 'this is wrong!!!~'
			print len(IS_dict[start]),len(sample_list)
			sys.exit(0)

		IS_list = IS_dict[start]
		NA_num = IS_list.count('NA')

		if NA_num/float(len(sample_list)) >= 0.5:
			continue

		m_list = []
		for i in IS_list:
			if i == 'NA':
				continue
			m_list.append(float(i))

		mean_num = np.mean(m_list)

		ISvalue_list.append((chr,start,mean_num))
		ISvalue_dict[(chr,start)] = IS_list
	f1.close()

	ISvalue_list.sort(key=lambda x:x[2])

	strong_list = []
	while len(ISvalue_list) >0:
		a_list = ISvalue_list[0]
		strong_list.append(a_list)
		
		start = a_list[1]

		all_list = []
		for b_list in ISvalue_list:
			if b_list[1] >= (start-100000) and b_list[1] < (start+100000):
				continue
			all_list.append(b_list)

		ISvalue_list = all_list
		ISvalue_list.sort(key=lambda x:x[2])

	strong_list.sort(key=lambda x:x[1])

	oup = 'whole.'+pos+'.'+tissue+'.'+chr+'.strong.boundary.txt'
	out = open(oup,'w')
	info_list = ['chr','center_boundary']+[tissue+'_mean_IS']
	out.write('{0}\n'.format('\t'.join(map(str,info_list))))

	for a_list in strong_list:
		info_list = list(a_list)
		start = a_list[1]
		out.write('{0}\n'.format('\t'.join(map(str,info_list))))
	out.close()


if __name__ == '__main__':
	main()
