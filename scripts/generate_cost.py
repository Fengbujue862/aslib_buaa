#!/bin/python

'''
    @author: Marius Lindauer
'''

import sys
import os
import arff
import random
import copy
import csv
csv_reader = csv.reader(open("D:\学习资料\实习\附件\数据集\\random\cost.csv"))
i= 0
for row in csv_reader:
	for i,item in enumerate(row):
		# print (item,end='')
		# if i==0:
		# 	print(',1',end='')
		# if i!=len(row)-1:
		# 	print(',', end='')
		if i==0:
			print(item, end='')
			print(',1', end='')
		else:
			print(',ok',end='')
	print()

