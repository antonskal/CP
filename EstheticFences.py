from itertools import product, chain
from more_itertools import powerset, set_partitions

def alternating(ell):
	count_reds = 0
	count_blues = 0
	for i in ell:
		if i[1] == 'r':
			count_reds+=1
		else:
			count_blues+=1
	return count_reds == count_blues and count_reds + count_blues >= 4
#You are given nfence parts, each colored either blue or red. 
#Each fence part has a length and a color. 
#We need to build a triangular fence using some or all of these parts. 
#For esthetic reasons, adjacent parts of this triangular fence have to have different colors.
def generate_combinations(red,blue):
	reds = list(powerset(red))[1:]
	blues = list(powerset(blue))[1:]
	cross = list((product(reds,blues)))
	cross = [tuple(chain.from_iterable(x)) for x in cross]
	triangles = set(filter(alternating,cross))
	return triangles



def degenerate(a,b,c):
	count = [0,0,0]
	for i in a:
		count[0] += int(i[0])
	for i in b:
		count[1] += int(i[0])
	for i in c:
		count[2] += int(i[0])
	count.sort()
	if count[0] + count[1] > count[2]:
		return count[0] * count[1] * count[2]
	else:
		return 0
def esthetic_fences():
	n = int(input())
	red = []
	blue = []
	for i in range(n):
		ell = input().split(" ")
		if ell[1] == 'r':
			red.append((ell[0])+ell[1])
		else:
			blue.append(ell[0]+ell[1])


	 
	reds = list(powerset(red))[1:]
	blues = list(powerset(blue))[1:]
	cross = list((product(reds,blues)))
	cross = [tuple(chain.from_iterable(x)) for x in cross]
	triangles = set(filter(alternating,cross))

	m = 0
	for i in triangles:
		ell = list(set_partitions(i,3))	
		for triangle in ell:
			c = degenerate(triangle[0],triangle[1],triangle[2])
			m = max(c,m)
	print(m)
					
			
esthetic_fences()
			
