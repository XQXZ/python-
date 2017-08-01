count = 0
while True:
    def hanoi(n,A,B,C):
        global count
        if n == 1:
            print 'Move',n,'from',A,'to',C
            count += 1
        else:
            hanoi(n-1,A,C,B)
            print 'Move',n,'from',A,'to',C
            count += 1
            hanoi(n-1,B,A,C)
    
    num = int(raw_input())
    hanoi(num,'Left','Mid','right')
    print count


