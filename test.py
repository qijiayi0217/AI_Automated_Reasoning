class Negation:
	def __init__(self,a):
		self.bool=(not a.bool)
		self.link=a
	def update(self):
		tmp=self.link
		self.bool=(not tmp.bool)

class And:
	def __init__(self,a,b):
		self.bool=(a.bool and b.bool)
		self.link1=a
		self.link2=b
	def update(self):
		tmp1=self.link1
		tmp2=self.link2
		self.bool=(tmp1.bool and tmp2.bool)

class Or:
	def __init__(self,a,b):
		self.bool=(a.bool or b.bool)
		self.link1=a
		self.link2=b
	def update(self):
		tmp1=self.link1
		tmp2=self.link2
		self.bool=(tmp1.bool or tmp2.bool)
class Arrow:
	def __init__(self,a,b):
		self.bool=arrow(a.bool,b.bool)
		self.link1=a
		self.link2=b
	def update(self):
		tmp1=self.link1
		tmp2=self.link2
		self.bool=arrow(tmp1.bool,tmp2.bool)

def arrow(a,b):
	if (a and b) or (not a and b) or (not a and not b):
		return True
	elif (a and not b):
		return False
class Arrow2:
	def __init__(self,a,b):
		self.bool=arrow2(a.bool,b.bool)
		self.link1=a
		self.link2=b
	def update(self):
		tmp1=self.link1
		tmp2=self.link2
		self.bool=arrow2(tmp1.bool,tmp2.bool)

def arrow2(a,b):
	if (a and b) or (not a and not b):
		return True
	elif (not a and b) or (a and not b):
		return False
class obj:
	def __init__(self,a):
		self.bool=a
	def set(self,b):
		self.bool=b


def TT_entails(KB,a,variables):
	symbols=[]
	for i in range(len(KB)):
		if isinstance(KB[i],obj) and KB[i] not in symbols:
			symbols.append(KB[i])
	for i in range(len(a)):
		if isinstance(a[i],obj) and a[i] not in symbols:
			symbols.append(a[i])
	model=[]
	return TTcheckall(KB,a,symbols,model,variables)

def TTcheckall(KB,a,symbols,model,variables):
	if len(symbols)==0:
		if PL_true(KB,model,variables):
			#print("stop")
			return PL_true(a,model,variables)
		else:
			return True
	else:
		p=symbols[0]
		if len(symbols)==1:
			rest=[]
		else:
			rest=symbols[1:]
		model1=model[:]
		model2=model[:]
		model1.append(True)
		model2.append(False)
		return (TTcheckall(KB,a,rest,model1,variables) and TTcheckall(KB,a,rest,model2,variables))

def PL_true(a,model,variables):
	#print(model)
	for i in range(len(model)):
		variables[i].set(model[i])
	for i in range(len(a)):
		if not isinstance(a[i],obj):
			a[i].update()
	if a[-1].bool==True:
		print(model)
	return a[-1].bool

A=obj(True)
B=obj(True)
C=obj(True)
negc=Negation(C)
arr1=Arrow2(A,negc) #first
and1=And(A,C)
arr2=Arrow2(B,and1)#second
arr3=Arrow2(C,B)#thrid
t1=And(arr1,arr2)
t2=And(t1,arr3)
KB=[A,B,C,negc,arr1,and1,arr2,arr3,t1,t2]

#we can easily find out that C always equals to B
alpha7=4*[None]
mo=4*[None]
nega=Negation(A)
negb=Negation(B)
negc=Negation(C)
tmp11=And(A,B)
tmp12=And(tmp11,C)
alpha7[0]=[A,B,C,tmp11,tmp12]
mo[0]=[True,True,True]
tmp21=And(nega,B)
tmp22=And(tmp21,C)
alpha7[1]=[A,B,C,tmp21,tmp22]
mo[1]=[False,True,True]
tmp31=And(A,negb)
tmp32=And(tmp31,negc)
alpha7[2]=[A,B,C,tmp31,tmp32]
mo[2]=[True,False,False]
tmp41=And(nega,negb)
tmp42=And(tmp41,negc)
alpha7[3]=[A,B,C,tmp41,tmp42]
mo[3]=[False,False,False]
print('Liars and Truth-tellers (b):\n')
for s in range(4):
	sym=[]
	for i in range(len(KB)):
		if isinstance(KB[i],obj) and KB[i] not in sym:
			sym.append(KB[i])
	for i in range(len(alpha7[s])):
		if isinstance(alpha7[s][i],obj) and alpha7[s][i] not in sym:
			sym.append(alpha7[s][i])
	print(len(alpha7[s]))
	print(TT_entails(KB,alpha7[s],sym))
	print("A,B,C:")
	print(mo[s])




