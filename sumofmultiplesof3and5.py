n=int(input('enter the upper limit'))
sum=0
for x in range(1,n):
    if (x%3==0 or x%5==0):
        sum +=x
print(f'The sum of multiples of 3 and 5 under {n} = {sum}')