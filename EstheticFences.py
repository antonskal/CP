from itertools import groupby, combinations, chain
import functools

def powerset(iterable):
    "powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def alternating(fences):
        count_reds = 0
        count_blues = 0
        for i in fences:
                if i[1] == 'r':
                        count_reds+=1
                else:
                        count_blues+=1
        return count_reds == count_blues and count_reds + count_blues >= 4

#a b and c are sorted
def degenerate(a,b,c):
        return a+b <= c
def calculate_sorted_triangle(triangle):
    max = 0
    result = []
    for i in range(0,len(triangle)-2):
        for j in range(i+1,len(triangle)-1):
            for k in range(j+1,len(triangle)):
                mapped_triangle = triangle[0:j],triangle[j:k],triangle[k:len(triangle)]
                a = functools.reduce(lambda x, y: x + int(y[0]), mapped_triangle[0],0)
                b = functools.reduce(lambda x, y: x + int(y[0]), mapped_triangle[1],0)
                c = functools.reduce(lambda x, y: x + int(y[0]), mapped_triangle[2],0)
                ell = sorted([a,b,c])
                if not degenerate(ell[0],ell[1],ell[2]) and a*b*c > max:
                    max = a*b*c

                
    return max

n = int(input())
fences = []
for i in range(n):
    fences.append(input().replace(" ",""))

#Pre-Process into triangles with Equal Red and Blue Sides
fences = list(k for k,_ in groupby(filter(lambda x: alternating(x), powerset(fences))))

#Pre-Process into Alternating Red and Blue configurations '1r,2b,3r,4b'
sorted_result = []
for triangle in fences:
    reds = []
    blues = []
    merged = []
    for side in triangle:
        if side[1] == 'r':
            reds.append(side)
        else:
            blues.append(side)
    while(reds and blues):
        merged.append(reds.pop(0))
        merged.append(blues.pop(0))
    if not reds:
        merged.extend(blues)
    else:
        merged.extend(reds)
    sorted_result.append(merged)      
sorted_result
max = 0
for i in sorted_result:
    product_of_all_sides = calculate_sorted_triangle(i)
    if product_of_all_sides > max:
        max = product_of_all_sides
print(max)
    