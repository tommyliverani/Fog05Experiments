import os
import time
import datetime
import csv


f=open('raw/out_destination.txt')
out = open("out_destination.csv", "w")
writer=csv.writer(out)
line=f.readline()

while line:
	lis=line.split()
	row=[]
	row.append(100-int(lis[14]))
	row.append(4028776 - int(lis[3]))
	writer.writerow(row)
	line=f.readline()
out.close()
