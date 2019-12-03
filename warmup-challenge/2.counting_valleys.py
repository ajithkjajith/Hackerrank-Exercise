#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Complete the countingValleys function below.
def countingValleys(n, s):
    s=s+"."
    count=0 #for level
    v=0
    for i in range(n):
        if s[i]=="U":
            count=count+1
            if count==0:
                v=v+1
        else:
            count=count-1
    return v