import os
import time
import datetime
import csv


f=open('monitor_source.txt')
out = open("out_source.csv", "w")
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
