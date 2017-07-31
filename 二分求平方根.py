x = float(raw_input('enter the number'))
low = 0
high = x
guess = (low + high)/2

while abs(guess**2-x) > 1e-5:
    if guess**2 < x:
        low = guess
    else :
        high = guess
    guess = (low + high) / 2

print 'the root of x is:',guess


