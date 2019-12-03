#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

n=9
ar=[10,20,20,10,10,30,50,10,20]   
ar.sort()
ar.append(".")
    # return n
# Complete the sockMerchant function below.
#def sockMerchant(n, ar):
    # ar.sort()
    # ar.append(".")
    # # return n
p=0
    # for i in range(n):
    #     if(i<n and ar[i]==ar[i+1]):
    #         p=p+1
    #         i=i+2
ite=0
while(ite<n):
    if(ar[ite]==ar[ite+1]):
        p=p+1
        ite=ite+2
    else:
        ite=ite+1
print(p)