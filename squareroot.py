N=14.5
approx=1
sqrt=1+1
while (approx!=sqrt):
    approx=sqrt
    sqrt=0.5*(approx+N/approx)
    if approx==sqrt:
        continue
print(sqrt)