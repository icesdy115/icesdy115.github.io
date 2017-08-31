#coding = utf-8

# def cal(cmd):
# 	ops=['+','-','**','*']
# 	for op in ops:
# 		#print op

# 		cmd = cmd.split(op)
# 		cmd[0] = float(cmd[0])
# 		cmd[1] = float(cmd[1])
# 		if op == '+' : return sum(cmd[0],cmd[1])
# 		if op == '-' : return cmd[0] - cmd[1]
# 		if op == '**' : return pow(cmd[0],cmd[1])
# 		if op == '*' : return cmd[0] * cmd[1]
# def test():
# 	cmd = raw_input ('input:')
# 	ends = cal(cmd)
# 	print ends

# if __name__ == '__main__':
# 	test()

# class closedObject:
# 	def setName(self,name):
# 		self.name = name
# 	def getName(self):
# 		return self.name
# c = closedObject()
# c.setName('test')
# cStr = c.getName()
# print cStr

# class superList(list):
# 	def __sub__(a,b):
# 		a = a[:]
# 		print a
# 		b = b[:]
# 		print b
# 		while len(b) > 0:
# 			e_b = b.pop()
# 			if e_b in a:
# 				a.remove(e_b)
# 		return a
# print superList([1,2,3]) - superList([3,4,5])

# Sum = 0
# x=[2,3,1,5]
# y=[3,2,5,1]

# for x1,y1 in zip(x,y):
# 	Sum = (x1*0.9)+(y1*1.08)
# 	if Sum == 31500:
# 		print x1,y1

list1 = []
for a1 in xrange(11,88,11):
 	list1.append(a1)

Sum = 0
for i in xrange(len(list1)):
	Sum += list1[i]
 	print list1[i]
print Sum
