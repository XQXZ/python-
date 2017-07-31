import math 

ch = ''

while ch != 'q':
    a = float(raw_input('enter a:'))
    b = float(raw_input('enter b:'))
    c = float(raw_input('enter c:'))
    if a != 0:
        delta = b**2 - 4*a*c
        if delta < 0:
          print "no solution"
        elif  delta == 0:
          s = -b/(2*a)
          print "%s:",s
        else:
          root = math.sqrt(delta)
          s1 = (-b+root)/(2*a)
          s2 = (-b-root)/(2*a)
          print "two solution:",s1,s2
    ch = raw_input("quit?")

