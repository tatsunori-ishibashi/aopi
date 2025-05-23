sum=0
for i in range(10001):
    if i%13==0:
        sum+=i
    elif i%17==0:
        sum+=i
print(sum)