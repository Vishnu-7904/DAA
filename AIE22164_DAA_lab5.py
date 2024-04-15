
#candy problem
n=int(input(""))
arr=[]
for i in range(0,n):
    arr.append(int(input("")))
print(arr)

rating=1
temp=[]
for i in range(0,n-1):
    if(arr[i] > arr[i+1]):
        temp.append(rating)
        rating = 1
    if(arr[i] < arr[i+1]):
        temp.append(rating)
        rating += 1
    if(arr[i] == arr[i+1]):
        temp.append(rating)
        rating = 1
temp.append(rating)
print(temp)
print(sum(temp))

#goodman city
n, k=input("").split()
print(n,k)

c=list(map(int,input("").split()))
print(c)

for i in range(0,n):
    if(c[i]==0):
        if( 1 in c[i:i+k]):
            print(c[i+k])
        else:
            print(-1)
