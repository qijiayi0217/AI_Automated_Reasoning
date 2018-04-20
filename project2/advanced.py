def pl_resolution(KB,nota):
	#KB nota contain a list of object
	clause=[]
	for i in range(len(KB)):
		if KB[i] not in clause:
			clause.append(KB[i])
	for i in range(len(nota)):
		if nota[i] not in clause:
			clause.append(nota[i])
	new=[]
	while 1:
		for i in range(len(clause)-1):
			for j in range(i+1,len(clause)):
				resolvents=pl_resolve(clause[i],clause[j]) #list
				#print(resolvents)
				if [] in resolvents:
					return True
				for s in range(len(resolvents)): #new<-new U resolvents
					if resolvents[s] not in new:
						new.append(resolvents[s])
		check=0
		for i in range(len(new)):
			if new[i] not in clause:
				check=1
				clause.append(new[i])
				#print(clause)
		if check==0:
			return False

def pl_resolve(list1,list2):
	#print(list1)
	#print(list2)
	new=[]
	for i in range(len(list1)):
		for j in range(len(list2)):
			#print(list1[i]+list2[j])
			if list1[i]+list2[j]==0:
				if i!=len(list1)-1 and j!=len(list2)-1:
					tmp=list1[:i]+list1[i+1:]+list2[:j]+list2[j+1:]
					tmp=list(set(tmp))
					tmp.sort()
					if tmp not in new:
						new.append(tmp)
				elif i==len(list1)-1 and j!=len(list2)-1:
					tmp=list1[:i]+list2[:j]+list2[j+1:]
					tmp=list(set(tmp))
					tmp.sort()
					if tmp not in new:
						new.append(tmp)
				elif i!=len(list1)-1 and j==len(list2)-1:
					tmp=list1[:i]+list2[:j]+list1[i+1:]
					tmp=list(set(tmp))
					tmp.sort()
					if tmp not in new:
						new.append(tmp)
				elif i==len(list1)-1 and j==len(list2)-1:
					tmp=list1[:i]+list2[:j]
					tmp=list(set(tmp))
					tmp.sort()
					if tmp not in new:
						new.append(tmp)
	return new

#Modus Ponens
#{P,P=>Q}|=Q
#CNF format
#KB :P,(not P V Q)
#alpha: Q
#use 1 represent P 2 represent Q
p=1
q=2
KB=[[p],[-p,q]]
for element in KB:
	element.sort()
alpha=[[q]]
notalpha=[[-q]]
print("Modus Ponens:")
print("{P,P=>Q}|=Q: ")
print(pl_resolution(KB,notalpha))
print()

#Wumpus World(Simple)
#CNF format
#KB:not p11,not b11 V p12 V p21,not p12 V b11, not p21 V b11
#not b21 V p11 V p22 V p31,not p11 V b21, not p22 V b21, not p31 V b21
#not b11
#b21
#alpha: p12
p11=1
b11=2
p12=3
p21=4
b21=5
p22=6
p31=7
KB=[[-p11],[-b11,p12,p21],[-p12,b11],[-p21,b11],[-b21,p11,p22,p31],[-p11,b21],[-p22,b21],[-p31,b21],[-b11],[b21]]
for element in KB:
	element.sort()
alpha=[[p12]]
notalpha=[[-p12]]
print("Wumpus World(Simple)")
print('P12:')
print(pl_resolution(KB,notalpha))
print()

#Horn Clauses
#CNF format
#KB: not Mythical V imm, Mythical V not imm, Mythical V mam,
#not imm V horned, not mam V horned, not horned V magical
#alpha1: Mythical
#alpha2: Magical
#alpha3: horned
Mythical=1
imm=2
mam=3
horned=4
magical=5
KB=[[-Mythical,imm],[Mythical,-imm],[Mythical,mam],[-imm,horned],[-mam,horned],[-horned,magical]]
for element in KB:
	element.sort()
alpha1=[[Mythical]]
alpha2=[[magical]]
alpha3=[[horned]]
not1=[[-Mythical]]
not2=[[-magical]]
not3=[[-horned]]
print('Horn Clause')
print('Mythical:')
print(pl_resolution(KB,not1))
print('\nMagical:')
print(pl_resolution(KB,not2))
print('\nhorned:')
print(pl_resolution(KB,not3))

#Liars and Truth-tellers (a)
#CNF format
#KB:not a V a, not a V c, not a V not c V a
#not b V not c, c V b
#not c V b V not a, not b V c, a V c
#alpha:a,b,c
a=1
b=2
c=3
KB=[[-a,a],[-a,c],[-a,-c,a],[-b,-c],[c,b],[c,b,-a],[-b,c],[a,c]]
for element in KB:
	element.sort()
alpha1=[[a]]
alpha2=[[b]]
alpha3=[[c]]
not1=[[-1]]
not2=[[-2]]
not3=[[-3]]
print('Liars and Truth-tellers (a)')
print('A:')
print(pl_resolution(KB,not1))
print('\nB:')
print(pl_resolution(KB,not2))
print('\nC:')
print(pl_resolution(KB,not3))
#Liars and Truth-tellers (b)
#CNF format
#KB:not a V not c, c V a, not b V a, not b V c, not a V not c V b
#not c V b, not b V c
#alpha:a,b,c
KB=[[-a,-c],[c,a],[-b,a],[-b,c],[-a,-c,b],[-c,b],[-b,c]]
for element in KB:
	element.sort()
print('Liars and Truth-tellers (b)')
print('A:')
print(pl_resolution(KB,not1))
print('\nB:')
print(pl_resolution(KB,not2))
print('\nC:')
print(pl_resolution(KB,not3))


