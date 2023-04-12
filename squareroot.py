N=float(input('Please enter a positive number: '))
approx=1
sqrt=1+1
while (approx!=sqrt):
    approx=sqrt
    sqrt=0.5*(approx+N/approx)
    if approx==sqrt:
        continue
print('The square root of 14.5 is approx ', sqrt)
