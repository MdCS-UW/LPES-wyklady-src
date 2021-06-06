#!/usr/bin/python3

def sumTimeList(x):
	m, s = 0, 0
	for t in x:
		t = t.split(":")
		s += int(t[-1])
		m += int(t[-2])
	m += s//60
	s = s%60
	return "{:02d}:{:02d}".format(m, s)

def sumTimeString(x):
	return sumTimeList(x.split("+"))

import sys,re

t = []
for f in sys.argv:
	f = open(f)
	for l in f:
		if re.match("Clip length", l):
			l = l.rstrip().split(" is ")
			t.append(l[1])
			break
	f.close()

print(sumTimeList(t))
