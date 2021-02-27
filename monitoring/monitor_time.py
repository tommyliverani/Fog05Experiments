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

"""
while True:
	time.sleep(1)
	os.system('vmstat > tmp.txt')
	f = open("tmp.txt", "r")
	line= f.readline()
	line= f.readline()
	line= f.readline()
	f.close()
	cpu_usage=int(line.split()[14])
	ram_usage=4028776-int(line.split()[3])
	vm_usage=float(line.split()[16])
	out = open("out.csv", "a")
	writer=csv.writer(out)
	row=[]
	row.append(datetime.datetime.now())
	row.append(cpu_usage)
	row.append(ram_usage)
	row.append(vm_usage)
	writer.writerow(row)
	out.close()
	print(line.split())
	#print('{} | {} | {} |{}'.format(datetime.datetime.now(),cpu_usage,ram_usage,vm_usage))

"""


while True:
	time.sleep(1)
	out = open("time.csv", "a")
	writer=csv.writer(out)
	row=[]
	row.append(datetime.datetime.now())
	writer.writerow(row)
	print(datetime.datetime.now())
	out.close()


