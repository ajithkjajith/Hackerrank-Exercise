s="aba"
n=10

count = s.count("a")
rem = n%len(s)
r = n//len(s)
s=s[:rem]
print((count*r)+s.count("a"))

#k = s.count("a")*(n/len(s))
#k += s[:n%len(s)].count("a")
#print k