#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))
p=[]
for i in range(max(a), min(b)+1):
	count =0
	for j in a:
		if(i%j == 0):
			count = count +1
		else:
			break

	if(count == len(a)):
		p.append(i)

print p

k=0
for i in p:
	count =0
	for j in b:
		if(j%i == 0):
			count =  count +1
		else:
			break

	if(count == len(b)):
		k = k+1

print k