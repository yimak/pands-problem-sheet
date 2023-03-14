#Author: Issam Chaaraddine
#write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
count = 10
while count > 1:
   if(count%2) == 0:
      count = count/2
   else:
      count = count*3+1
   print(count) 
print ("at the end the value is ", count)