x=0
y=1
z=0
sum=0
n=int(input('enter the inclusive upper limit : '))
while(z<=n):
    z=x+y
    if (z%2==0):
        sum+=z
    x=y
    y=z
print(sum)

