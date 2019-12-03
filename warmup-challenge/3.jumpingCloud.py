# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump=0
    #there will be no two consecutive tunderclouds
    #there is possible to always win
    i=0
    n=len(c)
    while i < n-1:
        if(c[i+1]==1):
            i=i+1
            jump = jump +1
        else:
            i=i+2
            jump=jump + 1
    return jump