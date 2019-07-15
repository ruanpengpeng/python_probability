import random
n=10000000
count=0
for i in range(n):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x*x+y*y<=1:
       count=count+1
print(4*float(count)/float(n))