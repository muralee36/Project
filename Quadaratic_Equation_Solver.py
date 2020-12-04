#a Simple program to find the solution of Quadratic
import math
a,b,c=map(int,input('Enter the coefficients of quadratic equation: ').split())
dis=b**2-4*a*c
roots=[]
if dis>=0:
    roots.append((-b+math.sqrt(dis))/(2*a))
    roots.append((-b-math.sqrt(dis))/(2*a))
else:
    roots.append(complex(-b/(2*a),math.sqrt(-dis)/(2*a)))
    roots.append(complex(-b/(2*a),-1*math.sqrt(-dis)/(2*a)))
print('The roots are :')
for i in roots:
    print(i)