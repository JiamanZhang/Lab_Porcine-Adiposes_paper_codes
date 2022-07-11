import sys
import os
def main():
	tissue = sys.argv[1]
	pos = sys.argv[2]

	inp = 'whole.ULB.samples.txt'
	f1 = open(inp,'r')
	sample_list = []
	for line1 in f1:
		sample = line1.strip()
		sample_list.append(sample)
	f1.close()

	boundary_list = []
	for sample in sample_list:
		inp = sample+'.chr18.TAD.boundary.txt'
		f1 = open(inp,'r')
		for line1 in f1:
			info1 = line1.strip().split('\t')
			chr = int(info1[0])

			center = int(info1[1])
			boundary_list.append((chr,center))
		f1.close()

	uniq_list = sorted(list(set(boundary_list)),key=lambda x:(x[0],x[1]))

	oup = 'whole.'+pos+'.'+tissue+'.uniq.booundary.txt'
	out = open(oup,'w')
	for a_list in uniq_list:
		info_list = [a_list[0],a_list[1]]
		out.write('{0}\n'.format('\t'.join(map(str,info_list))))
	out.close()


if __name__ == '__main__':
	main()