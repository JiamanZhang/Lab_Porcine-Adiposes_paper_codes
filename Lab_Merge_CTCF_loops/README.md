# Lab_Merge_CTCF_loops
# -- codes to fit loop_merge models
## 1. System requirements

- python 3.7
- bedtools

2. Installation guide

- No installation needed
- As an example， execute the following code：
- python merge.loop.py FitHiC.spline_pass1.res5000.significances.30k.2M.Q0.01.ctcf.all.chr.top8000.bed

## 3. Demo

### Input:
- FitHiC.spline_pass1.res5000.significances.30k.2M.Q0.01.ctcf.all.chr.top8000.bed
- Columns of input file are chrom1(1st), start1(2), end1(3), chrom2(4), start2(5), end2(6), qvalue(7)

### Output:
- ctcf.merged.N50.loop.xls

## 4. Instructions for use

Change the hard-coded paths in the code to your own paths where you place the input and output files
Before using this script, you need to get the loop file first. 
