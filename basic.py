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
	#print(variables)
	for i in range(len(model)):
		variables[i].set(model[i])
	for i in range(len(a)):
		if not isinstance(a[i],obj):
			a[i].update()
	#print(a[-1].bool)
	return a[-1].bool

#Modus Ponens
P=obj(False)
Q=obj(False)
#c=obj(True)
#n=Negation(a.bool)
arr=Arrow(P,Q)
s=And(P,arr)

KB=[P,Q,arr,s] #KB[-1] is the whole sentence
alpha=[Q]
sym1=[]
for i in range(len(KB)):
	if isinstance(KB[i],obj) and KB[i] not in sym1:
		sym1.append(KB[i])
for i in range(len(alpha)):
	if isinstance(alpha[i],obj) and alpha[i] not in sym1:
		sym1.append(alpha[i])
#print(KB)
print('Modus Ponens\n')
print("{P,P=>Q}|=Q: ")
print(TT_entails(KB,alpha,sym1))
print('\n')
# wumpus world(simple)
P11=obj(False)
neg1=Negation(P11) #first condition
B11=obj(True)
P12=obj(True)
P21=obj(True)
or1=Or(P12,P21)
arr1=Arrow2(or1,B11) #second condition
B21=obj(False) #fifth condition
P22=obj(True)
P31=obj(True)
or2=Or(P11,P22)
or3=Or(or2,P31)
arr2=Arrow2(or3,B21) #third condition
neg2=Negation(B11) #fourth condition
t1=And(neg1,arr1)
t2=And(t1,arr2)
t3=And(t2,neg2)
t4=And(t3,B21) #all
KB2=[P11,neg1,B11,P12,P21,or1,arr1,B21,P22,P31,or2,or3,arr2,neg2,t1,t2,t3,t4]
alpha2=[P12]
sym2=[]
for i in range(len(KB2)):
	if isinstance(KB2[i],obj) and KB2[i] not in sym2:
		sym2.append(KB2[i])
for i in range(len(alpha2)):
	if isinstance(alpha2[i],obj) and alpha2[i] not in sym2:
		sym2.append(alpha2[i])

print("Wumpus World (Simple)\n")
print("P12: ")
print(TT_entails(KB2,alpha2,sym2))
print("\n")

#Horn clause
Myth=obj(True)
imm=obj(True)
arr3=Arrow(Myth,imm) #first
neg3=Negation(Myth)
neg4=Negation(imm)
mam=obj(True)
and1=And(neg4,mam)
arr4=Arrow(neg3,and1) #second
or4=Or(imm,mam)
horned=obj(True)
arr5=Arrow(or4,horned) #thrid
magical=obj(True)
arr6=Arrow(horned,magical) #fourth
t5=And(arr3,arr4)
t6=And(t5,arr5)
t7=And(t6,arr6) #total
KB3=[Myth,imm,arr3,neg3,neg4,mam,and1,arr4,or4,horned,arr5,magical,arr6,t5,t6,t7]
alpha3=[Myth]
alpha4=[magical]
alpha5=[horned]
sym3=[]
for i in range(len(KB3)):
	if isinstance(KB3[i],obj) and KB3[i] not in sym3:
		sym3.append(KB3[i])
for i in range(len(alpha3)):
	if isinstance(alpha3[i],obj) and alpha3[i] not in sym3:
		sym3.append(alpha3[i])
sym4=[]
for i in range(len(KB3)):
	if isinstance(KB3[i],obj) and KB3[i] not in sym4:
		sym4.append(KB3[i])
for i in range(len(alpha4)):
	if isinstance(alpha4[i],obj) and alpha4[i] not in sym4:
		sym4.append(alpha4[i])
sym5=[]
for i in range(len(KB3)):
	if isinstance(KB3[i],obj) and KB3[i] not in sym5:
		sym5.append(KB3[i])
for i in range(len(alpha5)):
	if isinstance(alpha5[i],obj) and alpha5[i] not in sym5:
		sym5.append(alpha5[i])
print('Horn clause\n')
print('Unicorn is mythical:')
print(TT_entails(KB3,alpha3,sym3))
print('Unicorn is magical:')
print(TT_entails(KB3,alpha4,sym4))
print('Unicorn is horned:')
print(TT_entails(KB3,alpha5,sym5))
print('\n')

#Liars and Truth-tellers (a)
A=obj(False)
B=obj(False)
C=obj(True)
and1=And(C,A)
arr1=Arrow2(A,and1) #first
neg1=Negation(C)
arr2=Arrow2(B,neg1) #second
neg2=Negation(A)
or1=Or(B,neg2)
arr3=Arrow2(C,or1) #thrid
t1=And(arr1,arr2)
t2=And(t1,arr3)
KB=[A,B,C,and1,arr1,neg1,arr2,neg2,or1,arr3,t1,t2]
#print(t2.bool)
nega=Negation(A)
negb=Negation(B)
negc=Negation(C)
alpha=6*[None]
mo=6*[None]
#ABC can not all be true or all be false
tmp10=And(A,B)
tmp20=And(tmp10,negc)
alpha[0]=[A,B,C,tmp10,tmp20]
mo[0]=[True,True,False]
tmp11=And(A,negb)
tmp21=And(tmp11,C)
alpha[1]=[A,B,C,tmp11,tmp21]
mo[1]=[True,False,True]
tmp12=And(nega,B)
tmp22=And(tmp12,C)
alpha[2]=[A,B,C,tmp12,tmp22]
mo[2]=[False,True,True]
tmp13=And(nega,negb)
tmp23=And(tmp13,C)
alpha[3]=[A,B,C,tmp13,tmp23]
mo[3]=[False,False,True]
tmp14=And(nega,B)
tmp24=And(tmp14,negc)
alpha[4]=[A,B,C,tmp14,tmp24]
mo[4]=[False,True,False]
tmp15=And(A,negb)
tmp25=And(tmp15,negc)
alpha[5]=[A,B,C,tmp15,tmp25]
mo[5]=[True,False,False]
print('Liars and Truth-tellers (a):\n')
for s in range(6):
	sym=[]
	for i in range(len(KB)):
		if isinstance(KB[i],obj) and KB[i] not in sym:
			sym.append(KB[i])
	for i in range(len(alpha[s])):
		if isinstance(alpha[s][i],obj) and alpha[s][i] not in sym:
			sym.append(alpha[s][i])
	if(TT_entails(KB,alpha[s],sym)):
		print("A,B,C:")
		print(mo[s])
	

#Liars and Truth-tellers (b)
A=obj(True)
B=obj(False)
C=obj(False)
negc=Negation(C)
arr1=Arrow2(A,negc) #first
and1=And(A,C)
arr2=Arrow2(B,and1)#second
arr3=Arrow2(C,B)#thrid
t1=And(arr1,arr2)
t2=And(t1,arr3)
KB=[A,B,C,negc,arr1,and1,arr2,arr3,t1,t2]
#print(t2.bool)
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
#print(tmp32.bool)
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
	#print(len(alpha7[s]))
	if(TT_entails(KB,alpha7[s],sym)):
		print("A,B,C:")
		print(mo[s])
#print(TT_entails(KB,alpha7[s],sym))



