import os
import time
import datetime
import csv
"""
while True:
	time.sleep(1)
	os.system('top -u fos -n 1 | grep fos > tmp.txt')
	f = open("tmp.txt", "r")
	line= f.readline()
	cpu_usage=0.0
	while line:
		cpu_usage=cpu_usage + float(line.split()[9].replace(',','.'))
		line=f.readline()
	f.close
	out = open("out.csv", "a")
	writer=csv.writer(out)
	line=[]
	line.append(datetime.datetime.now())
	line.append(cpu_usage)
	writer.writerow(line)
	out.close()
	print(cpu_usage)
"""


while True:
	time.sleep(1)
	os.system('vmstat > tmp.txt')
	f = open("tmp.txt", "r")
	line= f.readline()
	line= f.readline()
	line= f.readline()
	cpu_usage=float(line.split()[12])
	ram_usage=4028776-float(line.split()[3])
	out = open("out.csv", "a")
	writer=csv.writer(out)
	line=[]
	line.append(datetime.datetime.now())
	line.append(cpu_usage)
	line.append(ram_usage)
	writer.writerow(line)
	out.close()
	print('{} | {} | {}'.format(datetime.datetime.now(),cpu_usage,ram_usage))
