import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

z=0
for i, j in zip(s, t):
	if(i == j):
		z =z+1
	else:
		break


if((len(s) + len(t) - (2*z)) > k):
	print "No"
else:
	print "Yes"