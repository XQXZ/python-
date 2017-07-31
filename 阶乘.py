#e = 1 + 1/1! + 1/2! +...+ 1/i!
e = 1
factory = 1

for i in range(1,100):
    factory *= i
    e += 1./factory

print "e is",e
