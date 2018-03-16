import re

def parser(fname):
	f = open(fname, 'r')
	dico = {}
	table = {}
	i = 1
	for l in f:
		m = re.match('^([0-9]+) (O|M)([a-zA-Z0-9_\-\.:\'!?]+)',l)
		if m:
			key = m.group(1)+m.group(2)
			name = m.group(3)
			if key not in dico:
				dico[key] = set()
			if name not in table:
				table[name] = i
				i+=1
			dico[key].add(table[name])
	return dico, table

def writeSet(dico, table, fname):
	f = open(fname, 'w')
	for a in dico:
		sorted_a = sorted(dico[a])
		line = ' '.join(map(str, sorted_a))
		f.write(line+'\n')

#def LCM(fname):
