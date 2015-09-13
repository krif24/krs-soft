#! /usr/bin/python

our_bulls = [l.rstrip().decode('utf-8').lower().split("\t") for l in open('tmp', 'r')]
our_bulls = set('-'.join(w.rstrip().lstrip() for w in s) for s in our_bulls)

all_bulls = {}
for l in open('allbulls.bik', 'r'):
	data = [w.lstrip().rstrip() for w in l.rstrip().decode('utf-8').lower().split("|")]
	id = "%s-%s" % (data[1], data[2])
	all_bulls[id] = data
	
for l in open('tmp2', 'r'):
	data = l.rstrip().decode('utf-8').lower().split("\t")
	id = "-".join(w.rstrip().lstrip() for w in data)
	if id not in all_bulls:
		print "%s,0,not found" % id.encode('utf-8')
	else:
		current_id = id
		parent_list = []
		while current_id in all_bulls:
			data = all_bulls[current_id]
			parent_list.append(current_id)
			current_id = "%s-%s" % (data[9], data[10])
			# print current_id
		print ("%s,%d,%s" % (id, len(parent_list)-1, "->".join(parent_list))).encode('utf-8')
	
	# if id in our_bulls:
	# 	print data[0]