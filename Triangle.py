line0 = [6,7,8,9]
line1 = [1,2,6]
line2 = [1,3,7,10]
line3 = [1,4,8,11]
line4 = [1,5,9]
line5 = [2,3,4,5]
line6 = [5,6,10,11]
line = [line0,line1,line2,line3,line4,line5,line6]

num = 0

def cross(a, b):
	result = False
	for i in range(len(a)):
		for j in range(len(b)):
			if a[i] == b[j]:
				result = a[i]
				break
	return result


	
for i in range(0, len(line)):
	for j in range(i+1, len(line)):
		for k in range(j+1, len(line)):
			a = cross(line[i], line[j])
			b = cross(line[j], line[k])
			c = cross(line[i], line[k])
			if a and b and c and a != b:
				num += 1
				print ("No.%d:  %d %d %d" % (num, a, b, c))