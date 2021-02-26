test_cases=int(input())
for i in range(test_cases):
	no_of_classes=int(input())
	different_timings=int(input())
	li=[]
	for j in range(no_of_classes):
		n,m=map(int,input().split())
		li.append([n,m])
	d={}
	for l in li:
		if l[0] in d:
			d[l[0]]+=1
		else:
			d[l[0]]=1
		if l[1] in d:
			d[l[1]]+=1
		else:
			d[l[1]]=1
	for l in li:
		for x in d:
			if x>l[0] and x<l[1]:
				d[x]+=1
	print(max(d.values()))